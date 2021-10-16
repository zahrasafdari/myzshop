from utilities.EmailService import EmailService
from zshop_account.forms import EditUserForm, LoginForm, RegisterForm, SendEmailForm
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.shortcuts import render, redirect

from django.contrib.auth import login, get_user_model, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error(
                'user_name', 'کاربری با این مشخصات وجود ندارد')
    context = {
        'login_form': login_form
    }
    return render(request, 'account/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        User.objects.create_user(
            username=user_name, email=email, password=password)
        return redirect('/login')

    context = {
        'register_form': register_form
    }
    return render(request, 'account/register.html', context)


def forget_password(request):
    sendemail = SendEmailForm(request.POST or None)
    if sendemail.is_valid():
        email = sendemail.cleaned_data.get('email')
        print(email)
        EmailService.send_email('ایمیل تستی',
                                [str(email)],
                                'emails/test_email.html',
                                {
                                    'title': 'این یک پیام تستی میباشد',
                                    'description': 'این ایمیل عشقتون زهراعه'
                                })
    context = {
        'sendemail': sendemail
    }
    return render(request, 'account/forget-password.html', context)


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/logout-page")


def logout_page(request):
    context = {}
    return render(request, 'account/logout.html', context)


@login_required(login_url='/login')
def user_account_main_page(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)

    context = {
        'username': user,

    }
    return render(request, 'account/user_account_main.html', context)


@login_required(login_url='/login')
def edit_user_profile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)

    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')

    edit_user_form = EditUserForm(request.POST or None,
                                  initial={'first_name': user.first_name, 'last_name': user.last_name})

    if edit_user_form.is_valid():
        first_name = edit_user_form.cleaned_data.get('first_name')
        last_name = edit_user_form.cleaned_data.get('last_name')

        user.first_name = first_name
        user.last_name = last_name
        user.save()

    context = {'edit_form': edit_user_form}

    return render(request, 'account/edit_account.html', context)


def user_sidebar(request):
    return render(request, 'account/user_sidebar.html', {})
