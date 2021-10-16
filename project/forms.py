from django import forms
from . import models

from django.contrib.auth.models import User


class EmailMedicineForm(forms.Form):
    name = forms.CharField(max_length=255)
    to_email = forms.EmailField()
    comment = forms.CharField(required=False,
                              widget=forms.Textarea)


class MedicineForm(forms.ModelForm):
    class Meta:
        model = models.Medicine
        fields = ('title', 'body')


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Pass', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Pass2', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('bad password')
        return cd['password']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('birth', 'photo')
