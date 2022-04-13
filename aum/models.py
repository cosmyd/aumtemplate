from django.db import models
from django.utils import timezone

class Member(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile_pics')
    role = models.CharField(max_length=150, blank=True)
    bio = models.TextField()
    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=100)
    date_uploaded = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='news_pics')
    paragraph1 = models.TextField()
    article = models.TextField()
    image2 = models.ImageField(upload_to='news_pics', blank=True)
    article2 = models.TextField(blank=True)
    link1_prompt = models.TextField(blank=True)
    link1 = models.URLField(blank=True)
    album = models.URLField(blank=True)
    hashtag = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100)
    period = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project_pics')
    paragraph1 = models.TextField()
    article = models.TextField()
    image2 = models.ImageField(upload_to='news_pics', blank=True)
    article2 = models.TextField(blank=True)
    link1_prompt = models.TextField(blank=True)
    link1 = models.URLField(blank=True)
    album = models.URLField(blank=True)
    hashtag = models.URLField(blank=True)
    present = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='event_pics')
    paragraph1 = models.TextField()

    def __str__(self):
        return self.title

class YEvent(models.Model):
    title = models.CharField(max_length=150)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_pics')
    paragraph1 = models.TextField()
    forms_rules = models.URLField(blank=True)
    album = models.URLField(blank=True)
    hashtag = models.URLField(blank=True)
    link1_prompt = models.TextField(blank=True)
    link1 = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Number(models.Model):
    name = models.CharField(max_length=150)
    value = models.CharField(max_length=10)

class Collaborator(models.Model):
    name = models.CharField(max_length=100)
    contry = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='collaborator_pics')
    local = models.BooleanField(default=False)

    def __str__(self):
        return self.name