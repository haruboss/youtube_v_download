from django.urls import path
from . import views

app_name = 'downloadVideo'

urlpatterns = [
    path('', views.home, name='home'),
    path('download-video/', views.download_video, name='download'),

]
