from django.urls import path
from .views import index,thanks

urlpatterns = [
    path('index/',index),
    path('thanks/',thanks)
]
