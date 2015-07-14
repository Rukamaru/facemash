import os
import datetime
from django.utils import timezone
from django.db import models


class Question(models.Model):
    question_text = models.CharField('Texte', max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    pub_date = models.DateTimeField('Date de publication', default=timezone.now)
    choice = models.ManyToManyField('Choice')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Recente ?'


class Choice(models.Model):
    votes = models.IntegerField(default=0)
    photo = models.ForeignKey('Photo')

    def __str__(self):
        return str(self.photo)


class User(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    photo = models.ForeignKey('Photo')

    def __str__(self):
        return self.name + " " + self.first_name


class Photo(models.Model):
    file = models.ImageField(upload_to="photos/")

    def __str__(self):
        return os.path.basename(self.file.name)

