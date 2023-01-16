from django import forms
from .models import HabitModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class signupForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget = forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget = forms.PasswordInput)
    first_name = forms.CharField(label="Full Name")
    last_name = forms.IntegerField(label="Phone Number")
    class Meta:
        model = User
        fields = ['username', 'first_name','email','last_name']
        help_texts = {
            'username': None
        }
    
# class UserPhoneForm(forms.ModelForm):
#     phone = forms.IntegerField(label='Phone No',widget=forms.TextInput(attrs={"class":"form-control"}))
#     class Meta:
#         model = UserphoneModel
#         fields = ['phone']


#This is for Add Habit Form
class HabitForm(forms.ModelForm):
    class Meta:
        model = HabitModel
        fields = ['user','habit1','habit2','habit3','habit4','habit5']
        widgets = {
            'habit1': forms.TextInput(attrs={'class': 'form-control'}),
            'habit2': forms.TextInput(attrs={'class': 'form-control'}),
            'habit3': forms.TextInput(attrs={'class': 'form-control'}),
            'habit4': forms.TextInput(attrs={'class': 'form-control'}),
            'habit5': forms.TextInput(attrs={'class': 'form-control'}),
        }
