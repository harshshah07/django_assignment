from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .view import EmployeeView, ProjectView, IssueView, CustomAuthToken, SprintView,getIssuesByProject

router = DefaultRouter()
router.register('employee', EmployeeView, basename='employee/')
router.register('project', ProjectView, basename='project/')
router.register('issue', IssueView, basename='issue/')
router.register('sprint', SprintView, basename='sprint/')

urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', CustomAuthToken.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("issuebyproject/<int:projectId>",getIssuesByProject)
]
