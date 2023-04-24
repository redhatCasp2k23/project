from django import forms
from .models import User,UserExtra

class UserForm(forms.ModelForm):
    """Form definition for User."""

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ('first_name','last_name','email','phone','username','password')

class UserExtraForm(forms.ModelForm):
    """Form definition for UserExtra."""

    class Meta:
        """Meta definition for UserExtraform."""

        model = UserExtra
        exclude = ['user']
class Userwp(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','phone','username']
        

