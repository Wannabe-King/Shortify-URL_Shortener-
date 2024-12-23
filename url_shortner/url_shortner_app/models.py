from django.db import models

# Create your models here.
class URL(models.Model):
    url=models.URLField()
    shortCode=models.CharField(max_length=30)
    created_at=models.DateTimeField()
    # updated_at=models.DateTimeField()
    access_count = models.IntegerField(default=0)