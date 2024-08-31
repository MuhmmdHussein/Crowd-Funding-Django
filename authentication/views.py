from datetime import timezone
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist


from authentication.forms import LoginForm, SignupForm
from authentication.models import Register
# Create your views here.


def auth_login(request):
    if 'user_id' not in request.session :
        msg = None
        if request.method == "POST":
            form = LoginForm( request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                encryptpassword=make_password(password)
                try:
                    user = Register.objects.get(email=email , password=encryptpassword)
                except (ObjectDoesNotExist):
                    user = None
                if user is not None:
                    if  user.is_active:
                        login(request, user)
                        user.last_login = timezone.now()
                        user.is_login= True
                        user.save()
                        request.session['user_id'] = user.id
                        msg = f"You are now logged in as {user.first_name}"
                        return redirect("/" )
                    else:
                        msg= "please check your email to activate it!"
                else:
                    msg = "user doesn't exist "
            else:
                msg = 'Invalid email or password.'
        form = LoginForm()
        return render(request=request, template_name="auth/login.html", context={"login_form":form , "msg": msg})
    else:
        return redirect("/" )


def auth_signup(request):
    form = SignupForm()
    return render(request, 'auth/signup.html', {'signup_form': form})