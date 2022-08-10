from django.contrib import admin

from .models import Employee, User, Project, Issue

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Employee)