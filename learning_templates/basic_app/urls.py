from django.urls import path
from basic_app import views

# TEMPLATE TAGGING
# app_nameに指定した文字列が、HTMLファイル内のurl '〇〇:'、〇〇部分に対応する。
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
