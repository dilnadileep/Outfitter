from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings




urlpatterns = [
   path('', views.index, name="index"),
   path('signup/', views.signup, name="signup"),
   path('signin/',views.signin, name="signin"),
   path('t_signup/', views.t_signup, name="t_signup"),
   path('t_index/', views.t_index, name="t_index"),
   path('loggout/', auth_views.LogoutView.as_view(), name="loggout"),
   path('t_index/', views.t_index, name="t_index"),  # Add this URL pattern for the 'index' view
   path('admindashboard/', views.admindashboard, name="admindashboard"),  # Add this URL pattern for the 'admindashboard' view
   path('profile/', views.profile, name='profile'),
   path('add_garment/', views.add_garment, name='add_garment'),
   path('toggle_product_status/<int:product_id>/', views.toggle_product_status, name='toggle_product_status'),
   path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
   path('productview/', views.productview, name='productview'),
   path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
   path('measurment/<int:product_id>/', views.measurment, name='measurment'),
   path('blouse_measurment/<int:product_id>/', views.blouse_measurment, name='blouse_measurment'),
   path('order_request/', views.order_request, name='order_request'),
   path('change_password/', views.change_password, name='change_password'),
   path('order/', views.order, name='order'),
   path('order_status/<int:order_id>/', views.order_status, name='order_status'),

   path('fetch_measurement_details/', views.fetch_measurement_details, name='fetch_measurement_details'),
   
   path('paymenthandler/<int:order_id>/<str:amount>/', views.paymenthandler, name='paymenthandler'),
   path('payment1/<int:order_id>/<str:price>/', views.payment1, name='payment1'),
   path('invoice/<int:order_id>/', views.invoice_view, name='invoice'),

   path('t_order/', views.t_order, name='t_order'),

   
   
   
   path('toggle_user_status/<int:user_id>/', views.toggle_user_status, name='toggle_user_status'),
   path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
   path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
   path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
   path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
