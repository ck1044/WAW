from django.db import models


class Post(models.Model):
    date = models.CharField(max_length=50)
    # date_write = models.DateField()
    content = models.TextField()
    photo = models.ImageField(blank=True)
    likes = models.ManyToManyField


