#Exercicio 27 - MÉDIA DE ALUNOS POR TURMAS
import os                   # COMANDO USADO PARA UTILIZAR O CLS E PAUSE

somaAlunos = 0
print("\n\t MÉDIA DE ALUNOS POR TURMA\n")
turmas = int(input("Digite a quantidade de turmas: "))
os.system("cls")
for i in range(0,turmas):
    if turmas > i:
        alunos = int(input("Digite a quantidade de alunos da turma: "))
        os.system("cls")
        if alunos <= 40:
            somaAlunos += alunos
        else:
            print("A turma não pode ter mais de 40 alunos.")
            os.system("pause")
            os.system("cls")
        
media = somaAlunos / turmas
print(" A média de alunos da turma: {:.2f} ".format(media))