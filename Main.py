v1=[] #vetor1 para nome d quem ta pagando
f=0   #variável pra finalizar loop
num_pessoas = 0
#Loop para adicionar as pessoas
while(f == 0):
    n = input('Quem vai pagar? ') 
    n = str(n)                   
    num_pessoas += 1
    v1.append(n)                 

    m = input('Mais alguém? ')   
    m = str(m)                    

    #se for adicionar mais pessoas o loop continua, senao para
    if(m == 'sim'): 
        f = 0                    
    else:
        f=1                      
        x = v1.copy()          

v2=[]       #vetor para os gastos
v3=[v1,v2]  #vetor para atrelas os nomes e gastos
#enquanto houver elementos em v1 o loop se repete 
print("")
while(len(v1) > 0):  
    d = float(input('Quanto '+ v1[0] + ' gastou?')) 
    v2.append(d)     #adiciona o valor pago
    v1.remove(v1[0]) #remove o primeiro item da lista


v1 = x               #restaura os itens q foram removidos do v1
v3 = [v1,v2]         #acho q declarei dnv sem querer

     #variavel q guarda o valor total a ser pago
valor_total = sum(v2)
resp = input("\nTem gorjeta? ")
gor_perc = 0
if(resp == "sim"):
  gor_perc = int(input("Qual o valor (%)? ")) / 100
  valor_total += valor_total * gor_perc

  #gor_ind = gor_total / num_pessoas

pgmt_cartao = [] #vetor com nome de quem paga no cartao
totald = sum(v2)
print('\nAlguém vai pagar no cartão?')
card = input() #variavel para criar loop d quem vai usar cartao

while(card == 'sim'):

    ncard = input('Nome:') #salva o nome d quem vai pagar no cartao
    matriz = v1.index(ncard) 

    if(matriz == -1):
      print("Nome nao existe")
      continue #pula o resto do codigo

    totald -= v3[1][matriz] #subtrai do valor total o item presente na coordenada [1][?] de v3
    pgmt_cartao.append(v1[matriz])

    print('Mais alguém?')
    card = input()         #reinicia ou encerra o loop

#inicializa vetores com posicoes equivalentes ao numero de pessoas
valor = [0] * num_pessoas 
troco = [0] * num_pessoas
troco_total = totald - sum(valor) #totald de gastos menos o totald de dinheiro
print("")
for i in range(num_pessoas): #i = indice
  #se a pessoa nao for pagar em cartao entao  
  if(v1[i] not in pgmt_cartao): 
    valor[i] = float(input("Quanto {} vai dar em dinheiro?".format(v1[i])))
    v2[i] += v2[i] * gor_perc
    troco[i] = valor[i] - v2[i]   

print("\n\nValor total:", valor_total)
for i in range(num_pessoas):
  print("{}: deve pagar {} e receber {} de troco.".format(v1[i], v2[i], troco[i]))

#print("\n\nPessoas:\n{}\n{}".format(v1,v2))
#print("print pgmt:", pgmt_cartao)
#print(valor," valor")
#print("gor_pec", gor_perc)
#print("gor_total", gor_total)    
#print("troco totald", troco_total)
#print("troco indi", troco)