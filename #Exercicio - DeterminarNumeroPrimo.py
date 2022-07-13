#Exercicio 21 e 22 - Estrutura de Repetição For

total = 0
print("\t Determinar se um número é primo.\n")
numero = int(input("Digite um número: "))

for i in range(2, numero):
    if numero % i ==  0:
        print("Multiplo de ", i)
        total += 1
if total == 0:
    print("É primo.")
else:
    print("Possui ", total, " múltiplos acima de 2 e abaixo de ", numero)