from rest_framework import viewsets

from .models import Employee, Project, Issue
from .serializers import EmployeeSerializer, ProjectSerializers, IssueSerializers

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class CustomAuthToken(ObtainAuthToken):

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        try:
            employee_obj = Employee.objects.get(user=user.pk)
            token, created = Token.objects.get_or_create(user=user)
        except:
            print("User Doesn't Exist")
        return Response({
            'token': token.key,
            'user_id': employee_obj.pk,
            'employee_id': employee_obj.id,
            'email': employee_obj.email,
            'name': employee_obj.name,
        })


class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers
    pagination_class = None
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class IssueView(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializers
    pagination_class = None
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
