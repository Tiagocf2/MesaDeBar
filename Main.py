DIVISAO_NORMAL  = 0 #constante do tipo de divisao normal
DIVISAO_IGUAL   = 1 #constante do tipo de divisao igual
DIVISAO_PARCIAL = 2 #constante do tipo de divisao parcial
PGMT_DINHEIRO = 0 #constante do pagamento em dinheiro
PGMT_CARTAO   = 1 #constante do pagamento em cartao
tipo_divisao = 0 #tipo de divisao da conta
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

def main():
    tipo_divisao = definir_tipo_divisao()
    #Loop para adicionar as pessoas
    f=0   #variável pra finalizar loop
    while(f == 0):
        nome = input('Quem vai pagar? ').capitalize()
        adicionar_pessoa()

        m = input('Mais alguém? ')                     
        #se for adicionar mais pessoas o loop continua, senao para
        if(m.lower() != 'sim'): 
            f = 1                              
     
    print("")
    definir_gastos(tipo_divisao)
    print("")
    definir_gorjeta()
    print("")
    definir_pagamentos()
    print("")
    definir_valores()
    print("\n") 
    exibir_resultados()


#print("\n\nPessoas:\n{}\n{}".format(v1,v2))
#print("print pgmt:", pgmt_cartao)
#print(valor," valor")
#print("gor_pec", gor_perc)
#print("gor_total", gor_total)    
#print("troco total_card", troco_total)
#print("troco indi", troco)

def definir_tipo_divisao():
'''Define como a conta sera dividida'''
    print("Qual vai ser o modo de divisao?\n1. Normal\n2. Igualmente\n3. Parcialmente")
    resp = int(print("> "))
    if(resp == 1):
        return DIVISAO_NORMAL
    elif(resp == 2):
        return DIVISAO_IGUAL
    elif(resp == 3):
        return DIVISAO_PARCIAL

def adicionar_pessoa(nome):
'''Adiciona uma pessoa à conta'''
    p = pessoa_model.copy()
    p["nome"] = nome                  
    pessoas.append(p)              
    num_pessoas += 1

def definir_gorjeta():
'''Define o valor da gorjeta em % e adiciona ao valor total da conta'''
    resp = input("Tem gorjeta? ")
    if(resp == "sim"):
      gor_perc = int(input("Qual o valor (%)? ")) / 100
      valor_total += valor_total * gor_perc #adiciona o valor da gorjeta no total

def definir_gastos(div):
'''Define os gastos de cada pessoa levando em conta o tipo de divisão escolhido'''
    if(div == DIVISAO_NORMAL):
        #loop se repete de acordo com o tamanho do vetor "pessoas"
        #armazenando o valor de cada elemento na variavel "p" a cada ciclo
        for p in pessoas:
            val = float(input('Quanto '+ p["nome"] + ' gastou?')) 
            p["gasto"] = val     #adiciona o valor pago
            valor_total += val

    elif  (div == DIVISAO_IGUAL):
        v_indiv = total/len(v1)       #divide o valor total igualmente
        for i in range(len(v1)):
            v2[i] = v2[i] + v_indiv   #adiciona os valores individuais ao v2
        print("Cada um deve pagar", v_indiv, ".")

    elif(div == DIVISAO_PARCIAL):
        pass

def definir_pagamentos():
'''Define o pagamento em cartão para as pessoas escolhidas'''
    resp = input('Alguém vai pagar no cartão?').lower()
    if(resp == 'sim'):
        for i in range(num_pessoas):
            print("{}. {}".format(i+1, pessoas[i]["nome"]))
        while(resp == 'sim'):
            resp = int(input("Quem? "))
            pessoas[resp-1]["pgmt"] = PGMT_CARTAO
            resp = input('Mais alguém?')

def definir_valores():
    '''Define o valor para cada pessoa incluindo a gorjeta'''
    for p in pessoas:
      p["gasto"] += p["gasto"] * gor_perc #adiciona a gorjeta nos gastos de cada um
      #se o metodo de pagamento da pessoa for dinheiro, entao  
      if(p["pgmt"] == PGMT_DINHEIRO): 
        p["valor"] = float(input("Quanto {} vai dar em dinheiro?".format(p["nome"])))
        p["troco"] = p["valor"] - p["gasto"]   
        troco_total += p["troco"] 

def exibir_resultados():
'''Exibe o resultado final da conta'''
    print("Valor total:", valor_total)
    print("Troco total:", troco_total)
    for p in pessoas:
      print("{}: deve pagar {} e receber {} de troco.".format(p["nome"], p["gasto"], p["troco"]))

if(__name__ == "__main__"):
    main()