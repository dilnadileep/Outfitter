
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate ,login as auth_login,logout
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile



def index(request):
    return render(request, "index.html")

def t_index(request):
    return render(request, "t_index.html")



def signin(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        if request.user.is_customer:
            # Redirect to the migrant dashboard or your desired URL for migrants
            return redirect("index")  # Replace with your URL name
        elif request.user.is_tailor:
            # Redirect to the institute dashboard or your desired URL for institutes
            return redirect("t_index")  # Replace with your URL name
        elif request.user.is_superuser:
        #     # Redirect to the landlord dashboard or your desired URL for landlords
             return redirect('admindashboard')  # Replace with your URL name
        else:
            # Redirect to a generic home page or your desired URL
            return redirect("index")  # Replace with your URL name

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if email and password:
            user = authenticate(request, username=email, password=password)

            if user is not None:
                auth_login(request, user)
                if user.is_customer:
                    # Redirect to the migrant dashboard or your desired URL for migrants
                    return redirect("index")  # Replace with your URL name
                elif user.is_tailor:
                    # Redirect to the institute dashboard or your desired URL for institutes
                    return redirect("t_index")  # Replace with your URL name
                elif user.is_superuser:
                #     # Redirect to the landlord dashboard or your desired URL for landlords
                     return redirect('admindashboard')  # Replace with your URL name
                else:
                    # Redirect to a generic home page or your desired URL
                    return redirect("index")  # Replace with your URL name
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
    return redirect("index")  # Redirect to the home page after logout

def t_signup(request):
    if request.method == "POST":
        tusername = request.POST.get("temail")
        tfname =request.POST.get("tfname")
        tlname =request.POST.get("tlname")
        temail = request.POST.get("temail")
        tpassword = request.POST.get("tpassword")

        if (
            CustomUser.objects.filter(email=temail).exists()
        ):
            messages.error(request, "Email Already Registered")
            return render(request, "t_signup.html")
        else:
            user = CustomUser.objects.create_user(
                username=tusername,
                first_name=tfname,
                last_name=tlname,
                email=temail,
                password=tpassword,
                is_tailor=True,
            )
            UserProfile.objects.create(user=user)

            user.save()

            return redirect("signin")
    else:
        return render(request, "t_signup.html")


def signup(request):
    
    if request.method == "POST":
        username = request.POST.get('email')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        password = request.POST.get('password')
        
        if (
            CustomUser.objects.filter(email=email).exists()
        ):
            messages.error(request, "Email or Username Already Exists")
            return render(request, "signup.html")
        else:
            user = CustomUser.objects.create_user(
                username=username,
                first_name=fname,
                last_name=lname,
                email=email,
                password=password,
                is_customer=True,
            )
            UserProfile.objects.create(user=user)

            user.save()

            return redirect('signin')
    else:
        return render(request, "signup.html")


    # Fetch data for the admin dashboard here (e.g., user information, orders, statistics)
    # You can use Django's ORM to query the database for this data
    # Example:
             

  


from django.shortcuts import render, get_object_or_404
from .models import CustomUser  # Import your CustomUser model



from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

# Password Reset Views
class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'



from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import CustomUser


def admindashboard(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            tailors = CustomUser.objects.filter(is_tailor=True)
            customers = CustomUser.objects.filter(is_customer=True)
    
    
            context = {
                # Pass the fetched data to the template context
            'tailors': tailors,
            'customers':customers,
                
            }
            return render(request, "admindashboard.html",context) 
    else:
        return render(request, "index.html")
            
    

from django.http import JsonResponse
from .models import CustomUser

def toggle_user_status(request, user_id):
    try:
        user = CustomUser.objects.get(pk=user_id)
        user.is_active = not user.is_active  # Toggle the status
        user.save()
        new_status = 'active' if user.is_active else 'inactive'
        return JsonResponse({'status': new_status})
    except CustomUser.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)




from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser, UserProfile

@login_required
def profile(request):
    # Fetch the user's profile
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == "POST":
       
        # Update the user's profile with the submitted data
        user_profile.phone_number = request.POST.get("num")
        user_profile.state = request.POST.get("state")
        user_profile.district = request.POST.get("district")
        user_profile.gender = request.POST.get("gender")
        user_profile.age = request.POST.get("age")
        user_profile.save()
        # Redirect to the profile page after updating
        return redirect("profile")

    return render(request, "profile.html", {"user_profile": user_profile})





# def add_garment(request):
#     return render(request, "add_garment.html")


from django.shortcuts import render, redirect, get_object_or_404

from .models import Product

def add_garment(request):
    products = Product.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        category1 = request.POST.get("category")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        price = request.POST.get("price")
        
        # Get the currently logged-in user
        user = request.user

        # Create and save the product
        product = Product(name=name,pro_category=category1,description=description,image=image,price=price,user=user)
        product.save()

        return redirect('add_garment')  # Redirect to a success page or any other page you prefer

    return render(request, 'add_garment.html', {'products': products})



# def edit_product(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     # Handle editing the product here
#     # You can use a similar form as in your add_garment view
#     # Update the product instance and save it
    
#     return redirect('add_garment')  # Redirect back to the product list page

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Handle deleting the product here
    # Delete the product instance
    
    return redirect('add_garment')  


from django.http import JsonResponse
from app1.models import Product  # Import the model here



def get_product_details(request, product_id):
    try:
        product = Product.objects.get(id=product_id)  # Replace with your actual model
        data = {
            'name': product.name,
            'category': product.category,
            'description': product.description,
            'price': product.price,
            'image': product.image,
            # Add more fields if needed
        }
        return JsonResponse(data)
    except Product.DoesNotExist:  # Handle the case where the product does not exist
        return JsonResponse({'error': 'Product not found'}, status=404)
