from django.db import models

# Create your models here.

class Simple(models.Model):
    text = models.CharField(max_length=50)
    number = models.IntegerField(null=True)
    url = models.URLField(default='www.example.com')

    def __str__(self):
        return self.text