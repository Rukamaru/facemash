import os
import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

"""class User(models.Model):
    user = models.OneToOneField(User, null=True)
    photo = models.ForeignKey('Photo')"""

class Question(models.Model):
    question_text = models.CharField('Texte', max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    pub_date = models.DateTimeField('Date de publication', default=timezone.now)
    # choice = models.ManyToManyField('Choice')
    author = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Recente ?'


class Choice(models.Model):
    question = models.ForeignKey('Question', null=True)
    photo = models.ForeignKey('Photo')
    choice_text = models.CharField('Choice', max_length=200, null=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)


"""class User(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    photo = models.ForeignKey('Photo')"""


class Photo(models.Model):
    file = models.ImageField()

    def __str__(self):
        return os.path.basename(self.file.name)

