#Exercicio 19-Estrutura de Repetição For
import os
maior = 1
menor = 99999
soma = 0
num = int(input("\nDigite um conjunto de números: "))

if num > 0 and num < 1000:
    for i in range(0,num):
        numero = int(input("\nDigite os números: "))
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero            
        soma = soma + numero
    os.system("pause")
    print("\n Maior número: ", maior)
    print(" Menor número: ", menor)
    print(" Soma dos números: ", soma)
else:
    print("Valor fora do padrão aceitável.")
    
   
