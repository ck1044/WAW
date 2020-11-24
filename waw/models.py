from django.db import models



class Post(models.Model):
    hash_tag = models.CharField(max_length=100)
    content = models.TextField()

