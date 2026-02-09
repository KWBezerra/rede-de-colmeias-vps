from django.urls import path
from . import views

app_name = "tutorial"

urlpatterns = [
    path('', views.tutorial_list, name='tutorial_list'),
    path('tutorials/<slug:slug>/', views.tutorial_detail, name='tutorial_detail'),
]
