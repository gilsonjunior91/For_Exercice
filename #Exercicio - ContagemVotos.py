#Exercicio 26 - SIMULADOR DE CONTAGEM DE VOTOS
import os                 # COMANDO USADO PARA UTILIZAR CLS E PAUSE

limite = 99999            #CONDIÇÃO APENAS PARA EVITAR QUE UTILIZE UM VALOR MUITO ACIMA DO ESPERADO
print("\n\tELEIÇÕES FAJUTAS! \n")
eleitor1 = 0
eleitor2 = 0
eleitor3 = 0
eleitores = int(input("Digite a quantidade de eleitores: "))
if eleitores > 0 and eleitores < limite:
    for i in range(0,eleitores):
        print("[1]- Carochinha")
        print("[2]- Judas Perdeu as Botas")
        print("[3]- Chupa Prego até virar tarraxinha")
        op = int(input("Escolha o candidato: "))
        os.system("cls")
        if op == 1:
            eleitor1 += 1
        elif op == 2:
            eleitor2 += 1
        elif op == 3:
            eleitor3 += 1
        else:
            print("Candidato Inválido.")
    if eleitor1 > eleitor2 and eleitor3:
        print("\nO Eleitor 1 Ganhou! Ele(a) obteve: ", eleitor1, " votos.\n")
        os.system("pause")
    elif eleitor2 > eleitor1 and eleitor3:
        print("\nO Eleitor 2 Ganhou! Ele(a) obteve: ", eleitor2, " votos.\n")
        os.system("pause")
    elif eleitor3 > eleitor1 and eleitor2:
        print("\nO Eleitor 3 Ganhou! Ele(a) obteve: ", eleitor3, " votos.\n")
        os.system("pause")
    elif eleitor1 == eleitor2 and eleitor3:
        print(" Empate entre os 3 candidatos. Todos obtiveram ", eleitor1, " votos.")
        os.system("pause")
    elif eleitor1 == eleitor3:
        print(" Empate entre candidato 1 e 3. Ambos obtiveram ", eleitor3, " votos.")
        os.system("pause")
    elif eleitor2 == eleitor3:
        print(" Empate entre candidato 2 e 3. Ambos obtiveram ", eleitor2, " votos.")
        os.system("pause")
    else:
        print("Os candidatos não obtiveram votos válidos.")
        os.system("pause")
else:
    print("\n Eleições Encerradas!!!")
    os.system("pause")
