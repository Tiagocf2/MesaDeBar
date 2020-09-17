PGMT_DINHEIRO = 0 #constante do pagamento em dinheiro
PGMT_CARTAO   = 1 #constante do pagamento em cartao
valor_total = 0  #valor total da conta
troco_total = 0  #valor do troco da conta
num_pessoas = 0  #numero total de pessoas
gor_perc = 0     #percentual de gorjeta
pessoas = []     #vetor para armazenar as pessoas
pessoa_model = { #modelo para uma pessoa
    "nome":"",
    "pgmt":PGMT_DINHEIRO,
    "gasto":0,
    "valor":0,
    "troco":0
}


#Loop para adicionar as pessoas
f=0   #variável pra finalizar loop
while(f == 0):
    nome = input('Quem vai pagar? ').capitalize()
    p = pessoa_model.copy()
    p["nome"] = nome                  
    pessoas.append(p)              
    num_pessoas += 1

    m = input('Mais alguém? ')                     
    #se for adicionar mais pessoas o loop continua, senao para
    if(m.lower() != 'sim'): 
        f = 1                              
 
print("")
for p in pessoas:
    val = float(input('Quanto '+ p["nome"] + ' gastou?')) 
    p["gasto"] = val     #adiciona o valor pago
    valor_total += val

resp = input("\nTem gorjeta? ")
if(resp == "sim"):
  gor_perc = int(input("Qual o valor (%)? ")) / 100
  valor_total += valor_total * gor_perc #adiciona o valor da gorjeta no total

total_card = valor_total
resp = input('\nAlguém vai pagar no cartão?').lower()

if(resp == 'sim'):
    for i in range(num_pessoas):
        print("{}. {}".format(i+1, pessoas[i]["nome"]))
    while(resp == 'sim'):
        resp = int(input("Quem? "))
        pessoas[resp-1]["pgmt"] = PGMT_CARTAO
        #subtrai do valor total o gasto da pessoa escolhida
        total_card -= pessoas[resp-1]["gasto"] 
        resp = input('Mais alguém?')

print("")
for p in pessoas:
  p["gasto"] += p["gasto"] * gor_perc #adiciona a gorjeta nos gastos de cada um
  #se a pessoa nao for pagar em cartao entao  
  if(p["pgmt"] == PGMT_DINHEIRO): 
    p["valor"] = float(input("Quanto {} vai dar em dinheiro?".format(p["nome"])))
    p["troco"] = p["valor"] - p["gasto"]   
    troco_total += p["troco"] 


print("\n\nValor total:", valor_total)
print("Troco total:", troco_total)
for p in pessoas:
  print("{}: deve pagar {} e receber {} de troco.".format(p["nome"], p["gasto"], p["troco"]))

#print("\n\nPessoas:\n{}\n{}".format(v1,v2))
#print("print pgmt:", pgmt_cartao)
#print(valor," valor")
#print("gor_pec", gor_perc)
#print("gor_total", gor_total)    
#print("troco total_card", troco_total)
#print("troco indi", troco)




    

