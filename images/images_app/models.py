from django.contrib.auth.models import User
from django.db import models
from sorl.thumbnail import get_thumbnail

class Image(models.Model):
    image = models.ImageField(upload_to='media')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def thumbnail(self):
        if self.image:
            return get_thumbnail(self.image, '200', quality=90)
        return None
