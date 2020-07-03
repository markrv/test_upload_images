from django import forms
from core.models import Image


class ImageForm(forms.ModelForm):
    class Meta(object):
        model = Image
        exclude = ('title',)