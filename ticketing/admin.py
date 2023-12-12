from django.contrib import admin
from .models import SupportPerson, User, Ticket

admin.site.register(SupportPerson)
admin.site.register(User)
admin.site.register(Ticket)
