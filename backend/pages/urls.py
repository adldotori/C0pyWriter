from . import views
from django.urls import path

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('complete/', views.complete, name='complete'),
    path('summary/', views.summary, name='summary'),
]