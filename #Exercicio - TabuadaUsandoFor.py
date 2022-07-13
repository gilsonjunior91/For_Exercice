#Exercicio 12 - Estrutura de Repetição For

escolha = int(input("Digite o número da tabuada entre 1 e 10: "))
for n in range(1,11):
    print("[", escolha,"] X " "[", n, "]= ", escolha * n)