"""textInterviewApp
複数のアプリケーションを作成する場合は、「app_name」を用いて名前空間を指定する必要がある。
(例)app_name = 'textInterviewApp'
これをしないと、templatesなどで指定したいurlが適切に指定できなくなる。
ただし、アプリが1つしかない場合は、無理に設定しなくてよい。
"""
from django.urls import path

from .Views import qa_views as QAV
from .Views import simulate_views as SIM
from .Views import auth_views as AUTH


urlpatterns = [
    path('', QAV.home, name='home'),
    path('index/', QAV.index, name='index'),
    path('create/', QAV.create, name='create'),
    path('update/<str:id>/', QAV.update, name='update'),
    path('delete/<str:id>/', QAV.delete, name='delete'),
    path('simulate/', SIM.sim_index, name='sim_index'),
    path('simulate/start/', SIM.sim_start, name='sim_start'),
    path('login/', AUTH.login, name='login'),
    path('signup/', AUTH.signup, name='signup'),
]
