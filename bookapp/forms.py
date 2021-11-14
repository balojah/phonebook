from django import forms
from .models import ContactId


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactId
        fields = ['phone_number', 'name', 'surname', 'company', 'notes']
