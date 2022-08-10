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
        return "{0} {1}".format(self.title, self.code)


class Sprint(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    startDate = models.DateField()
    endDate = models.DateField()

    START = "START"
    STOP = "STOP"
    TYPES = [(START, START), (STOP, STOP)]
    type = models.CharField(max_length=8, choices=TYPES, null=True)

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="sprints")

    def __str__(self):
        return "{0}-{1} ".format(self.title, self.description)


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
    sprint = models.ForeignKey(
        Sprint, on_delete=models.CASCADE, related_name="issues")
    Open = "Open"
    InProgress = "InProgress"
    InReview = "InReview"
    CodeComplete = "CodeComplete"
    QATesting = "QA Testing"
    Done = "Done"

    STATUS = [(Open, Open), (InProgress, InProgress), (InReview, InReview),
              (CodeComplete, CodeComplete), (QATesting, QATesting), (Done, Done)]
    status = models.CharField(
        max_length=20, choices=STATUS, default=Open, null=False)

    def __str__(self):
        return "{0}-{1}".format(self.title, self.project.code)


class Label(models.Model):
    title = models.CharField(max_length=32)
    issues = models.ManyToManyField(Issue, null=True, related_name="labels")


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    issue = models.ForeignKey(
        Issue, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return "{0}-{1} ".format(self.pk, self.issue)


class TimeLog(models.Model):
    date = models.DateField()
    timeSpent = models.CharField(max_length=10)
    issue = models.ForeignKey(
        Issue, on_delete=models.CASCADE, related_name="timelog")
    user = models.ManyToManyField(User, related_name="timelog")

    def __str__(self):
        return "{0}".format(self.time_spent)


class watcher(models.Model):
    issue = models.OneToOneField(
        Issue, on_delete=models.CASCADE, null=True, related_name="watcher")
    watchers = models.ManyToManyField(
        User, null=True, related_name="issuedWatched")
