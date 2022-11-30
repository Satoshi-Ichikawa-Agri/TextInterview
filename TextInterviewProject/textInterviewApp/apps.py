""" Apps
appの設定を記述することでその内容をconfigフォルダのsettings.pyで読み込めるようにし、
結果的にプロジェクト全体に、該当するappの機能を反映しています。

"""
from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'textInterviewApp'
