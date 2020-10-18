from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
	path('', views.index, name="index"),
	path('app/', views.app, name="app"),
	path('app/error', views.app_error, name="app-error"),
	path('app/gastos', views.app_gsto, name="app-gsto"),
]
