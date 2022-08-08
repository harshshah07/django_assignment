from rest_framework import serializers

from .models import *


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