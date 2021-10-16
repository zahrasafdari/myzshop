from django.urls import path

from .views import forget_password, login_user, logout_page, register, logout_request, user_account_main_page, edit_user_profile

app_name = 'zshop_account'
urlpatterns = [
    path('login', login_user),
    path('register', register),
    path('logout/', logout_request, name='logout'),
    path('logout-page/', logout_page, name='logout-page'),
    path('user', user_account_main_page, name='user'),
    path('user/edit', edit_user_profile, name='user/edit'),
    path('forget_password', forget_password, name='forget_password'),



]
