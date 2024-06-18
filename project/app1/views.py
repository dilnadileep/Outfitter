

from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
import razorpay
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate ,login as auth_login,logout
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.http import JsonResponse
from .models import cart_design
from .models import Cart,Payment2


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
        user_profile.age = request.POST.get("age1")
        user_profile.ad1 = request.POST.get("ad1")
        user_profile.ad2 = request.POST.get("ad2")
        user_profile.pincode = request.POST.get("pincode")

        user_profile.save()
        # Redirect to the profile page after updating
        return redirect("profile")

    return render(request, "profile.html", {"user_profile": user_profile})

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')  # Get the old password from the form
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        user = request.user  # Get the currently logged-in user

        # Check if the entered old password matches the user's current password
        if not user.check_password(old_password):
            return JsonResponse({'error': 'Incorrect old password'}, status=400)

        if new_password == confirm_password:
            # Change the user's password and save it to the database
            user.set_password(new_password)
            user.save()

            # Update the session to keep the user logged in
            update_session_auth_hash(request, user)

            return JsonResponse({'message': 'Password changed successfully'})
        else:
            return JsonResponse({'error': 'Passwords do not match'}, status=400)

    return render(request, 'change_password.html')

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
        time1 = request.POST.get("delivery_time")
        price = request.POST.get("price")
        new_image = request.FILES.get("new_image")
        print(new_image)

        # Update the product's details
        product.pro_category = category1
        product.description = description
        product.price = price
        product.delivery_time = time1


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
        'delivery_time': product.delivery_time,
        'image_url': product.image.url if product.image else None,
    }

    return JsonResponse(product_data)

from django.db.models import Q

def productview(request):
    search_query = request.GET.get('search_query')
    all_products = Product.objects.filter(is_active=True)

    if search_query:
        searched_products = all_products.filter(
            Q(pro_category__icontains=search_query) |
            Q(description__icontains=search_query)
        )
        remaining_products = all_products.exclude(id__in=searched_products.values_list('id', flat=True))
    else:
        searched_products = []
        remaining_products = all_products

    products = list(searched_products) + list(remaining_products)

    return render(request, "productview.html", {"products": products})


from django.shortcuts import render, get_object_or_404
from .models import Product

from django.shortcuts import render, redirect
from .models import Product, Measurement # Import your models
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from .models import Product, Order

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    request.session['selected_product_id'] = product_id

    order = None

    if request.user.is_authenticated and request.user.is_customer:
        order = Order.objects.filter(customer=request.user, product=product).first()

    return render(request, "product_detail.html", {"product": product, "order": order})

# views.py


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Measurement, Product,Order
from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.core.exceptions import ValidationError

@login_required



def measurment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    # Check if a measurement record already exists for the user and product
    measurment, created = Measurement.objects.get_or_create(
        product=product,
        user=user,
        defaults={
            'bust': Decimal('0'),
            'waist': Decimal('0'),
            'hips': Decimal('0'),
            'length': Decimal('0'),
            'shoulder_width': Decimal('0'),
            'sleeve_length': Decimal('0'),
            'fabric_type': None,
            'color': None,
            'style_design': None,
            'neck_design': None,
            'back_design': None,
            'sleev_design': None,
            'lining_design': None,
            'work_design': None,
            'additional_info': None,
            'user': user,
        }
    )

    if request.method == 'POST':
        # Get data from the POST request and update the measurement
        bust = request.POST.get('bust')
        waist = request.POST.get('waist')
        hips = request.POST.get('hips')
        length = request.POST.get('length')
        shoulder_width = request.POST.get('shoulderWidth')
        sleeve_length = request.POST.get('sleeveLength')
        fabric_type = request.POST.get('fabric_type')
        color = request.POST.get('color')
        style_design = request.POST.get('style_design')
        neck_design = request.POST.get('neck_design')
        back_design = request.POST.get('back_design')
        sleev_design = request.POST.get('sleev_design')
        lining_design = request.POST.get('lining_design')
        work_design = request.POST.get('work_design')
        additional_info = request.POST.get('additional_info1')

        measurment.bust = bust
        measurment.waist = waist
        measurment.hips = hips
        measurment.length = length
        measurment.shoulder_width = shoulder_width
        measurment.sleeve_length = sleeve_length
        measurment.fabric_type = fabric_type
        measurment.color = color
        measurment.style_design = style_design
        measurment.neck_design = neck_design
        measurment.back_design = back_design
        measurment.sleev_design = sleev_design
        measurment.lining_design = lining_design
        measurment.work_design = work_design
        measurment.additional_info = additional_info

        measurment.save()

    
        order = Order.objects.create(product=product, customer=user, mesurment=measurment)
        order.save()

        messages.success(request, 'Order created successfully!')
        return redirect('product_detail', product_id=product_id)

    return render(request, 'measurment.html', {'product': product, 'measurment': measurment})



