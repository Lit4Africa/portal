from django.contrib import admin
# Register your models here.
from django.contrib.auth.models import User

from application.models import Member, Team, Objective

admin.site.register(Team)
admin.site.register(Objective)
admin.site.register(Member)
