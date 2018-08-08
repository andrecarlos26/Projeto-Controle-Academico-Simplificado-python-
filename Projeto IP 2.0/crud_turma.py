#Definir submenu TURMA.
def turma():
     import os
     crud_turma = []
     def pause():
# Pause para melhorar a visualização dos prints.
          pause = input("Pressione ENTER para CONTINUAR    ")

# pede_nome para pedir o nome do professor.
     def pede_cod_turma():
          return(input("Codigo da turma: "))

#pede_periodo para pedir o periodo
     def pede_periodo():
          return(input("Periodo: "))

#pede_cod_disciplina para pedir o codigo da disciplina.
     def pede_cod_desciplina():
          return(input("Codigo da disciplina: "))

#pede_cpf_prof para pedir o CPF do professor.
     def pede_cpf_prof():
          return(input("CPF do professor: "))

#pede_cpf_aluno para pedir o CPF do aluno.
     def pede_cpf_aluno():
          return(input("CPF do aluno: "))

# mostra_dados para printar os dados da turma.
#(codigo da turma e da disciplina, CPF dos alunos e dos professores, e o periodo).
     def mostra_dados(cod_turma, periodo, cod_disciplina, cpf_prof, cpf_aluno):
          print("---------------------------------------------------------------------\nCodigo da turma: %s\nPeriodo: %s\nCodigo da disciplina: %s\n" % (cod_turma, periodo, cod_disciplina))
          print()
          print("CPF do(s) professor(es):")
          for i in cpf_prof:
               print(i)
          print()
          print("CPF do(s) aluno(s):")
          for i in cpf_aluno:
               print(i)
          print("---------------------------------------------------------------------")

# pesquisar a turma através do codigo da turma.
     def pesquisa(cod_turma):
          mcod_turma = cod_turma.lower()
          for p, e in enumerate(crud_turma):
              if e[0].lower() == mcod_turma:
                    return p
          return None

#Adicionar nova turma.
#(codigo da turma e da disciplina, CPF dos alunos e dos professores, e o periodo).
     def novo():
          cod_turma = pede_cod_turma()
          periodo = pede_periodo()
          cod_disciplina = pede_cod_desciplina()
          cpf_prof = []
          print('Digite o CPF do professor ou pressione 0 (zero) para sair.')
          while True:
               cpfpro = pede_cpf_prof()
               if cpfpro=='0':
                    break
               else:
                    cpf_prof.append(cpfpro)
          
          cpf_aluno = []
          print('Digite o CPF do aluno ou pressione 0 (zero) para sair.')
          while True:
               cpfalun = pede_cpf_aluno()
               if cpfalun=='0':
                    break
               else:
                    cpf_aluno.append(cpfalun)
          crud_turma.append([cod_turma, periodo, cod_disciplina, cpf_prof, cpf_aluno])

# Remover turma, pesquisando através do codigo. Se encontrada, será apagada.
     def apaga():
          cod_turma = pede_cod_turma()
          p = pesquisa(cod_turma)
          if p != None:
              del crud_turma[p]
              print("Turma excluida.")
              pause()
          else:
              print("Codigo nao encontrado.")
              pause()

# Alterar dados da turma, pesuisando através do codigo.
# Se encontrado, será alterado conforme a atualização dos dados feito pelo usuário.
     def altera():
          p = pesquisa(pede_cod_turma())
          if p != None:
              cod_turma = crud_turma[p][0]
              periodo = crud_turma[p][1]
              cod_disciplina = crud_turma[p][2]
              cpf_prof = crud_turma[p][3]
              cpf_aluno = crud_turma[p][4]
              print("Encontrado:")
              mostra_dados(cod_turma, periodo, cod_disciplina, cpf_prof, cpf_aluno)
              cod_turma = pede_cod_turma()
              periodo = pede_periodo()
              cod_disciplina = pede_cod_desciplina()
              cpf_prof = pede_cod_desciplina()
              cpf_aluno = pede_cpf_aluno()
              crud_turma[p] = [cod_turma, periodo, cod_disciplina, cpf_prof, cpf_aluno]
              pause()
          else:
              print("CPF nao encontrado.")
              pause()

# Listar as turmas e seus dados e apresentá-los.
     def lista():
          print("\nTurma:\n\n---------------------------------------------------------------------")
          for e in crud_turma:
              mostra_dados(e[0], e[1], e[2], e[3], e[4])
          print("---------------------------------------------------------------------\n")
          pause()

## Ler o arquivo com os dados da turma.
     def le():
         try:
             nome_arquivo = 'crud_turma.txt'
             arquivo = open(nome_arquivo, "r", encoding = "utf-8")
             for l in arquivo.readlines():
                 cod_turma, periodo, cod_disciplina, cpf_prof, cpf_aluno = l.strip().split("#")
                 cpf_prof = cpf_prof.replace('[', '').replace(']', '').replace("'", '')
                 cpf_prof = cpf_prof.split(', ')
                 cpf_aluno = cpf_aluno.replace('[', '').replace(']', '').replace("'", '')
                 cpf_aluno = cpf_aluno.split(', ')
                 crud_turma.append([cod_turma, periodo, cod_disciplina, cpf_prof, cpf_aluno])
             arquivo.close()
         except:
             None

# Gravar os dados da turma.
# Grava automaticamente quando o numero 0 (zero) é digitado no menu principal.
     def grava():
          nome_arquivo = 'crud_turma.txt'
          arquivo = open(nome_arquivo, "w", encoding = "utf-8")
          for e in crud_turma:
              arquivo.write("%s#%s#%s#%s#%s\n" % (e[0], e[1], e[2], e[3], e[4]))
          arquivo.close()

# Validar os valores digitados no MENU principal.
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
    Turma:

    1 - Novo
    2 - Altera
    3 - Apaga
    4 - Lista

    0 - Voltar para o MENU
""")
          return valida_faixa_inteiro("Escolha uma opcao: ",0,4)

     le()
     while True:
         # os.system para limpar a tela.
          os.system('cls' if os.name == 'nt' else 'clear')
          opcao = menu()
          os.system('cls' if os.name == 'nt' else 'clear')
          if opcao == 0:
        # Neste momento todos os dados da turma serão gravados.
              grava()
              break
          elif opcao == 1:
              novo()
          elif opcao == 2:
              altera()
          elif opcao == 3:
              apaga()
          elif opcao == 4:
              lista()