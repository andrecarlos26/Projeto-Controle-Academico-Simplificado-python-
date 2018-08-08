#Definir submenu ALUNO.
def aluno():
#import os para limpar a tela.
     import os
     crud_aluno = []

#Pause para melhorar a visualização dos prints.
     def pause():
          pause = input("Pressione ENTER para CONTINUAR   ")

#pede_cpf para pedir o cpf do aluno
     def pede_cpf():
          return(input("CPF do aluno: "))

#pede_nome para pedir o nome do aluno
     def pede_nome():
          return(input("Nome do aluno: "))

#mostra_dados para printar os dados do aluno (CPF e nome)
     def mostra_dados(cpf, nome):
          print("---------------------------------------------------------------------\nCPF do aluno: %s        Nome do aluno: %s\n---------------------------------------------------------------------" % (cpf, nome))


#pesquisar o aluno através do CPF.
     def pesquisa(cpf):
          mcpf = cpf.lower()
          for p, e in enumerate(crud_aluno):
              if e[0].lower() == mcpf:
                    return p
          return None

#Adicionar novo aluno (CPF e nome)
     def novo():
          cpf = pede_cpf()
          nome = pede_nome()
          crud_aluno.append([cpf, nome])

#Remover aluno, pesquisando através do CPF. Se encontrado, será apagado.
     def apaga():
          cpf = pede_cpf()
          p = pesquisa(cpf)
          if p != None:
              del crud_aluno[p]
              print("Aluno excluido.")
              pause()
          else:
              print("CPF nao encontrado.")

#Alterar dados do aluno, pesuisando através do CPF.
#Se encontrado, será alterado conforme a atualização dos dados feito pelo usuário.
     def altera():
          p = pesquisa(pede_cpf())
          if p != None:
              cpf = crud_aluno[p][0]
              nome = crud_aluno[p][1]
              print("Encontrado:")
              mostra_dados(cpf, nome)
              cpf = pede_cpf()
              nome = pede_nome()
              crud_aluno[p] = [cpf, nome]
              pause()
          else:
              print("CPF nao encontrado.")
              pause()

#Listar os alunos e seus dados e apresentá-los.
     def lista():
          print("\nAluno(s):\n\n---------------------------------------------------------------------")
          for e in crud_aluno:
              mostra_dados(e[0], e[1])
          print("---------------------------------------------------------------------\n")
          pause()

#Ler o arquivo com os dados do aluno.
     def le():
         try:
             nome_arquivo = 'crud_aluno.txt'
             arquivo = open(nome_arquivo, "r", encoding = "utf-8")
             for l in arquivo.readlines():
                 cpf, nome = l.strip().split("#")
                 crud_aluno.append([cpf, nome])
             arquivo.close()
         except:
             None

#Gravar os dados dos alunos.
#Grava automaticamente quando o numero 0 (zero) é digitado no menu principal.
     def grava():
          nome_arquivo = 'crud_aluno.txt'
          arquivo = open(nome_arquivo, "w", encoding = "utf-8")
          for e in crud_aluno:
              arquivo.write("%s#%s\n" % (e[0], e[1]))
          arquivo.close()

#Validar os valores digitados no MENU principal.
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
    Aluno:

    1 - Novo
    2 - Altera
    3 - Apaga
    4 - Lista

    0 - Voltar para o MENU
""")
          return valida_faixa_inteiro("Escolha uma opcao: ",0,4)

     le()
     while True:
         #os.system para limpar a tela.
          os.system('cls' if os.name == 'nt' else 'clear')
          opcao = menu()
          os.system('cls' if os.name == 'nt' else 'clear')
          if opcao == 0:
        #Neste momento todos os dados dos alunos serão gravados.
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
