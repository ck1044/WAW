from django.db import models


class Post(models.Model):
    hash_tag = models.CharField(max_length=50)
    content = models.TextField()
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.hash_tag