@login_required
def blouse_measurment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    # Check if a measurement record already exists for the user and product
    measurment, created = Measurement.objects.get_or_create(
        product=product,
        user=user,
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
            'user' : user,

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

        order = Order.objects.create(product=product, customer=user, mesurment=measurment)
        order.save()

        messages.success(request, 'Order created successfully!')
        return redirect('product_detail', product_id=product_id)

    return render(request, 'blouse_measurment.html', {'product': product, 'measurment': measurment})

def success_page(request):
    return HttpResponse("Measurement data has been saved successfully.")



from .models import Product, Measurement
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Order
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
@login_required


def order_request(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')  # Get the order_id from the form
        try:
            order = Order.objects.get(pk=order_id)
            order.is_active = True
            order.save()
            
            # Send an email to the customer
            if order.customer.email and order.is_active:
                subject = 'Outfitter : Your Order is Approved '
                message = 'Your order is now approved from tailor. Thank you for your order.You can now make payment to confirm your order from our site..'
                from_email = 'dilnadileep2024a@mca.ajce.in'  # Change to your email
                recipient_list = [order.customer.email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                
            # You can add a success message or other logic here if needed
        except Order.DoesNotExist:
            # Handle the case where the order doesn't exist
            pass
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # Redirect back to the same page

    # Fetch the orders and associated data
    requests = Order.objects.select_related('customer', 'product', 'mesurment').all()
    
    return render(request, "order_request.html", {"requests": requests})


def get_pay_status(order):
    # Get the pay status for the given order
    return order.pay_status
from django.shortcuts import render
from .models import Order, UserProfile,OrderStatus

from django.db.models import Q

def order(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        search_query = request.GET.get('search_query', '')  # Get the search query from the request

        # Fetch the user's orders
        user_orders = Order.objects.filter(customer=request.user)

        tailor_profiles = {}  # Create a dictionary to store tailor profiles

        if search_query:
            # Filter orders based on the search query
            user_orders = user_orders.filter(Q(product__pro_category__icontains=search_query))

        for order in user_orders:
            # Set the pay_status attribute for each order
            order.pay_status = get_pay_status(order)

            product = order.product
            if product:
                tailor = product.user
                # Fetch the tailor's profile
                tailor_profile = UserProfile.objects.filter(user=tailor).first()
                if tailor_profile:
                    tailor_profiles[order.id] = tailor_profile
                    print(f"Tailor Profile for Order {order.id}: {tailor_profile}")

        return render(request, "order.html", {"requests": user_orders, "tailor_profiles": tailor_profiles, "search_query": search_query})
    else:
        # Handle the case where the user is not authenticated
        return render(request, "order.html")


def order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_statuses = OrderStatus.objects.filter(order=order)
    return render(request, "order_status.html", {"order_statuses": order_statuses})


from django.http import JsonResponse

def fetch_measurement_details(request):
    if request.method == "GET":
        request_id = request.GET.get("request_id")
        try:
            order = Order.objects.get(id=request_id)
            measurement = order.mesurment  # Get the measurement associated with the order
            measurement_details = {
                "fabric_type": measurement.fabric_type,
                "color": measurement.color,
                "bust": measurement.bust,
                "waist": measurement.waist,
                "hips": measurement.hips,
                "length": measurement.length,
                "shoulder_width": measurement.shoulder_width,
                "sleeve_length": measurement.sleeve_length,
                "style_design": measurement.style_design,
                "neck_design": measurement.neck_design,
                "back_design": measurement.back_design,
                "sleev_design": measurement.sleev_design,
                "lining_design": measurement.lining_design,
                "work_design": measurement.work_design,
                "additional_info": measurement.additional_info,
            }
            return JsonResponse(measurement_details)
        except Order.DoesNotExist:
            return JsonResponse({"error": "Order not found"}, status=400)




# authorize razorpay client with API Keys.


from datetime import datetime
from decimal import Decimal
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from razorpay.errors import BadRequestError
from .models import Payment
from django.conf import settings


razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def payment1(request, order_id, price):
    currency = 'INR'
    amount_in_rupees = Decimal(price)
    amount_in_paise = int(amount_in_rupees * 100)

    try:
        razorpay_order = razorpay_client.order.create(dict(amount=amount_in_paise, currency=currency, payment_capture='0'))
        razorpay_order_id = razorpay_order['id']
        callback_url = f'http://127.0.0.1:8000/paymenthandler/{order_id}/{price}/'

        context = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_merchant_key': settings.RAZOR_KEY_ID,
            'razorpay_amount': amount_in_paise,
            'currency': currency,
            'callback_url': callback_url,
        }

        return render(request, 'payment1.html', context=context)
    except BadRequestError as e:
        print(f"Error creating Razorpay order: {str(e)}")
        return HttpResponseBadRequest()

# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
from django.shortcuts import get_object_or_404
from .models import Order, Payment

@csrf_exempt
def paymenthandler(request, order_id, amount):
    # only accept POST requests.
    if request.method == "POST":
        try:
            # get the required parameters from the POST request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result is not None:
                # convert the amount to paise (multiply by 100)
                amount_in_paise = int(float(amount) * 100)

                try:
                    # capture the payment with the correct amount in paise
                    razorpay_client.payment.capture(payment_id, amount_in_paise)

                    # create a Payment instance and save it to the database
                    payment = Payment(
                        order_id=order_id,
                        payment_amount=float(amount),
                        payment_datetime=datetime.now(),
                        payee=request.user  # Assuming CustomUser is your User model
                    )
                    payment.save()

                    # Retrieve the corresponding Order and update pay_status
                    order = get_object_or_404(Order, id=order_id)
                    order.pay_status = True
                    order.save()
                    
                    payment.payment_status = 'Successful'
                    payment.save()

                    print("Payment successful. Redirecting to paymentsuccess.html.")
                    return render(request, "paymentsuccess.html")
                except Exception as e:
                    # If there's an error capturing the payment
                    print(f"Error capturing payment: {str(e)}")
                    print("Error capturing payment. Redirecting to paymentfail.html.")
                    return render(request, "paymentfail.html")
            else:
                print("Signature verification failed. Redirecting to paymentfail.html.")
                return render(request, "paymentfail.html")
        except Exception as e:
            # if there's an error processing POST data
            print(f"Error processing POST data: {str(e)}")
            print("Error processing POST data. Returning HttpResponseBadRequest.")
            return HttpResponseBadRequest()
    else:
        # if other than POST request is made.
        return HttpResponseBadRequest()
    
    
    
 
    

from django.shortcuts import render, get_object_or_404
from .models import Order, Payment

def invoice_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    # Use filter instead of get to handle MultipleObjectsReturned
    payments = Payment.objects.filter(order=order)
    payment = payments.first()

    context = {
        'order': order,
        'payment': payment,
    }

    return render(request, 'payment_reciept.html', context)


from django.http import HttpResponse
from django.shortcuts import render
from .models import Payment, Order, OrderStatus

def t_order(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        status = request.POST.get('status')

        # Update order status
        order = Order.objects.get(id=order_id)
        order_status, created = OrderStatus.objects.get_or_create(order=order)
        order_status.status = status
        order_status.save()

        return redirect('t_order')  # Redirect to the same view after updating status

    successful_payments = Payment.objects.filter(payment_status='Successful')
    orders_data = []
    for payment in successful_payments:
        order = payment.order
        product_name = order.product.pro_category if order.product else "N/A"
        customer_name = order.customer.first_name if order.customer else "N/A"
        
        # Fetch OrderStatus and get its status
        try:
            order_status = OrderStatus.objects.get(order=order)
            updated_status = order_status.status
        except OrderStatus.DoesNotExist:
            updated_status = "N/A"  # If OrderStatus doesn't exist, display 'N/A'

        # Collect necessary order details along with updated status
        order_details = {
            'order_id': order.id,
            'customer_name': customer_name,
            'product_name': product_name,
            'payment_amount': payment.payment_amount,
            'payment_datetime': payment.payment_datetime,
            'updated_status': updated_status,  # Include the updated status here
            # Add other details you want to display
        }
        orders_data.append(order_details)

    return render(request, 't_order.html', {'orders_data': orders_data})

import pandas as pd


def download_orders_as_excel(request):
    successful_payments = Payment.objects.filter(payment_status='Successful')
    orders_data = []

    for payment in successful_payments:
        order = payment.order
        if order:
            customer_name = order.customer.first_name if order.customer else "N/A"
            product_name = order.product.pro_category if order.product else "N/A"

            # You can add more fields or related data from the Order model or related models
            # For instance, if OrderStatus is related to the Order model, fetch its status
            order_status = "N/A"
            try:
                order_status_obj = OrderStatus.objects.get(order=order)
                order_status = order_status_obj.status
            except OrderStatus.DoesNotExist:
                pass  # Handle the case when OrderStatus doesn't exist

            # Collect necessary order details along with updated status
            order_details = {
                'Order ID': order.id,
                'Customer Name': customer_name,
                'Product Name': product_name,
                'Payment Amount': payment.payment_amount,
                'Order Status': order_status,
                # Add other details you want to display
            }
            orders_data.append(order_details)

    # Convert orders_data to a Pandas DataFrame
    df = pd.DataFrame(orders_data)

    # Create an Excel writer object using Pandas
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="orders_data.xlsx"'
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

    return response



from app1.models import Thread

@login_required
def messages_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    return render(request, 'messages.html', context)





# celebrity coutre main project 


from .models import c_Product

from django.shortcuts import render, redirect, get_object_or_404

def c_add_garment(request):
    if request.user.is_authenticated:
        # Filter products by the currently logged-in user
        c_products = c_Product.objects.filter(user=request.user)

        if request.method == "POST":
            c_category1 = request.POST.get("category")
            c_category2 = request.POST.get("category2")
            description = request.POST.get("description")
            time = request.POST.get("time")
            image = request.FILES.get("image")
            price = request.POST.get("price")

            # Create and save the product with the currently logged-in user
            c_product = c_Product(c_category=c_category1,t_category=c_category2 , description=description, delivery_time=time,image=image, price=price, user=request.user)
            c_product.save()

            return redirect('c_add_garment')  # Redirect to the product list page

        return render(request, 'c_add_garment.html', {'c_products': c_products})

    else:
        return redirect('signin')  # Redirect to the sign-in page if the user is not authenticated


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Add this decorator to disable CSRF protection for this view temporarily.
def toggle_product_status(request, product_id):
    if request.method == 'POST':
        # Get the product based on product_id
        c_product = c_Product.objects.get(id=product_id)

        # Toggle the product's status
        c_product.is_active = not c_product.is_active
        c_product.save()

        # Return the updated status as JSON response
        return JsonResponse({'status': 'active' if c_product.is_active else 'inactive'})




from django.http import JsonResponse

def c_edit_product(request, product_id):
    c_product = get_object_or_404(c_Product, pk=product_id)

    if request.method == "POST":
        c_category1 = request.POST.get("category")
        c_category2 = request.POST.get("category2")    
        description = request.POST.get("description")
        time1 = request.POST.get("delivery_time")
        price = request.POST.get("price")
        new_image = request.FILES.get("new_image")
        print(new_image)

        # Update the product's details
        c_product.c_category = c_category1
        c_product.t_category = c_category2
        c_product.description = description
        c_product.price = price
        c_product.delivery_time = time1


        if new_image:
            if c_product.image:
                # Delete the old image to save space
                c_product.image.delete()
            c_product.image = new_image
        c_product.save()

        return JsonResponse({'message': 'Product updated successfully'})

    # For GET requests, return product details as JSON
    product_data = {
        'category': c_product.c_category,
        'category2': c_product.t_category,        
        'description': c_product.description,
        'price': c_product.price,
        'delivery_time': c_product.delivery_time,
        'image_url': c_product.image.url if c_product.image else None,
    }

    return JsonResponse(product_data)




def r_index(request):
    lehangas = c_Product.objects.filter(t_category='Lehanga', is_active=True)
    anarkali_suits = c_Product.objects.filter(t_category='Anarkali Suit', is_active=True)
    gowns = c_Product.objects.filter(t_category='Gown', is_active=True)
    
    context = {
        'lehangas': lehangas,
        'anarkali_suits': anarkali_suits,
        'gowns': gowns,
    }
    
    return render(request, 'r_index.html', context)


from django.http import JsonResponse
from .models import c_Product

def get_products(request):
    if request.method == 'GET':
        model_name = request.GET.get('model')
        products = c_Product.objects.filter(c_category=model_name).values('description', 'image', 'price')
        return JsonResponse({'products': list(products)})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)



def product_details(request, product_id):
    product = c_Product.objects.get(id=product_id)
    related_products = c_Product.objects.filter(t_category=product.t_category).exclude(id=product_id)[:6]
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'single_product.html', context)


from django.http import JsonResponse
from .models import c_Product

def get_product_details(request, product_id):
    product = c_Product.objects.get(id=product_id)
    data = {
        'description': product.description,
        'image_url': product.image.url,
        'price': product.price,
    }
    return JsonResponse(data)


from django.shortcuts import render, redirect
from .models import Cart
from django.contrib import messages

def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        size = request.POST.get('size')

        # Assuming you have a function to get the product by ID
        product = c_Product.objects.get(id=product_id)

        # Create a new cart item
        cart_item = Cart(user=request.user, product=product, size=size, quantity=1)
        cart_item.save()

        messages.success(request, 'Product added to cart successfully!')
        return redirect('cart')  # Redirect to the cart page or any other page

from django.shortcuts import render
from .models import Cart, cart_design

def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    for item in cart_items:
        item.total = item.product.price * item.quantity
        # Fetch the corresponding design for the item
        item.design = cart_design.objects.filter(order=item).first()
        # Check if the order is customized and customization amount has not been added
        if item.is_customized and not item.customization_added:
            item.total += 150  # Add 150 rupees for customization
            item.product.price += 150  # Update product price in the database
            item.product.save()  # Save the updated product price
            item.customization_added = True  # Mark customization added
            item.save()  # Save the item with the updated customization flag
    subtotal = sum(item.total for item in cart_items)
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
    }
    return render(request, 'cart.html', context)

from django.shortcuts import render
from .models import Cart, c_Product

def cart_order(request):
    cart_items = Cart.objects.all()
    for item in cart_items:
        item.product_price = c_Product.objects.get(pk=item.product_id).price
        item.product_category = c_Product.objects.get(pk=item.product_id).t_category
        tailors = CustomUser.objects.filter(is_tailor=True)

    context = {
        'cart_items': cart_items,
        'tailors' : tailors,
    }
    return render(request, 'cart_order.html', context)


def update_tailor(request, cart_item_id):
    if request.method == 'POST':
        cart_item = Cart.objects.get(pk=cart_item_id)
        tailor_id = request.POST.get('tailor')
        tailor = CustomUser.objects.get(pk=tailor_id)
        cart_item.tailor = tailor
        cart_item.save()
    return redirect('cart_order')





def c_req_tailor(request):
    tailor_id = request.user.id
    tailor_cart_items = Cart.objects.filter(tailor_id=tailor_id)
    
    # Fetching additional details for each cart item
    for cart_item in tailor_cart_items:
        product = cart_item.product
        cart_item.price = product.price
        cart_item.image = product.image.url  # Assuming 'image' is the field name in c_Product model
        # Fetch the corresponding design for the item
        cart_item.design = cart_design.objects.filter(order=cart_item).first()
        
        
    context = {
        'tailor_cart_items': tailor_cart_items
    }
    return render(request, 'c_req_tailor.html', context)

def accept_order(request, cart_item_id):
    cart_item = Cart.objects.get(id=cart_item_id)
    cart_item.is_active = True
    cart_item.save()
    if cart_item.user.email and cart_item.is_active:        
        subject = 'Outfitter : Your Order is Approved by the tailor side '
        message = 'Your order is now approved from tailor now you can proceed with the order for checkout or you can customize. Thank you for your order.You can now make payment to confirm your order from our site..'
        from_email = 'dilnadileep2024a@mca.ajce.in'  # Change to your email
        recipient_list = [cart_item.user.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
               

    return redirect('c_req_tailor')

def reject_order(request, cart_item_id):
    cart_item = Cart.objects.get(id=cart_item_id)
    cart_item.is_rejected = True
    cart_item.save()
    return redirect('c_req_tailor')



def c_design(request, cart_id):
    cart_item = Cart.objects.get(pk=cart_id)
    if request.method == 'POST':
        cart_item.is_customized = True
        cart_item.save()
        
        neck_design = request.POST.get('selected_neck_design')
        back_design = request.POST.get('selected_back_design')
        sleev_design = request.POST.get('selected_sleev_design')
        lining_design = request.POST.get('selected_lining_design')
        additional_info = request.POST.get('additional_info')
        
        design = cart_design(
            order=cart_item,
            neck_design=neck_design,
            back_design=back_design,
            sleev_design=sleev_design,
            lining_design=lining_design,
            additional_info=additional_info
        )
        design.save()
        return redirect('cart')  # Redirect to the cart page after submitting

    return render(request, 'c_design.html', {'cart_item': cart_item})

def payment2(request, cart_id, price):
    currency = 'INR'
    amount_in_rupees = Decimal(price)
    amount_in_paise = int(amount_in_rupees * 100)

    try:
        # Assuming Cart object has a 'cart' attribute containing the required information
        razorpay_order = razorpay_client.order.create(dict(amount=amount_in_paise, currency=currency, payment_capture='0'))
        razorpay_order_id = razorpay_order['id']
        callback_url = f'http://127.0.0.1:8000/paymenthandler2/{cart_id}/{price}/'

        context = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_merchant_key': settings.RAZOR_KEY_ID,
            'razorpay_amount': amount_in_paise,
            'currency': currency,
            'callback_url': callback_url,
        }


        return render(request, 'payment2.html', context=context)
    except BadRequestError as e:
        print(f"Error creating Razorpay order: {str(e)}")
        return HttpResponseBadRequest()
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def paymenthandler2(request, cart_id, amount):
    # only accept POST requests.
    if request.method == "POST":
        try:
            # get the required parameters from the POST request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result is not None:
                # convert the amount to paise (multiply by 100)
                amount_in_paise = int(float(amount) * 100)

                try:
                    # capture the payment with the correct amount in paise
                    razorpay_client.payment.capture(payment_id, amount_in_paise)

                    # create a Payment instance and save it to the database
                    payment = Payment2(
                        order_id=cart_id,
                        payment_amount=float(amount),
                        payment_datetime=datetime.now(),
                        payee=request.user  # Assuming CustomUser is your User model
                    )
                    payment.save()

                    # Retrieve the corresponding Order and update pay_status
                    order = get_object_or_404(Cart, id=cart_id)
                    order.pay_status = True
                    order.save()
                    
                    payment.payment_status = 'Successful'
                    payment.save()

                    logger.info("Payment successful. Redirecting to paymentsuccess2.html.")
                    return render(request, "paymentsuccess2.html")
                except Exception as e:
                    # If there's an error capturing the payment
                    logger.error(f"Error capturing payment: {str(e)}")
                    logger.error("Error capturing payment. Redirecting to paymentfail.html.")
                    return render(request, "paymentfail.html")
            else:
                logger.error("Signature verification failed. Redirecting to paymentfail.html.")
                return render(request, "paymentfail.html")
        except Exception as e:
            # if there's an error processing POST data
            logger.error(f"Error processing POST data: {str(e)}")
            logger.error("Error processing POST data. Returning HttpResponseBadRequest.")
            return HttpResponseBadRequest()
    else:
        # if other than POST request is made.
        return HttpResponseBadRequest()


def c_order_customer(request):
    cart_items = Cart.objects.filter(user=request.user, pay_status=True)

    context = {
        'cart_items': cart_items
    }
    return render(request, 'c_order_customer.html', context)


def invoice2(request, cart_id):
    order = get_object_or_404(Cart, id=cart_id)
    # Use filter instead of get to handle MultipleObjectsReturned
    payments = Payment2.objects.filter(order=order)
    user_orders = Cart.objects.filter(user=request.user)

    payment = payments.first()

    context = {
        'order': order,
        'payment': payment,
        'user_orders':user_orders,
    }

    return render(request, 'payment_reciept2.html', context)

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import c_Product  # Ensure you import your c_Product model
from .feature_extraction import extract_features
from tensorflow.keras.models import load_model

def upload_and_recommend(request):
    if request.method == 'POST' and request.FILES['image']:
        # Save the uploaded image
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_image_url = fs.url(filename)

        # Load the trained model
        model_path = 'C:/Users/dilna/OneDrive/Desktop/seminar/dataset/model.h5'
        model = load_model(model_path)

        # Extract features and predict the category
        _, predicted_category_index = extract_features(uploaded_image_url, model)
        categories = ['Anarkali Suit', 'Gown', 'Lehanga','Not_found', 'No_outfit_detected']
        predicted_category = categories[predicted_category_index]

        # Fetch similar products from the database
        similar_products = c_Product.objects.filter(t_category__iexact=predicted_category)

        # Render the template with the prediction result and similar products
        return render(request, 'similar_products.html', {
            'uploaded_image_url': uploaded_image_url,
            'predicted_category': predicted_category,
            'similar_products': similar_products
        })


# views.py

from django.shortcuts import render
from .size_prediction import train_size_prediction_model
from sklearn.preprocessing import LabelEncoder

def predict_size(request):
    predicted_size = None
    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        age = float(request.POST.get('age'))
        height = float(request.POST.get('height'))

        model = train_size_prediction_model('C:/Users/dilna/OneDrive/Desktop/Outfitter/final_test.csv')
        prediction = model.predict([[weight, age, height]])

        label_encoder = LabelEncoder()
        label_encoder.fit(['S','XS', 'XXS', 'M', 'L', 'XL', 'XXL', 'XXXL',])  # Assuming 'S', 'M', 'L' are your original categorical sizes
        predicted_size = label_encoder.inverse_transform([round(prediction[0])])[0]

    return render(request, 'prediction_form.html', {'predicted_size': predicted_size})
