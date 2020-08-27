# from . models import Profile
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.models import User, Group
from django.utils.html import format_html
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SendEmailForm
from django.conf import settings
import requests
# from . models import Profile

admin.site.unregister(Group)
admin.site.unregister(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'status')
    fields = ('username', 'email', 'is_staff', 'date_joined')
    list_filter = ('date_joined', 'is_active')
    actions = ['send_email', ]

    def deactivate_user(self, request, user_id,):
        specific_user = User.objects.get(id = user_id)
        specific_user.is_active = False
        specific_user.save()
        self.message_user(request, "you've successfully deactivated {}".format(specific_user.username), level='warning')
        return redirect('../')
    
    def activate_user(self, request, user_id):
        specific_user = User.objects.get(id=user_id)
        specific_user.is_active = True
        specific_user.save()
        self.message_user(request, "you've successfully activated {}".format(specific_user.username))
        return redirect('../') 

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            re_path(
                r'^deactivate/(?P<user_id>\d+)$',
                self.admin_site.admin_view(self.deactivate_user),
                name='deactivation-button',
            ),
             re_path(
                r'^activate/(?P<user_id>\d+)$',
                self.admin_site.admin_view(self.activate_user),
                name='activation-button',
            ),
        ]
        return custom_urls + urls

    def status(self, obj):
        user = User.objects.get(id=obj.id)
        if user.is_active:
            return format_html(
            '<a class="button" href="{}">Deactivate</a>&nbsp;',
            reverse('admin:deactivation-button', args=[obj.id])
        )
        else:
            return format_html(
            '<a class="button" href="{}">Activate</a>&nbsp;',
            reverse('admin:activation-button', args=[obj.id]),
        )

    def send_email(self, requests, queryset):          
        form = SendEmailForm(initial={'users':queryset})
        return render(requests, 'admin/metrics/intermediate.html', {'form':form})

    send_email.short_description = 'Send Emails to Selected Users'
    