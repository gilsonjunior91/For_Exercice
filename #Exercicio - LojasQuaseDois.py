#Exercicio 29 - Lojas Quase Dois

import time             #UTILIZADO PARA A FUNÇÃO SLEEP()

soma = 0
print("\t\nLOJAS QUASE DOIS")

for i in range(1,11):
    soma += 1.99
    print("Item [",i,"] - VALOR R$",soma)
    time.sleep(2.5)
   
