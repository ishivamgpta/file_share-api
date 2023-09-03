
from django.urls import path
from .views import FileList

urlpatterns = [
    path('files/', FileList.as_view(), name='file-list'),
]