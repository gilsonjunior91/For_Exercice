#Exercicio 14 - Estrutura de Repetição For

par = 0
impar = 0
numero = 0
print("\tDigite 10 número inteiros")
for n in range(0,10):
    numero = int(input("\nNúmeros: "))
    if numero % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print("\nQuantidade de números pares: ", par)
print("\nQuantidade de números impares: ", impar)
