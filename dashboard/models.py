from django.db import models

# Create your models here.
# dashboard/models.py


class Project(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('On Hold', 'On Hold')
    ])
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.name