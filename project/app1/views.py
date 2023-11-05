
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
from django.http import JsonResponse



def index(request):
    return render(request, "index.html")

def t_index(request):
    return render(request, "t_index.html")



def signin(request):
    if request.user.is_authenticated:
        if request.user.is_customer:
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
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # If the UserProfile doesn't exist, create one for the user
        user_profile = UserProfile.objects.create(user=request.user)
    
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



from .models import Product

from django.shortcuts import render, redirect, get_object_or_404

def add_garment(request):
    if request.user.is_authenticated:
        # Filter products by the currently logged-in user
        products = Product.objects.filter(user=request.user)

        if request.method == "POST":
            category1 = request.POST.get("category")
            description = request.POST.get("description")
            time = request.POST.get("time")
            image = request.FILES.get("image")
            price = request.POST.get("price")

            # Create and save the product with the currently logged-in user
            product = Product(pro_category=category1, description=description, delivery_time=time,image=image, price=price, user=request.user)
            product.save()

            return redirect('add_garment')  # Redirect to the product list page

        return render(request, 'add_garment.html', {'products': products})

    else:
        return redirect('signin')  # Redirect to the sign-in page if the user is not authenticated


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Add this decorator to disable CSRF protection for this view temporarily.
def toggle_product_status(request, product_id):
    if request.method == 'POST':
        # Get the product based on product_id
        product = Product.objects.get(id=product_id)

        # Toggle the product's status
        product.is_active = not product.is_active
        product.save()

        # Return the updated status as JSON response
        return JsonResponse({'status': 'active' if product.is_active else 'inactive'})




from django.http import JsonResponse

def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        category1 = request.POST.get("category")
        description = request.POST.get("description")
        time = request.POST.get("time")
        price = request.POST.get("price")
        new_image = request.FILES.get("new_image")
        print(new_image)

        # Update the product's details
        product.pro_category = category1
        product.description = description
        product.price = price
        product.delivery_time = time


        if new_image:
            if product.image:
                # Delete the old image to save space
                product.image.delete()
            product.image = new_image
        product.save()

        return JsonResponse({'message': 'Product updated successfully'})

    # For GET requests, return product details as JSON
    product_data = {
        'category': product.pro_category,
        'description': product.description,
        'price': product.price,
        'image_url': product.image.url if product.image else None,
    }

    return JsonResponse(product_data)

def productview(request):
    products = Product.objects.all()

    return render(request, "productview.html", {"products": products})

    

from django.shortcuts import render, get_object_or_404
from .models import Product

from django.shortcuts import render, redirect
from .models import Product, Measurement # Import your models
from django.http import HttpResponse

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    request.session['selected_product_id'] = product_id

    return render(request, "product_detail.html", {"product": product})

# views.py


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Measurement, Product
from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.core.exceptions import ValidationError

@login_required
def measurment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    # Check if a measurement record already exists for the user and product
    measurment, created = Measurement.objects.get_or_create(
        user=user,
        product=product,
        defaults={
            'bust':Decimal('0'),
            'waist': Decimal('0'),
            'hips': Decimal('0'),
            'length':Decimal('0'),
            'shoulder_width':Decimal('0'),
            'sleeve_length': Decimal('0'),
            'fabric_type': None,
            'color': None,
            'neck_design': None,
            'back_design': None,
            'sleev_design': None,
            'lining_design': None,
            'work_design': None,
            'additional_info':None,
        }
    )

    if request.method == 'POST':
        # Get data from the POST request
        bust = request.POST.get('bust')
        waist = request.POST.get('waist')
        hips = request.POST.get('hips')
        length = request.POST.get('length')
        shoulder_width = request.POST.get('shoulderWidth')
        sleeve_length = request.POST.get('sleeveLength')
        fabric_type = request.POST.get('fabric_type')
        color = request.POST.get('color')
        neck_design = request.POST.get('neck_design')
        back_design = request.POST.get('back_design')
        sleev_design = request.POST.get('sleev_design')
        lining_design = request.POST.get('lining_design')
        work_design = request.POST.get('work_design')        
        additional_info = request.POST.get('additional_info1')
        # Update the existing measurement record
        measurment.bust = bust
        measurment.waist = waist
        measurment.hips = hips
        measurment.length = length
        measurment.shoulder_width = shoulder_width
        measurment.sleeve_length = sleeve_length
        measurment.fabric_type = fabric_type
        measurment.color = color
        measurment.neck_design = neck_design
        measurment.back_design = back_design
        measurment.sleev_design = sleev_design
        measurment.lining_design = lining_design
        measurment.work_design = work_design        
        measurment.additional_info = additional_info
        measurment.save()

        return redirect('product_detail', product_id=product_id)

    return render(request, 'measurment.html', {'product': product, 'user': user, 'measurment': measurment})



@login_required
def blouse_measurment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    # Check if a measurement record already exists for the user and product
    measurment, created = Measurement.objects.get_or_create(
        user=user,
        product=product,
        defaults={
            'bust':Decimal('0'),
            'waist':Decimal('0'),
           'hips':Decimal('0'),
            'length': Decimal('0'),
            'shoulder_width': Decimal('0'),
            'sleeve_length': Decimal('0'),
            'fabric_type': None,
            'color': '',
            'neck_design': None,
            'back_design': None,
            'sleev_design': None,
            'lining_design': None,
            'work_design': None,
            'additional_info': None,

        }
    )

    if request.method == 'POST':
        # Get data from the POST request
        bust = request.POST.get('bust')
       
        length = request.POST.get('length')
        shoulder_width = request.POST.get('shoulderWidth')
        sleeve_length = request.POST.get('sleeveLength')
        fabric_type = request.POST.get('fabric_type')
        color = request.POST.get('color')
        neck_design = request.POST.get('neck_design')
        back_design = request.POST.get('back_design')
        sleev_design = request.POST.get('sleev_design')
        lining_design = request.POST.get('lining_design')
        work_design = request.POST.get('work_design')        
        additional_info = request.POST.get('additional_info1')

        # Update the existing measurement record
        measurment.bust = bust
        measurment.length = length
        measurment.shoulder_width = shoulder_width
        measurment.sleeve_length = sleeve_length
        measurment.fabric_type = fabric_type
        measurment.color = color
        measurment.neck_design = neck_design
        measurment.back_design = back_design
        measurment.sleev_design = sleev_design
        measurment.lining_design = lining_design
        measurment.work_design = work_design        
        measurment.additional_info = additional_info

        measurment.save()

        return redirect('product_detail', product_id=product_id)

    return render(request, 'blouse_measurment.html', {'product': product, 'user': user, 'measurment': measurment})


def success_page(request):
    return HttpResponse("Measurement data has been saved successfully.")



from django.shortcuts import render
from .models import Product, Measurement
from django.contrib.auth.decorators import login_required

@login_required
def order(request):
    # Get the currently logged-in user (tailor)
    current_user = request.user

    # Fetch the products added by the tailor
    tailored_products = Product.objects.filter(tailor=current_user)

    # Create a dictionary to store product and customer measurement details
    order_details = {}

    for product in tailored_products:
        # Fetch the corresponding measurement details added by customers for each product
        customer_measurements = Measurement.objects.filter(product=product)

        # Fetch the customer details for this product
        customer = product.user  # Assuming user field in Product refers to the customer

        # Create a dictionary to store product and measurement details
        product_details = {
            'product': product,
            'customer': customer,
            'measurements': customer_measurements
        }

        order_details[product] = product_details

    context = {
        'order_details': order_details,
        'tailor_name': current_user.username,
        'tailor_email': current_user.email,
    }

    return render(request, "order.html", context)
