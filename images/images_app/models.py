from django.contrib.auth.models import User, Group
from django.db import models
from sorl.thumbnail import get_thumbnail


class Image(models.Model):
    image = models.ImageField(upload_to='media')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def thumbnails(self):
        if self.image:
            group = self.owner.groups.first()
            sizes = group.groupdetail.thumbnail_set.all()
            result = []
            for size in sizes:
                hgt = 'x%s' % size
                thmb = get_thumbnail(self.image, hgt)
                result.append(thmb)
            return result
        return None

    @property
    def original_image(self):
        if self.image:
            group = self.owner.groups.first()
            if group.groupdetail.original_image == True:
                return self.image
            return None
        return None


class GroupDetail(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    original_image = models.BooleanField(default=True)

    def __str__(self):
        return self.group.name


class Thumbnail(models.Model):
    height = models.PositiveIntegerField()
    group = models.ManyToManyField(GroupDetail)

    def __str__(self):
        return str(self.height)
