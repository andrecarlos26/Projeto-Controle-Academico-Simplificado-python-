#Definir submenu da DISCIPLINA.
def disciplina():
     import os
#import os para limpar a tela.
     crud_disc = []
# Pause para melhorar a visualização dos prints.
     def pause():
          pause = input("Pressione ENTER para CONTINUAR   ")

# pede_codigo para pedir o codigo da disciplina.
     def pede_codigo():
          return(input("Codigo da disciplina: "))

# pede_nome para pedir o nome da disciplina.
     def pede_nome():
          return(input("Nome da disciplina: "))

# mostra_dados para printar os dados da disciplina (codigo e nome)
     def mostra_dados(codigo, nome):
          print("--------------------------------------------------------------------\nCodigo da disciplina: %s        Nome da disciplina: %s\n---------------------------------------------------------------------" % (codigo, nome))

# pesquisar disciplina através do codigo.
     def pesquisa(codigo):
          mcodigo = codigo.lower()
          for p, e in enumerate(crud_disc):
              if e[0].lower() == mcodigo:
                    return p
          return None

# Adicionar nova disciplina (codigo e nome)
     def novo():
          codigo = pede_codigo()
          nome = pede_nome()
          crud_disc.append([codigo, nome])

# Remover disciplina, pesquisando através do codigo. Se encontrado, será apagado.
     def apaga():
          codigo = pede_codigo()
          p = pesquisa(codigo)
          if p != None:
              del crud_disc[p]
              print("Disciplina excluida.")
              pause()

          else:
              print("Codigo nao encontrado.")
              pause()

# Alterar dados da disciplina, pesuisando através do codigo.
# Se encontrado, será alterado conforme a atualização dos dados feito pelo usuário.
     def altera():
          p = pesquisa(pede_codigo())
          if p != None:
              codigo = crud_disc[p][0]
              nome = crud_disc[p][1]
              print("Encontrado:")
              mostra_dados(codigo, nome)
              codigo = pede_codigo()
              nome = pede_nome()
              crud_disc[p] = [codigo, nome]
              pause()
          else:
              print("Codigo nao encontrado.")
              pause()

# Listar as disciplinas e seus dados e apresentá-los.
     def lista():
          print("\nDisciplina(s):\n\n---------------------------------------------------------------------")
          for e in crud_disc:
              mostra_dados(e[0], e[1])
          print("----------------------------------------------------------------------\n")
          pause()

# Ler o arquivo com os dados da disciplina.
     def le():
          try:
              codigo_arquivo = 'crud_dis.txt'
              arquivo = open(codigo_arquivo, "r", encoding = "utf-8")
              for l in arquivo.readlines():
                  codigo, nome = l.strip().split("#")
                  crud_disc.append([codigo, nome])
              arquivo.close()
          except:
              None


# Gravar os dados da disciplina.
# Grava automaticamente quando o numero 0 (zero) é digitado no menu principal.
     def grava():
          codigo_arquivo = 'crud_dis.txt'
          arquivo = open(codigo_arquivo, "w", encoding = "utf-8")
          for e in crud_disc:
              arquivo.write("%s#%s\n" % (e[0], e[1]))
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
    Disciplina:

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
        # Neste momento todos os dados da disciplina serão gravados.
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