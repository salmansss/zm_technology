from django.db import models

# Create your models here.

class batches(models.Model):
    subject = models.CharField(max_length=50)
    start_day = models.CharField(max_length=100)
    end_day = models.CharField(max_length=100)
    timing = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    true = models.BooleanField(default=False)

    def __str__(self):
        return self.subject