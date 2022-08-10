from rest_framework import serializers

from .models import *


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['email'], validated_data['email'], validated_data['password'])

        employee = Employee.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password'],
            user=user
        )
        return employee


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class IssueSerializers(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"

class SprintSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = "__all__"

class LabelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = "__all__"
