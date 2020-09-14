v1=[] #vetor1 para nome d quem ta pagando
f=0   #variável pra finalizar loop


while(f == 0): #loop q add quem paga

    n = input('Quem vai pagar?') 
    n = str(n)                   #nome das pessoas q vao pagar

    v1.append(n)                 #adiciona o nome no vetor 1

    m = input('Mais alguém?')   
    m = str(m)                   #variavel para o if abaixo q decide se o loop continua

    if(m == 'sim'):
        f = 0                    #se mais pessoas serao add a variavel f n muda
    else:
        f=1                      #se n houver mais pessoas o valor de f mudo finalizando o loop
        x = v1.copy()            #copia v1 em x para ser restourado dps



v2=[]       #vetor2 para o valor que cada um gastou*
v3=[v1,v2]  #matrizv3 para atrelar os vetores 1 e 2.
             #(pois será necessario q o conteudo dos v1 e v2 tenham coordenadas)



while(len(v1) > 0): #enquanto houver elementos em v1 o loop se repete  #loop q pergunta quanto cada um gastou e 
    d = float(input('Quanto '+ v1[0] + ' gastou?')) #add o valor       # q se auto finaliza
                                                    #v1[0]adiciona o 
                                                    #primeiro nome do v1
    v2.append(d)     #adiciona o valor pago
    v1.remove(v1[0]) #remove o primeiro item d v1, assim o segundo nome se torna v1[0]
                     #quando v1 n tiver mais itens o len(v1) se torna 0, finalizando o loop 



v1 = x               #restaura os itens q foram removidos do v1
v3=[v1,v2]           #acho q declarei dnv sem querer

total = sum(v2)      #variavel q guarda o valor total a ser pago



print('Alguém vai pagar no cartão?')

card= input() #variavel para criar loop d quem vai usar cartao

while(card == 'sim'):

    ncard =input('Nome:') #salva o nome d quem vai pagar no cartao

    matriz = v1.index(ncard) #procura a posiçao(q é um numero/coordenada d v3) 
                             # do nome escrito em ncard no v1 e salva como um numero/coordenada

    total = total-v3[1][matriz] #subtrai do valor total o item presente na coordenada [1][?] de v3
    
    print('Mais alguém?')
    card =input()         #reinicia ou encerra o loop
    

print(v3)     #prints q coloquei só para testar se estava funcionando direito
print(total)




    

