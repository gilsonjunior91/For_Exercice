#Exercicio 15 - Estrutura de Repetição For

ulti = 1
penu = 1
numero = int(input("\nDigite o número para sequencia de Fibonacci: "))

for n in range(2,numero):
    termo = ulti + penu
    penu = ulti
    ulti = termo
    n +=1

print(termo)