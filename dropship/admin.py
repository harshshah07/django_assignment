from django.contrib import admin

from .models import Employee, Sprint, User, Project, Issue, Label

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Employee)
admin.site.register(Sprint)
admin.site.register(Label)
