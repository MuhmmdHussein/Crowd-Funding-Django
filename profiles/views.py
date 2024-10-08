from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from authentication.models import Register
from home.models import Project
from profiles.forms import EditProfileForm
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ObjectDoesNotExist

from projects.models import Donation,Project


# Create your views here.


def profile (request):
    if 'user_id'  in request.session :
        try:
            user_object= Register.objects.get(id = request.session['user_id'])
            projects =Project.objects.filter(created_by =  user_object )
            donations = Donation.objects.filter(user =  user_object )
            
            images = []
            for project in projects:
                first_image = project.images.first()
                if first_image and first_image.image: 
                    images.append(first_image.image.url)  
                else:
                    images.append(None)
            project_images = zip(projects, images)

        except Register.DoesNotExist:
            return redirect('/')
        
        return render(request, 'profile/Profile.html', {"user" :user_object ,"donations":donations,"projects":projects,'project_images':project_images})
    else:
        return redirect("/" )
    # return render(request, 'profile/Profile.html')
   


def EditProfile(request):
    if 'user_id' not in request.session:
        return redirect('/')

    user_object = get_object_or_404(Register, id=request.session['user_id'])
    form = EditProfileForm(request.POST or None, request.FILES or None, instance=user_object)

    if request.method == 'POST' and form.is_valid():
        # Update password if provided
        if form.cleaned_data['password']:
            form.instance.password = make_password(form.cleaned_data['password'])

        form.save()
        return redirect('profile')

    return render(request, 'profile/editProfile.html', {'form': form, "user": user_object})

# @login_required  
# def delet_account(request):
#     if request.method=='POST':
#         request.user.delete()
#         messages.success(request, 'Deleted account done')
#         return redirect('/')
#     return render(request, 'profile/Profile.html')

def delet_account(request):
    if 'user_id' in request.session:
        try:
            user = Register.objects.get(id=request.session['user_id'])
        except ObjectDoesNotExist:
            messages.error(request, 'User does not exist.')
            return redirect('login')  

        user.delete()

        del request.session['user_id']

        messages.success(request, 'Account deleted successfully.')

        
        return redirect('/')  
    else:
        return redirect('login')