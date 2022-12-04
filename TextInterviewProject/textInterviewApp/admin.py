""" textInterviewApp
管理サイトにmodels.pyで作成したモデルを登録するには以下のようにadmin.pyを編集する。

"""
from django.contrib import admin

from .Models.qa_models import *


# 管理サイトで「Question」モデルのCRUDを実行する
admin.site.register(Question)
