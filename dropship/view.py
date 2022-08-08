from rest_framework import viewsets

from .models import User, Project, Issue
from .serializers import UserSerializers, ProjectSerializers, IssueSerializers


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers
    pagination_class = None

class IssueView(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializers
    pagination_class = None