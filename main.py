v1=[]
f=0

while(f == 0):

    n = input('Quem vai pagar?')
    n = str(n)

    v1.append(n)

    m = input('Mais alguém?')
    m = str(m)

    if(m == 'sim'):
        f = 0
    else:
        f=1
        x = v1.copy()

v2=[]
v3=[v1,v2]

while(len(v1) > 0):
    d = float(input('Quanto '+ v1[0] + ' gastou?'))

    v2.append(d)
    v1.remove(v1[0])

v1 = x    
v3=[v1,v2]

total = sum(v2)

print('Alguém vai pagar no cartão?')

card= input()

while(card == 'sim'):

    ncard =input('Nome:')

    matriz = v1.index(ncard)

    total = total-v3[1][matriz]
    
    print('Mais alguém?')
    card =input()
    

print(v3)
print(total)




    

