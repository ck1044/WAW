from django.urls import path

from . import views

app_name = 'waw'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('aboutUs/', views.aboutUS, name='aboutUs'),
    path('write', views.write, name='write'),
    path('login', views.login, name='login'),
]
