from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from user.models import UserBalance
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','first_name']
        
class UserBalanceForm(forms.ModelForm):
    class Meta:
        model = UserBalance
        fields = ['user','balance']
        