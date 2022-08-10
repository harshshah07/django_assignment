from django.contrib import admin

from .models import Employee, Sprint, User, Project, Issue, Label, Comment, TimeLog

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Employee)
admin.site.register(Sprint)
admin.site.register(Label)
admin.site.register(Comment)
admin.site.register(TimeLog)
