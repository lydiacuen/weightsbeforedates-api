from django.db import models
from django.contrib.auth import get_user_model

class BuffPost(models.Model):
    content = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
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
