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
   path('download-orders-excel/', views.download_orders_as_excel, name='download_orders_excel'),

   path('messages_page/', views.messages_page, name='messages_page'),
   
   path('r_index/', views.r_index, name='r_index'),
   path('get_products/', views.get_products, name='get_products'),
   # path('single_product/', views.single_product, name='single_product'),
   path('product/<int:product_id>/', views.product_details, name='product_details'),
   path('get_product_details/<int:product_id>/', views.get_product_details, name='get_product_details'),
   path('cart/', views.cart, name='cart'),
   path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
   path('cart_order/', views.cart_order, name='cart_order'),
   path('update_tailor/<int:cart_item_id>/', views.update_tailor, name='update_tailor'),
   path('c_req_tailor/', views.c_req_tailor, name='c_req_tailor'),
   path('accept_order/<int:cart_item_id>/', views.accept_order, name='accept_order'),
   path('reject_order/<int:cart_item_id>/', views.reject_order, name='reject_order'),


   
   

   path('c_add_garment/', views.c_add_garment, name='c_add_garment'),
   path('toggle_product_status/<int:product_id>/', views.toggle_product_status, name='toggle_product_status'),
   path('c_edit_product/<int:product_id>/', views.c_edit_product, name='c_edit_product'),
   path('c_design/<int:cart_id>/', views.c_design, name='c_design'),
   path('paymenthandler2/<int:cart_id>/<str:amount>/', views.paymenthandler2, name='paymenthandler2'),
   path('payment2/<int:cart_id>/<str:price>/', views.payment2, name='payment2'),
   path('c_order_customer/', views.c_order_customer, name='c_order_customer'),
   path('invoice2/<int:cart_id>/', views.invoice2, name='invoice2'),
   path('upload/', views.upload_and_recommend, name='upload_and_recommend'),
   path('prediction_form/', views.predict_size, name='predict_size'),

   
   
   path('toggle_user_status/<int:user_id>/', views.toggle_user_status, name='toggle_user_status'),
   path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
   path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
   path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
   path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
