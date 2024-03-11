from django.db import models

# Create your models here.
class RemindMeLater(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.date} {self.time} - {self.message}'