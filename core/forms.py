from django import forms
from core.models import Image
from core.utils import create_image_hash


class ImageForm(forms.ModelForm):
    class Meta(object):
        model = Image
        exclude = ['checksums']

    def clean_image(self):
        image = self.cleaned_data['image']
        hash = create_image_hash(image)
        self.instance.checksums = hash
        if Image.objects.filter(checksums=hash).exists():
            raise forms.ValidationError('Такой файл уже был загружен ранее')
        return image


