from django import forms
from django.contrib.auth.models import User

class SendEmailForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    users = forms.ModelMultipleChoiceField(label="To", queryset=User.objects.all(), widget=forms.SelectMultiple())