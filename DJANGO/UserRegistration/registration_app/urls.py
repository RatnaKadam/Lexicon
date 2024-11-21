from django.urls import path  
from registration_app import views

# App namespace
app_name = 'registration_app'

urlpatterns = [
    path('register/', views.register, name='register'),  # Define the 'register' path
    path('login/', views.user_login, name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('special/',views.special,name='special'),
]
