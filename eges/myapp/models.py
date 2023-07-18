from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='activity_pics/', blank=True, null=True)

    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='partner_pics/', blank=True, null=True)

    def __str__(self):
        return self.name

