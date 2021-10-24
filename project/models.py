from django.db import models
from django_bookmark_base.models import BookmarkModel
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from PIL import Image


# Create your models here.


class Medicine(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,
                            unique_for_date='publish')

    SUPPLIED_TYPE = [
        ('Не указано', 'Не указано'),
        ('Таблетки', 'Таблетки'),
        ('Порошок', 'Порошок'),
        ('Капсулы', 'Капсулы'),
        ('Драже', 'Драже'),
        ('Гранулы', 'Гранулы'),
        ('Мазь', 'Мазь'),
        ('Крем', 'Крем'),
        ('Паста', 'Паста'),
        ('Гель', 'Гель'),
        ('Раствор', 'Раствор'),
        ('Суспензия', 'Суспензия'),
        ('Капли', 'Капли'),
        ('Сироп', 'Сироп'),
        ('Аэрозоль', 'Аэрозоль'),
        ('Другое', 'Другое'),
    ]

    SUPPLIED_TYPE = models.CharField(
        max_length=100,
        choices=SUPPLIED_TYPE,
        default='Не указано'
    )
    PHARMACY = [
        ('Нет в наличии', 'Нет в наличии'),
        ('Алибегова ул., д. 13/1', 'Алибегова ул., д. 13/1'),
        ('Воронянского ул., д. 17а', 'Воронянского ул., д. 17а'),
        ('Горецкого ул., д. 2', 'Горецкого ул., д. 2'),
        ('Городецкая ул., д. 30', 'Городецкая ул., д. 30'),
        ('Дзержинского пр-т, д. 119', 'Дзержинского пр-т, д. 119'),
    ]

    PHARMACY = models.CharField(
        max_length=500,
        choices=PHARMACY,
        default='Нет в наличии'
    )

    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('project:detailed_medicine',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    class Meta:
        ordering = ['-updated']


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    birth = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(blank=True, upload_to="user/%Y/%m/%d")
