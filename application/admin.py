from django.contrib import admin
# Register your models here.
from django.contrib.auth.models import User

from application.models import Member

admin.site.register(Member)
