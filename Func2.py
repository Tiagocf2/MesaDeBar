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
                  
v2=[0] * len(v1)      #vetor para os gastos divididos
v3=[v1,v2]  #vetor para atrelar os nomes e gastos
#enquanto houver elementos em v1 o loop se repete 

print("")

total = float(input('Quanto deu a conta?')) 

resp = input("\nTem gorjeta? ") 
gor_perc = 0
if(resp == "sim"):
  gor_perc = int(input("Qual o valor (%)? ")) / 100
  total += total * gor_perc                          #adiciona-se o valor da gorjeta ao valor total

v_indiv = total/len(v1)       #divide o valor total igualmente

for i in range(len(v1)):
    v2[i] = v2[i] + v_indiv   #adiciona os valores individuais ao v2

print("")
print("Cada um deve pagar", v_indiv, ".")

pgmt_cartao=[]  #vetor q terá os nomes d quem pagar no cartão
print('\nAlguém vai pagar no cartão?')
card = input() #variavel para criar loop d quem vai usar cartao

while(card == 'sim'):

    ncard = input('Nome:') #salva o nome d quem vai pagar no cartao
    matriz = v1.index(ncard) 

    if(matriz == -1):
      print("Nome nao existe")
      continue #pula o resto do codigo
      
    pgmt_cartao.append(v1[matriz]) #adiciona o nome d quem ta d cartao à pgmt_cartao

    print('Mais alguém?')
    card = input()       

valor = [0] * num_pessoas  #valor d dinheiro entregue por cada um
troco = [0] * num_pessoas  #vetor c o troco d cada um

print("")
for i in range(num_pessoas): #i = indice
  #se a pessoa nao for pagar em cartao entao  
  if(v1[i] not in pgmt_cartao): 
    valor[i] = float(input("Quanto {} vai dar em dinheiro?".format(v1[i]))) #recebe os valores em dinheiro entregues
    
    troco[i] = valor[i] - v2[i]   
    troco_total = (sum(valor) + v_indiv * len(pgmt_cartao)) - total    #calcula troco total e troco d cada um

print("\n\nValor total:", total)
print("Troco total:", troco_total)
for i in range(num_pessoas):
  print("{}: deve pagar {} e receber {} de troco.".format(v1[i], v2[i], troco[i]))


#print(v3)
#print(total)
#print(v_indiv)
#print(valor)
#print(troco_total)
#print(troco)


