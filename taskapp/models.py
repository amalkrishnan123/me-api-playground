from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    education = models.CharField(max_length=200)

class Skill(models.Model):
    name = models.CharField(max_length=50)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True)
    skills = models.ManyToManyField(Skill)