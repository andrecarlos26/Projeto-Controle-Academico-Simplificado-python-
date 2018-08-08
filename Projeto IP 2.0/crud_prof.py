#Definir submenu PROFESSOR.
def professor():
     import os
     crud_prof = []
     def pause():
# Pause para melhorar a visualização dos prints.
          pause = input("Pressione ENTER para CONTINUAR   ")

# pede_nome para pedir o nome do professor.
     def pede_nome():
          return(input("Professor: "))

# pede_cpf para pedir o cpf do professor
     def pede_cpf():
          return(input("CPF: "))

#pede_departamento para pedir o departamento do professor.
     def pede_departamento():
          return(input("Departamento: "))

# mostra_dados para printar os dados do professor (CPF, nome e departamento).
     def mostra_dados(nome, cpf, departamento):
          print("---------------------------------------------------------------------\nNome: %s\nCPF: %s\nDepartamento: %s\n---------------------------------------------------------------------" % (nome, cpf, departamento))

# pesquisar o professor através do CPF.
     def pesquisa(cpf):
          mcpf = cpf.lower()
          for p, e in enumerate(crud_prof):
              if e[1].lower() == mcpf:
                    return p
          return None

# Adicionar novo professor (CPF, nome e departamento).
     def novo():
          nome = pede_nome()
          cpf = pede_cpf()
          departamento = pede_departamento()
          crud_prof.append([nome, cpf, departamento])

# Remover professor, pesquisando através do CPF. Se encontrado, será apagado.
     def apaga():
          cpf = pede_cpf()
          p = pesquisa(cpf)
          if p != None:
              del crud_prof[p]
              print("Professor excluido.")
              pause()

          else:
              print("CPF nao encontrado.")
              pause()

# Alterar dados do professor, pesuisando através do CPF.
# Se encontrado, será alterado conforme a atualização dos dados feito pelo usuário.
     def altera():
          p = pesquisa(pede_cpf())
          if p != None:
              nome = crud_prof[p][0]
              cpf = crud_prof[p][1]
              departamento = crud_prof [p][2]
              print("Encontrado:")
              mostra_dados(nome, cpf, departamento)
              nome = pede_nome()
              cpf = pede_cpf()
              departamento = pede_departamento()
              agenda[p] = [nome, cpf, departamento]
              pause()
          else:
              print("Professor nao encontrado.")
              pause()

# Listar os professores e seus dados e apresentá-los.
     def lista():
          print("\nProfessor:\n\n---------------------------------------------------------------------")
          for e in crud_prof:
              mostra_dados(e[0], e[1], e[2])
          print("---------------------------------------------------------------------\n")
          pause()

# Ler o arquivo com os dados do professor.
     def le():
         try:
             nome_arquivo = 'crud_prof.txt'
             arquivo = open(nome_arquivo, "r", encoding = "utf-8")
             for l in arquivo.readlines():
                 nome,cpf, departamento = l.strip().split("#")
                 crud_prof.append([nome, cpf, departamento])
             arquivo.close()
             pause()
         except:
             None

# Gravar os dados dos professores.
# Grava automaticamente quando o numero 0 (zero) é digitado no menu principal.
     def grava():
          nome_arquivo = 'crud_prof.txt'
          arquivo = open(nome_arquivo, "w", encoding = "utf-8")
          for e in crud_prof:
              arquivo.write("%s#%s#%s\n" % (e[0], e[1], e[2]))
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
    Professor:
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
        # Neste momento todos os dados dos alunos serão gravados.
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
