from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     gender = models.CharField(max_length=10, blank=True)
#     location = models.CharField(max_length=255, blank=True)
#     dob = models.DateField(null=True, blank=True)

#     @property
#     def full_name(self):
#         return "%s %s"%(self.user.first_name, self.user.last_name)

#     def __str__(self):
#         return self.full_name

#     @property
#     def email(self):
#         return "%s"%(self.user.email)

#     def __str__(self):
#         return self.email

#     @property
#     def date_joined(self):
#         return "%s"%(self.user.date_joined)
    
#     def __str__(self):
#         return self.date_joined

#     @property
#     def is_active(self):
#         return "%s"%(self.user.is_active)
    
#     def __str__(self):
#         return self.is_active
