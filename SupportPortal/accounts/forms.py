from django import forms
from django.contrib.auth.forms import AuthenticationForm

class login1(AuthenticationForm):
    username = forms.CharField(max_length=20,
                               widget=forms.TextInput(attrs={'class': 'input100', 'name':'username', 'placeholder': 'username or email'}))
    password = forms.CharField(max_length=15, label= ("input100"),
                               widget=forms.PasswordInput({'class': 'input100', 'placeholder': 'Password'}))


class activity_new(forms.Form):
    activity_name = forms.CharField(max_length='30',
                                widget=forms.TextInput(
                                    attrs={'placeholder': "Activity Name", 'tabindex': "2", "required": "required",
                                           "autofocus": "autofocus"}))
