from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django import forms

from blog_app.models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileSettingsForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(max_length=100,
                                       widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'confirm_password')

    def clean(self):
        cleaned_data = super(EditProfileSettingsForm, self).clean()
        confirm_password = cleaned_data.get('confirm_password')
        if not check_password(confirm_password, self.instance.password):
            self.add_error('confirm_password', 'Password does not match.')


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, label='New Password',
                                    widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', }))
    new_password2 = forms.CharField(max_length=100, label='Confirm New Password',
                                    widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', }))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class EditUserPageForm(forms.ModelForm):
    bio = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    profile_pic = forms.ImageField(widget=forms.FileInput())
    website_url = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telegram_url = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    github_url = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'telegram_url', 'github_url',)
