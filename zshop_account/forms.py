from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core import validators
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class EditUserForm(forms.Form):
    first_name=forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control",'placeholder':'لطفا نام خود را وارد نمایید','size':40}),
        label='نام'
    )
    last_name=forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control",'placeholder':'لطفا نام خانوادگی خود را وارد نمایید'}),
        label='نام خانوادگی'
    )


class SendEmailForm(forms.Form):
        email=forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':'لطفا ایمیل خود را وارد نمایید'}),
        label='ایمیل',
        validators=[
            validators.EmailValidator(message='ایمیل وارد شده معتبر نمی باشد')
        ]
    )
class LoginForm(forms.Form):

    user_name=forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا نام کاربری خود را وارد نمایید'}),
        label='نام کاربری'
    )

    password=forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'کلمه عبور خود را وارد نمایید'}),
        label='کلمه عبور'
    )

    def clean_user_name(self):
        user_name=self.cleaned_data.get('user_name')
        is_exists_user=User.objects.filter(username=user_name).exists()
        if not is_exists_user:
            raise ValidationError('کاربری با این مشخصات ثبت نام نکرده است')
        return user_name

class RegisterForm(forms.Form):

    user_name=forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا نام کاربری خود را وارد نمایید'}),
        label='نام کاربری',
        validators=[
        validators.MaxLengthValidator(limit_value=20 , message='تعداد کارکتر های وارد شده نمیتواند بیشتر از 20 باشد'),
        validators.MinLengthValidator(limit_value=8 , message='تعداد کارکتر های وارد شده نمیتواند کمتر از 8 باشد')
        ]
    )

    email=forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':'لطفا ایمیل خود را وارد نمایید'}),
        label='ایمیل',
        validators=[
            validators.EmailValidator(message='ایمیل وارد شده معتبر نمی باشد')
        ]
    )

    password=forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'کلمه عبور خود را وارد نمایید'}),
        label='کلمه عبور'
    )
    
    re_password=forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'کلمه عبور خود را مجددا وارد نمایید'}),
        label='تکرار کلمه عبور'
    )

    def clean_user_name(self):
        user_name=self.cleaned_data.get('user_name')
        is_exists_user_by_username=User.objects.filter(username=user_name).exists()

        if is_exists_user_by_username:
            raise ValidationError('این کاربر قبلا ثبت نام کرده است')
        return user_name

    def clean_email(self):
        email=self.cleaned_data.get('email')
        is_exists_user_by_email=User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise ValidationError('ایمیل وارد شده تکراری می باشد')
        if len(email)>200:
            raise ValidationError('تعداد کارکتر های ایمیل باید کمتر از 20 باشد')
        return email

    def clean_re_password(self):
        password=self.cleaned_data.get('password')
        re_password=self.cleaned_data.get('re_password')
        print(password)
        print(re_password)
        if password != re_password:
            raise ValidationError('کلمه های عبور مغایرت دارند')
        return password


