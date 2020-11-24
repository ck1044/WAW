from django.db import models


<<<<<<< HEAD

=======
class Post(models.Model):
    hash_tag = models.CharField(max_length=50)
    content = models.TextField()
    photo = models.ImageField(blank=True)
    pin = models.DecimalField(max_digits=99999999, decimal_places=0)

    def __str__(self):
        return self.hash_tag
>>>>>>> dce61b5fd3bbd03db21dfcfa6d22f1e080bde1ce

