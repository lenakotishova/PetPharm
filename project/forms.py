from django import forms
from . import models


class EmailMedicineForm(forms.Form):
    name = forms.CharField(max_length=255)
    to_email = forms.EmailField()
    comment = forms.CharField(required=False,
                              widget=forms.Textarea)


class MedicineForm(forms.ModelForm):
    class Meta:
        model = models.Medicine
        fields = ('title', 'body')
