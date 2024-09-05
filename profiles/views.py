from django.shortcuts import redirect, render
from authentication.models import Register
from home.models import Project
from profiles.forms import EditProfileForm

# Create your views here.


def profile (request):
    if 'user_id'  in request.session :
        try:
            user_object= Register.objects.get(id = request.session['user_id'])
            projects =Project.objects.filter(user_id =  request.session['user_id'] )
            # donations = Donation.objects.filter(user_id =  request.session['user_id'] )
            
            images = []
            for project in projects:
                images.append(project.image_set.all().first().images.url)

        except Register.DoesNotExist:
            return redirect('/')
        
        
        return render(request, 'profile/Profile.html', {"user" :user_object ,"projects":projects ,'images':images})
    else:
        return redirect("/" )
    # return render(request, 'profile/Profile.html')
   


def EditProfile(request):
     
    return render(request, 'profile/editProfile.html')
    