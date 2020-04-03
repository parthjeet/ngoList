from django.urls import path

from . import views

app_name = 'ngoTable'
urlpatterns = [
    path('', views.index, name='index')
]