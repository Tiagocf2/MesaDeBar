from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.

def index(request):
	template = loader.get_template('index.html')
	return HttpResponse(template.render({}, request))

def app(request):
	template = loader.get_template('app.html')
	context = {"teste":1}
	return HttpResponse(template.render(context, request))