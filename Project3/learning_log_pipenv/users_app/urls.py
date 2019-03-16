""" Defines URL patterns for users_app """

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views 

app_name = 'users_app'
urlpatterns = [
    # Login page
    path('login/', LoginView.as_view(template_name='users_app/login.html'), name='login'),

    # Logout page
    path('logout/', LogoutView.as_view(template_name='users_app/logout.html'), name='logout'),
]