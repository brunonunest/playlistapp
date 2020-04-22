from django.conf import settings
from django.db import models


class Producer(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(default=None)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(default=None)
    producer = models.ManyToManyField(
        Producer)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(default=None)
    producers = models.ForeignKey(Producer, on_delete=models.CASCADE, default=None)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name




