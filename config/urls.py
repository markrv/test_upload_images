"""test_upload_images URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.conf import settings

from core.views import ImageListView, ImageCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ImageListView.as_view(), name='images'),
    path('uploading_image/', ImageCreateView.as_view(), name='uploading_image'),

    path('login/', LoginView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
