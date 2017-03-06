from django.contrib import admin

from .models import Body, Voter, IssueCategory, Proxy, IssueType, Issue, IssueChoice, Vote

admin.site.register((Body, Voter, IssueCategory, Proxy, IssueType, Issue, IssueChoice, Vote))

# Register your models here.
