from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=250)
    published = models.DateTimeField(auto_now_add=True)
    userName= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        date_time = self.published.strftime("%m/%d/%Y, %H:%M:%S")
        return "{} {}".format(self.title, date_time)
