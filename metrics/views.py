from django.shortcuts import render
from .forms import SendEmailForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from user_metrics import settings
from django.contrib import messages
# Create your views here.

class SendUserEmails(FormView):
    template_name = 'admin/metrics/intermediate.html'
    form_class = SendEmailForm

    def form_valid(self, form):
        users = form.cleaned_data['users']
        print(users)
        subject = form.cleaned_data['subject']
        print(subject)
        message = form.cleaned_data['message']
        print(message)
        recipient = []
        for items in users:
            recipient.append(items.email)
            print(items.email)
        print(recipient)
        send_mail(subject, message, "phemmylintry@gmail.com" , recipient, fail_silently=True)
        user_message = '{0} users emailed successfully!'.format(form.cleaned_data['users'].count())
        messages.success(self.request, user_message)
        return super(SendUserEmails, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('metrics:email')