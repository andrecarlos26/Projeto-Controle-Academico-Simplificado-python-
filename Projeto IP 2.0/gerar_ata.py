#Definir submenu para GERAR A ATA DE EXERCICIO.
def gerar_ata():

#import os para limpar a tela.
    import os

#pause para melhorar a visualização do print.
    def pause():
        pause = input("Pressione ENTER para CONTINUAR    ")

#pedir o codigo da disciplina para gerar a ata de exercicio.
    def pede_cod_disc():
        return (input("Codigo da disciplina: "))


    cod_disci = pede_cod_disc()
    print()
    print()
    print()
    pause()
    encontrado = False
#os.system para limpar a tela.
    os.system('cls' if os.name == 'nt' else 'clear')
#abrir o arquivo com as disciplinas.
    arquivo = open('crud_dis.txt', "r", encoding="utf-8")
    for i in arquivo.readlines():
        codigo_disc, nome_disc = i.strip().split('#')
#pesquisar se o codigo digitado confere com o codigo de alguma disciplina previamente armazenada.
        if cod_disci == codigo_disc:
#armazenar o nome da disciplina.
            nome_disciplina = nome_disc
            encontrado = True
            break
    arquivo.close()

#Se caso não for encontrado, será a presentadp a mensagem: Codigo Incorreto!
    if not encontrado:
        print('Codigo Incorreto!')
        print()
        print()
        print()
        pause()


    else:
        encontrado = False

        cpf_alunos = ''
        nome_alunos = ''
#Se encontrado, abrir o arquivo com os dados da turma.
        arquivo = open('crud_turma.txt', "r", encoding="utf-8")
        for i in arquivo.readlines():
            cod_turma, periodo, cod_disciplina, cpf_prof, cpf_aluno = i.strip().split("#")
# pesquisar se o codigo digitado confere com o codigo de alguma disciplina previamente armazenada.
            if cod_disci == cod_disciplina:
#Armazenar os dados da turma.
                lista_cpf_aluno =  cpf_aluno.replace('[', '').replace(']', '').replace("'", '').split(', ')
                encontrado = True
                break
        arquivo.close()

#Se caso encontrar a disciplina, mas não encontrar nenhuma turma com essa disciplina.
#Apresentar a mensagem: Nao ha turmas com essa disciplina.
        if not encontrado:
            print(nome_disciplina)
            print('Nao ha turmas com essa disciplina.')
            print()
            print()
            print()
            pause()

        else:
#Se encontrar todos os dados, apresenta-los.
            print('Codigo da Disciplina: %s' % cod_disci)
            print('Nome da Diciplina: %s' % nome_disciplina)
            print()
            print('Codigo da Turma: %s' % cod_turma)
            print()
            print('Periodo: %s' % periodo)
            print()
            print('Alunos:')

            arquivo = open('crud_aluno.txt', "r", encoding="utf-8")
            for i in arquivo.readlines():
                cpf, nome = i.strip().split("#")
                if cpf in lista_cpf_aluno:
                    print('%s   %s' %(cpf, nome))

            print()
            print()
            print()
            print()

            pause()


