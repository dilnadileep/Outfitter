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
   #path('admindashboard/', views.admindashboard, name="admindashboard"),  # Add this URL pattern for the 'admindashboard' view
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
