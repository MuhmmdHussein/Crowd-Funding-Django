from datetime import timezone, datetime
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ObjectDoesNotExist


from authentication.forms import LoginForm, SignupForm
from authentication.models import Register

# Create your views here.


def auth_login(request):
    if "user_id" not in request.session:
        msg = None
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                try:
                    user = Register.objects.get(email=email)
                except ObjectDoesNotExist:
                    user = None
                if user is not None and check_password(password, user.password):
                    if user.is_active:
                        user.last_login = datetime.now()
                        user.is_login = True
                        user.save()
                        request.session["user_id"] = user.id
                        msg = f"You are now logged in as {user.first_name}"
                        return redirect("/")
                    else:
                        msg = "please check your email to activate it!"
                else:
                    msg = "user doesn't exist "
            else:
                if form.errors:
                    msg = ""
                    for key, value in form.errors.items():
                        msg += str(value) + "\n"

                    html_tags = ["<li>", "</li>", "<ul>", "</ul>"]
                    for tag in html_tags:
                        msg = msg.replace(tag, "")
                else:
                    msg = "Invalid email or password."

        form = LoginForm()
        return render(
            request=request,
            template_name="auth/login.html",
            context={"login_form": form, "msg": msg},
        )
    else:
        return redirect("/")


def auth_signup(request):
    msg = None
    if "user_id" not in request.session:
        if request.method == "POST":
            form = SignupForm(request.POST, files=request.FILES)
            print("Form: " + str(form))
            print("Form is valid: " + str(form.is_valid()))
            print("Form Cleaned Data: " + str(form.cleaned_data))
            print("Form Errors: " + str(form.errors))
            if form.is_valid():
                hashedpassword = make_password(form.cleaned_data["password"])
                check = check_password(form.cleaned_data["password"], hashedpassword)
                print(check)
                first_name = form.cleaned_data["first_name"]
                last_name = form.cleaned_data["last_name"]
                email = form.cleaned_data["email"]
                password = hashedpassword
                phone = form.cleaned_data["phone"]
                image = form.cleaned_data["profile_img"]

                print(first_name, last_name, email, password, phone, image)

                user = Register.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                    phone=phone,
                    profile_img=image,
                )
                user.is_active = False
                user.save()

                msg = "Please confirm your email address to complete the registration"
                redirect("/auth/login")
            else:
                if form.errors:
                    msg = ""
                    for key, value in form.errors.items():
                        msg += str(value) + "\n"

                    html_tags = ["<li>", "</li>", "<ul>", "</ul>"]
                    for tag in html_tags:
                        msg = msg.replace(tag, "")
                # msg = "Invalid Data"
        else:
            form = SignupForm()
        return render(request, "auth/signup.html", {"signup_form": form, "msg": msg})

    else:
        return redirect("/")
