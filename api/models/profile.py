from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )


def __str__(self):
    # This must return a string
    return f"{self.name} {self.about} by {self.owner}"


def as_dict(self):
    """Returns dictionary version of buffpost models"""
    return {
        'id': self.id,
        'name': self.name,
        'about': self.about,
        'owner': self.owner
    }
