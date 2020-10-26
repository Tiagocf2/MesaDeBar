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
valor_total = 0  #valor total da conta
troco_total = 0  #valor do troco da conta
tipo_divisao = 0 #tipo de divisao da conta
gor_perc = 0     #percentual de gorjeta
pessoas = []     #vetor para armazenar as pessoas
id_atual = 0     #armazena o proximo id livre
pessoa_model = { #modelo para uma pessoa
	"id":'0',
	"nome":"",
	"pgmt":PGMT_DINHEIRO,
	"gasto":0,
	"valor":0,
	"troco":0
}
grupos = []
grupo_model = {
	"nome":"",
	"pessoas":[],
	"valor":0
}

"""VIEWS"""
def index(request):
	template = loader.get_template('index.html')
	context = {}
	return HttpResponse(template.render(context, request))

def app(request):
	template = loader.get_template('app-ini.html')
	context = {}
	return HttpResponse(template.render(context, request))

def app_error(request):
	template = loader.get_template('app-error.html')
	context = {"msg":request.GET.get("msg")}
	return HttpResponse(template.render(context, request))

def app_gsto(request):
	'''Processa os nomes das pessoas e o tipo de divisao'''
	global tipo_divisao, pessoas, valor_total
	pessoas = []
	valor_total = 0

		
	if ("nome" not in request.POST):
		return throw_error("Por favor não mude o nome da chave ;)")

	#QueryDict retorna so o ultimo valor de uma chave entao precisa de '.getList()' pra pegar todos os valores
	nomes = request.POST.getlist("nome")
	
	if(len(nomes) <= 0):
		return throw_error("Nenhum nome foi especificado")

	for nome in nomes:
		adicionar_pessoa(nome.capitalize())

	if("divisao" in request.POST):
		tipo_divisao = definir_tipo_divisao(int(request.POST["divisao"]))
		if(tipo_divisao == None):
			return throw_error("Tipo de divisão inválido")
			
	else:
		return throw_error("Tipo de divisão não especificado")

	template = loader.get_template('app-gsto.html')
	context = {"div":tipo_divisao, "pessoas":pessoas}
	return HttpResponse(template.render(context, request))

def app_pgmt(request):
	'''Processa os valores dos gastos e a gorjeta'''
	global gor_perc, valor_total, pessoas, tipo_divisao, grupos, grupo_model
	gor_perc = 0
	grupos = []

	if("gorjeta" not in request.POST or "gasto" not in request.POST):
		return throw_error("Por favor não mude o nome da chave ;)")

	if("temGorjeta" not in request.POST):
		temGorjeta = False
	else:
		temGorjeta = True

	if (tipo_divisao == DIVISAO_NORMAL):
		gastos = request.POST.getlist("gasto")
		for i in range(0, len(pessoas)):
			gastos[i] = round(float(gastos[i]),2)
			pessoas[i]["gasto"] = gastos[i]
			valor_total += gastos[i]

	elif (tipo_divisao == DIVISAO_IGUAL):
		gasto = float(request.POST["gasto"])
		valor_total = gasto
		valor_indv = round(valor_total/len(pessoas),2)
		for p in pessoas:
			p["gasto"] += valor_indv

	elif (tipo_divisao == DIVISAO_PARCIAL):
		gastos = request.POST.getlist("gasto")
		for i in range(0, len(pessoas)):
			gastos[i] = round(float(gastos[i]),2)
			pessoas[i]["gasto"] = gastos[i]
			valor_total += gastos[i]
		g_nomes = request.POST.getlist("grupo-nome")
		g_valores = request.POST.getlist("grupo-valor")
		g_pessoas = request.POST.getlist("grupo-pessoa")
		for i in range(len(g_nomes)):
			valor = float(g_valores[i])
			membros = g_pessoas[i].split(",")
			grupo = grupo_model.copy()
			grupo["nome"] = g_nomes[i]
			grupo["valor"] = valor
			grupo["pessoas"] = membros
			grupos.append(grupo)
			valor_total += valor
			valor_indv = round(valor/len(membros),2)
			for _id in membros:
				for p in pessoas:
					if(p["id"] == int(_id)):
						p["gasto"] += valor_indv

	if(temGorjeta):
		gor_perc = float(request.POST["gorjeta"])/100
		valor_total += round(valor_total * gor_perc,2)
		for p in pessoas:
			p["gasto"] += round(p["gasto"] * gor_perc,2)

	template = loader.get_template('app-pgmt.html')
	context = {
		"total": valor_total,
		"gorjeta": gor_perc,
		"pessoas": pessoas,
		"div": string_divisao(tipo_divisao)
	}
	return HttpResponse(template.render(context, request))

def app_rslt(request):
	'''Processa os valores de pagamento e troco'''
	global gor_perc, valor_total, pessoas, tipo_divisao, troco_total, grupos
	troco_total = 0

	if("pgmt" not in request.POST or "valor" not in request.POST):
		return throw_error("Por favor não mude o nome da chave ;)")

	pgmts = request.POST.getlist("pgmt")
	valores = request.POST.getlist("valor")

	for i in range(0, len(pessoas)):
		if(pgmts[i] == "on"):
			pessoas[i]["pgmt"] = PGMT_CARTAO
		elif(pgmts[i] == "off"):
			pessoas[i]["pgmt"] = PGMT_DINHEIRO

		if(pessoas[i]["pgmt"] == PGMT_DINHEIRO):
			pessoas[i]["valor"] = round(float(valores[i]),2)
			troco = pessoas[i]["valor"] - pessoas[i]["gasto"]
			pessoas[i]["troco"] = troco
			troco_total += troco

	template = loader.get_template('app-rslt.html')
	context = {
		"total": valor_total,
		"troco": troco_total,
		"gorjeta": gor_perc,
		"pessoas": pessoas,
		"div": tipo_divisao,
		"grupos": grupos
	}
	return HttpResponse(template.render(context, request))

"""OUTRAS FUNCOES"""
def throw_error(msg):
	base_url = reverse('app-error')
	get_args = urlencode({"msg":msg})
	url = "{}?{}".format(base_url, get_args);
	return redirect(url);

def adicionar_pessoa(nome):
	'''Adiciona uma pessoa à conta'''
	global id_atual
	p = pessoa_model.copy()
	p["nome"] = nome
	p["id"] = str(id_atual)
	pessoas.append(p)
	id_atual += 1
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

def string_divisao(valor):
	if(valor == 0):
		return "Divisão Normal"
	elif(valor == 1):
		return "Divisão Igual"
	elif(valor == 2):
		return "Divisão Parcial"
	return None;