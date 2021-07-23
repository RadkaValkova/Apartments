from django.urls import path
from Apart.accounts.views import login_user, logout_user, register_user, profile_details, delete_user, edit_profile

urlpatterns = [
    path('login/', login_user, name='log in user'),
    path('logout/', logout_user, name='log out user'),
    path('register/', register_user, name='register user'),
    path('profile/', profile_details, name='profile details'),
    path('delete/', delete_user, name='delete user'),
    path('edit/', edit_profile, name='edit profile')
]