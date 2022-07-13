#Exercicio 24 - Calcular Média Aritmética

mediaArit = 0
somaNotas = 0
print("\t\n Programa para calcular Média Aritmética\n")

valor = int(input("\nDigite quantas notas deverão ser inseridas: "))

for i in range(0,valor):
    nota = float(input("\nDigite a nota: "))
    somaNotas += nota

mediaArit = somaNotas / valor

print("\nA média aritmética das notas é ", mediaArit)