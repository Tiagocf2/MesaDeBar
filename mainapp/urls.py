from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
	path('', views.index, name="index"),
	path('app/', views.app, name="app"),
]
