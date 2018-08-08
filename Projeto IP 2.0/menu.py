#MENU do programa
import os
#Acessa o submenu dos alunos
from crud_aluno import aluno
#Acessa o submenu das disciplinas
from crud_disc import disciplina
#Acessa o submenu dos professores
from crud_prof import professor
#Acessa o submenu das turmas
from crud_turma import turma
#from ata_exercicio import ata_de_exercicio
from gerar_ata import gerar_ata


#Validar os valores digitados para os submenus
def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return(valor)
        except ValueError:
            print("Valor invalido, favor digitar entre %d e %d" % (inicio, fim))

def menu():
    print("""
    MENU:

    1 - Aluno
    2 - Disciplina
    3 - Professor
    4 - Turma
    5 - Gerar ata de exercicios
    

    0 - Fechar
""")
    return valida_faixa_inteiro("Escolha uma opcao: ",0,5)
#valores para os submenus
while True:
#os.system para limpar a tela
    os.system('cls' if os.name == 'nt' else 'clear')
    opcao = menu()
    os.system('cls' if os.name == 'nt' else 'clear')
#Escolher a opção
    if opcao == 0:
        break
    elif opcao == 1:
        aluno()
    elif opcao == 2:
        disciplina()
    elif opcao == 3:
        professor()
    elif opcao == 4:
        turma()
    elif opcao == 5:
        gerar_ata()
    elif opcao == 0:
        break
            

