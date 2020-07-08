import hashlib

from django.db.models import ImageField


class CustomImageField(ImageField):
    pass


def create_image_hash(image_file):
    return hashlib.sha3_256(image_file.read(10000)).hexdigest()
