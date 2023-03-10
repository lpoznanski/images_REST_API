from django.contrib.auth.models import User
from django.db import models
from sorl.thumbnail import get_thumbnail

class Image(models.Model):
    image = models.ImageField(upload_to='media')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def small(self):
        if self.image:
            return get_thumbnail(self.image, 'x200', quality=90)
        return None

    @property
    def large(self):
        if self.image:
            return get_thumbnail(self.image, 'x400', quality=90)
        return None
