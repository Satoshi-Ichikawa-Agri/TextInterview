"""textInterviewApp
"""
from django.urls import path

from .Views import qa_views as QAV
from .Views import simlate_views as SIM

urlpatterns = [
    path('', QAV.home, name='home'),
    path('index/', QAV.index, name='index'),
    path('create/', QAV.create, name='create'),
    path('update/<str:id>/', QAV.update, name='update'),
    path('delete/<str:id>/', QAV.delete, name='delete'),
    path('simulate/', SIM.sim_index, name='sim_index'),
    path('simulate/start/', SIM.sim_start, name='sim_start'),
]
