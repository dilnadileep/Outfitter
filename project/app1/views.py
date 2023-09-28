
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate ,login as auth_login,logout
from django.urls import reverse

# Create your views here.
def index(request):
     return render(request, "index.html")
 
def t_index(request):
    
    return render(request, "t_index.html")


def t_signup(request):
    if request.method == "POST":
        username = request.POST.get("email")
        fname =request.POST.get("fname")
        lname =request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")

        if (
            CustomUser.objects.filter(username=username).exists()
            or CustomUser.objects.filter(email=email).exists()
        ):
            messages.error(request, "Email Already Registered")
            return render(request, "signin.html")
        else:
            user = CustomUser.objects.create_user(
                 username=username,
                first_name=fname,
                last_name=lname,
                email=email,
                password=password,
                is_tailor=True,
            )
            user.save()

            return redirect("signin")
    else:
        return render(request, "t_signup.html")


def signin(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        if request.user.is_customer:
            # Redirect to the migrant dashboard or your desired URL for migrants
            return redirect('index')  # Replace with your URL name
        elif request.user.is_tailor:
            # Redirect to the institute dashboard or your desired URL for institutes
            return redirect('t_index')  # Replace with your URL name
        # elif request.user.is_landlord:
        #     # Redirect to the landlord dashboard or your desired URL for landlords
        #     return redirect('landlord_dashboard')  # Replace with your URL name
        else:
            # Redirect to a generic home page or your desired URL
            return redirect('index')  # Replace with your URL name

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if email and password:
            user = authenticate(request, email=email, password=password)

            if user is not None:
                auth_login(request, user)
                if user.is_customer:
                    # Redirect to the migrant dashboard or your desired URL for migrants
                    return redirect('index')  # Replace with your URL name
                elif user.is_tailor:
                    # Redirect to the institute dashboard or your desired URL for institutes
                    return redirect('t_index')  # Replace with your URL name
                # elif user.is_landlord:
                #     # Redirect to the landlord dashboard or your desired URL for landlords
                #     return redirect('landlord_dashboard')  # Replace with your URL name
                else:
                    # Redirect to a generic home page or your desired URL
                    return redirect('index')  # Replace with your URL name
            else:
                error_message = "Invalid login credentials."
                return render(request, "signin.html", {"error_message": error_message})
        else:
            error_message = "Please fill out all fields."
            return render(request, "signin.html", {"error_message": error_message})

    return render(request, "signin.html")


from django.contrib.auth import logout

def loggout(request):
    logout(request)
    return redirect('index')  # Redirect to the home page after logout
def signup(request):
 
    
    if request.method == "POST":
        username = request.POST.get("email")
        email = request.POST.get("email")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        print(fname)
        if (
            CustomUser.objects.filter(username=username).exists()
            or CustomUser.objects.filter(email=email).exists()
        ):
            messages.error(request, "Email or Username Already Exists")
            return render(request, "signin.html")
        else:
            user = CustomUser.objects.create_user(
                username=username,
                first_name=fname,
                last_name=lname,
                email=email,
                password=password,
                is_customer=True,
            )
            user.save()
            return redirect('signin')
    else:
        return render(request, "signup.html")

        
    
    
    
       # if request.method == 'POST':
    #     fname = request.POST.get('fname')
    #     lname = request.POST.get('lname')
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     confirm_password=request.POST.get('confirm_password')

    #     #role = request.POST.get('role', 1)
    #     if CustomUser.objects.filter(email=email).exists():
    #         messages.error(request,"email already exits")
    #     elif password!=confirm_password:
    #         messages.error(request,"password not match")
    #     elif fname and  lname and  email and password:
    #         # if CustomUser.objects.filter(email=email).exists():
    #         #     messages.error(request, "Email already exists")
    #         #     return redirect('seller_register')
            
    #         user = CustomUser( first_name=fname,last_name=lname,email=email)
    #         user.set_password(password)
    #         user.is_customer= True
    #         # if role == 'seller':
    #         #     user.is_seller = True
    #         user.save()
    #         messages.success(request, "Registered as a seller successfully")
    #         return redirect('/signin')