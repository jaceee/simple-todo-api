from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Todo(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="todos",
        related_query_name="todo",
    )
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1024)
    done = models.BooleanField(default=False)
