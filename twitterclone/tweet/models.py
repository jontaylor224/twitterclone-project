from django.db import models
from django.utils import timezone

class Tweet(models.Model):
    content = models.CharField(max_length=140)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    time_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content
