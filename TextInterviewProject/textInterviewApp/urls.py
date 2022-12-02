"""textInterviewApp
"""
from django.urls import path

from .Views import qa_views as QAV

urlpatterns = [
    path('', QAV.home, name='home'),
    path('index/', QAV.index, name='index'),
    path('create/', QAV.create, name='create'),
    path('update/<str:id>/', QAV.update, name='update'),
    path('delete/<str:id>/', QAV.delete, name='delete'),
]
