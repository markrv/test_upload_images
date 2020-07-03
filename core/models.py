from django.db import models
from django.urls import reverse

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from core.utils import CustomImageField


class Image(models.Model):
    title = models.CharField(max_length=254)
    image = CustomImageField(upload_to='user_img')

    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(350, 350)],
                                      format='JPEG',
                                      options={'quality': 80})

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'pk': self.pk})