from django.urls import path
from . import views

app_name = 'opening'
urlpatterns = [
    path('', views.index, name='index'),
    path('find/', views.find, name='find')
]