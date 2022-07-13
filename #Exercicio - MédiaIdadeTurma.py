#Exercicio 25 - Estrutura de Repetição For
import os
media = 0
resultado = 0
print("\n\t MÉDIA DA TURMA FLOR DA IDADE\n")

pessoas = int(input("Entre com a quantidade de pessoas da turma: "))

for i in range(0,pessoas):
    idade = int(input("\nDigite sua idade: "))
    media += idade

resultado = media / pessoas
os.system("cls")
print("\nMédia das idades: ", resultado)

if resultado > 0 and resultado < 25:
    print("\nA turma é considerada Jovem!")
    os.system("pause")
elif resultado > 26 and resultado < 60:
    print("\nA turma é considerada Adulto(a)!")
    os.system("pause")
elif resultado > 61:
    print("\nA turma é considerada Idoso(a)!")
    os.system("pause")