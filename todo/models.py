from django.db import models
from datetime import datetime

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length = 150, null=False)
    timestamp = models.DateTimeField(default = datetime.now())
    content = models.TextField()
    def __str__(self):
        return self.title