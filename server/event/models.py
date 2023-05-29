from django.db import models
from django.contrib.auth.models import User


def upload_to(instance, filename):
    return "images/{filename}".format(filename=filename)


class Event(models.Model):
    event_name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    is_liked = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name
