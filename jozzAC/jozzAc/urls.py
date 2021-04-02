
from django.contrib import admin
from django.urls import path

from .views import dasboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dasboard, name='dasboard'),
]
