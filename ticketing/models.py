from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class SupportPerson(models.Model):
    username = models.CharField(max_length=150, unique=True, default="")
    first_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30,default="")
    email = models.EmailField(unique=True, default="")
    phone_number = models.IntegerField()
    password = models.CharField(max_length=128, default="")
    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return self.username

class User(AbstractUser):
    phone_no = models.IntegerField(null=True, blank=True, default=None)


class Ticket(models.Model):
    title = models.CharField(max_length=255)
    issue_description = models.TextField()
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    support_person = models.ForeignKey(SupportPerson, on_delete=models.CASCADE, null=True, blank=True)
    solution = models.TextField(null=True, blank=True)
    solution_timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    


    