from django.db import models

# Create your models here.

class Publication(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_time_of_creation = models.DateTimeField(auto_now_add = True)
    commentaries = models.ManyToManyField("Commentary")

    def __str__(self):
        return self.title


class Commentary(models.Model):
    text = models.TextField()
    author = models.CharField(max_length = 63)
    date_time_of_creation = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.text
    