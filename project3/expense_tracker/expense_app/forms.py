from django import forms
from .models import Account, UserSetup


class RegistrationForm (forms.ModelForm):
    class Meta:
        model= UserSetup
        fields = '__all__'
        widgets ={
            'email': forms.EmailInput(),
            'password': forms.PasswordInput(),
        }


class AccountForm (forms.ModelForm):
    class Meta:
        model = Account
        fields = {
            'username',
            'firstName',
            'lastName'}