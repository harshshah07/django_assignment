from operator import mod
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    def __str__(self):
        return self.username


class Employee(models.Model):
    name = models.CharField(max_length=32, null=False)
    email = models.EmailField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False, validators=[
                                MinLengthValidator(8)])
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name


class Project(TimestampModel):
    title = models.CharField(max_length=128)
    description = models.TextField()
    code = models.CharField(max_length=64, unique=True, null=False)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="projectCreated")

    def __str__(self):
        return "{0} {1}".format(self.code, self.title)


class Issue(TimestampModel):
    BUG = "BUG"
    TASK = "TASK"
    STORY = "STORY"
    EPIC = "EPIC"
    TYPES = [(BUG, BUG), (TASK, TASK), (STORY, STORY), (EPIC, EPIC)]

    title = models.CharField(max_length=128)
    description = models.TextField()

    type = models.CharField(max_length=8, choices=TYPES,
                            default=BUG, null=False)

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="issues")
    reporter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="issuesReported")
    assignee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="issuesAssigned", null=True)
    '''
    status=
    labels=
    watchers(users)=
    worklog (logs)=
    '''

    def __str__(self):
        return "{0}-{1}".format(self.project.code, self.title)
