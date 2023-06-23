from django.urls import path
from secondApp.views import index
urlpatterns = [
    path('', index),
]
