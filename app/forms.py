from django import forms
from django.contrib.auth.forms import UserCreationForm



from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    error_messages = {
        'password_mismatch': ('گذرواژه و تکرار گذرواژه یکسان نیست')
    }
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','first_name','last_name')
        labels={
            'username' : ('نام کاربری'),
            'email' : ('ایمیل'),
            'password1' : ('رمز عبور'),
            'password2' : ('تکرار رمز عبور'),
            'first_name' : ('نام'),
            'last_name' : ('نام خانوادگی')
        }
        error_messages = {
            'username':{
                'max-length' : ('نام شما طولانی است'),
                'required' : ('نام خود را وارد کنید '),
                'unique' : ('کاربری نام کاربری زیر وجود دارد'),
            },
            'email':{
                'unique':('کاربری با ایمیل زیر وجود دارد')
            },
        }