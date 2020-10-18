from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse
from urllib.parse import urlencode
# Create your views here.

"""VARIAVEIS GLOBAIS"""
DIVISAO_NORMAL  = 0 #constante do tipo de divisao normal
DIVISAO_IGUAL   = 1 #constante do tipo de divisao igual
DIVISAO_PARCIAL = 2 #constante do tipo de divisao parcial
PGMT_DINHEIRO = 0 #constante do pagamento em dinheiro
PGMT_CARTAO   = 1 #constante do pagamento em cartao
tipo_divisao = 0 #tipo de divisao da conta
pessoas = []     #vetor para armazenar as pessoas
pessoa_model = { #modelo para uma pessoa
	"nome":"",
	"pgmt":PGMT_DINHEIRO,
	"gasto":0,
	"valor":0,
	"troco":0
}

"""VIEWS"""
def index(request):
	template = loader.get_template('index.html')
	context = {}
	return HttpResponse(template.render(context, request))

def app(request):
	template = loader.get_template('app-ini.html')
	context = {};
	return HttpResponse(template.render(context, request))

def app_error(request):
	template = loader.get_template('app-error.html')
	context = {"msg":request.GET.get("msg")}
	return HttpResponse(template.render(context, request))

def app_gsto(request):
	'''Processa os nomes das pessoas e o tipo de divisao'''
	global tipo_divisao
	global pessoas
	#QueryDict retorna so o ultimo valor de uma chave entao precisa de '.getList()' pra pegar todos os valores
	for nome in request.POST.getlist("nome"):
		adicionar_pessoa(nome.capitalize())

	if("divisao" in request.POST):
		tipo_divisao = definir_tipo_divisao(int(request.POST["divisao"]))
		if(tipo_divisao == None):
			msg = "Tipo de divisão inválido"
			return throw_error(msg)
			
	else:
		msg = "Tipo de divisão não especificado"
		return throw_error(msg)

	template = loader.get_template('app-gsto.html')
	context = {"div":tipo_divisao, "pessoas":pessoas}
	return HttpResponse(template.render(context, request))

"""OUTRAS FUNCOES"""
def throw_error(msg):
	base_url = reverse('app-error')
	get_args = urlencode({"msg":msg})
	url = "{}?{}".format(base_url, get_args);
	return redirect(url);

def adicionar_pessoa(nome):
	'''Adiciona uma pessoa à conta'''
	p = pessoa_model.copy()
	p["nome"] = nome
	pessoas.append(p)
	return p

def definir_tipo_divisao(valor):
	'''Define como a conta sera dividida'''
	if(valor == 0):
		return DIVISAO_NORMAL
	elif(valor == 1):
		return DIVISAO_IGUAL
	elif(valor == 2):
		return DIVISAO_PARCIAL
	return None;
