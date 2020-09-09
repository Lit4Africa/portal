from django.contrib import admin

from application.models import Member, Team, Objective

# Register your models here.

admin.site.register(Team)
admin.site.register(Objective)
admin.site.register(Member)
