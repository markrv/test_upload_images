from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib import messages


from core.forms import ImageForm
from core.models import Image


class ImageListView(ListView):
    model = Image

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ImageListView, self).dispatch(*args, **kwargs)


class ImageCreateView(CreateView):
    model = Image
    fields = ['title', 'image']
    success_url = reverse_lazy('images')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ImageCreateView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'ok')
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, form.errors)
        return self.get(self, request, *args, **kwargs)