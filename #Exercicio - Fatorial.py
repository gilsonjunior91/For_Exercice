#Exercicio 17-Estrutura de Repetição For
fat = 1

numero = int(input("\nDigite um número para ver o seu fatorial: "))
for i in range(1, numero + 1):
    fat = fat * i
print("Fatorial de ", numero," é: ", fat)