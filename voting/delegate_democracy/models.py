from django.db import models
from django.contrib.auth.models import User

CHAR_LENGTH = 200
CHAR_LENGTH_LONG = 2000


class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    proxy = models.BooleanField(default=False)


class IssueCategory(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    name = models.CharField(max_length=CHAR_LENGTH)


class Proxy(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE, related_name='proxy_child')
    proxy = models.ForeignKey(Voter, on_delete=models.CASCADE, related_name='proxy_parent')
    issue_catergory = models.ForeignKey(IssueCategory, on_delete=models.CASCADE)


class IssueType(models.Model):
    name = models.CharField(max_length=CHAR_LENGTH)
    description = models.CharField(max_length=CHAR_LENGTH)


class Issue(models.Model):
    title = models.CharField(max_length=CHAR_LENGTH)
    description = models.CharField(max_length=CHAR_LENGTH_LONG)
    category = models.ForeignKey(IssueCategory, on_delete=models.CASCADE)
    type = models.ForeignKey(IssueType, on_delete=models.CASCADE)
    created = models.DateTimeField()
    resolved = models.DateTimeField()


class IssueChoice(models.Model):
    issue = models.ForeignKey(Issue)
    description = models.CharField(max_length=CHAR_LENGTH)


class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created = models.DateTimeField()
    value = models.CharField(max_length=CHAR_LENGTH)
    value_choice = models.ForeignKey(IssueChoice, on_delete=models.CASCADE)
    comment = models.CharField(max_length=CHAR_LENGTH_LONG)