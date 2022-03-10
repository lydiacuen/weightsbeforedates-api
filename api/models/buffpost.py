from django.db import models
from django.contrib.auth import get_user_model

# When we run makemigrations, and migrate, it applies all of the schema or the way we have models.py organized and fields declared. It takes what we wrote in django and makes sure the database matches that.


class BuffPost(models.Model):
    # we add a blank=True and null=True in content because if we just want to post a motivational quote image, we do not need to have any text.
    content = models.TextField(blank=True, null=True)
    # same here, we add the blank=True and null=True because if we add text but not an image, then that is ok too.
    image = models.FileField(upload_to='images/', blank=True, null=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

def __str__(self):
    # This must return a string
    return f"{self.content} {self.image} by {self.owner}"

def as_dict(self):
    """Returns dictionary version of buffpost models"""
    return {
        'id': self.id,
        'content': self.content,
        'image': self.image,
        'owner': self.owner
    }
