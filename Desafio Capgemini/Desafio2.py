# importa o OS para limpar a tela posteriormente
import os

# inicilização das variáveis
anuncios = [[],[]]
menu_principal = 1
j = 0

# limpa a tela
os.system('cls')

# cria uma repetição do menu principal
while (menu_principal != 3):

  print("Escolha a opção desejada \n")
  print("1 - Inserir novo anúncio \n")
  print("2 - Filtrar e exibir anúncio \n")
  print("3 - Sair \n")

  # recebe a opção do menu principal
  menu_principal = int(input())

  # limpa a tela
  os.system('cls')

  # se a opção escolhida for a de inserir novo anúncio
  if menu_principal == 1:

    # entrada dos dados
    nome = input("Nome do anúncio \n")
    cliente = input("Nome do cliente \n")
    dataInicio = input("Data de início (aaaammdd) \n")
    dataFim = input("Data de término (aaaammdd) \n")
    investido = float(input("Valor investido por dia \n"))

    #limpa a tela
    os.system('cls')

    # calculo das parciais para encontrar o alcance
    original = investido * 30
    cliques = original * (12/100)
    compart  = cliques * (3/20)
    novas_vis = compart * 40
    max_vis = novas_vis * 4

    # insere os dados no array
    anuncios[j] = [nome, cliente, dataInicio, dataFim, investido, int(original), int(cliques), int(compart), int(novas_vis), int(max_vis)]

    # incrementa contador
    j+=1


  # se a opção escolhida for a de filtrar dados para exibir anúncios
  elif menu_principal == 2:

    # Entrada dos dados
    print("Por qual campo deseja buscar? \n")
    print("1 - Intervalo de tempo \n")
    print("2 - Cliente \n")

    tipoFiltro = int(input())
    
    # verificar qual dados será o filtro
    if (tipoFiltro == 1):

      dataInicio = int(input("Insira a data de inicio (aaaammdd) \n"))
      dataFim = int(input("Insira a data de término (aaaammdd) \n"))

      i = 0

      # varre o array e compara com os dados inseridos
      while (i < j):
        if (int(anuncios[i][2]) >= dataInicio and int(anuncios[i][3]) <= dataFim):

          print("Nome do anúncio: ", anuncios[i][0], " ")
          print("Nome do cliente: ", anuncios[i][1], " ")
          print("Valor total investido: ", anuncios[i][4], " ")
          print("Quantidade máxima de visualizações: ", anuncios[i][9], " ")
          print("Quantidade máxima de cliques: ", anuncios[i][7], " ")
          print("Quantidade máxima de compartilhamentos: ", anuncios[i][8], "\n")

          print("\n\n")

        i+=1

    elif (tipoFiltro == 2):

      cliente = input("Insira o nome do cliente \n")

      i = 0

      # varre o array e compara com os dados inseridos
      while (i < j):
        if (anuncios[i][1] == cliente):

          print("Nome do anúncio: ", anuncios[i][0], " ")
          print("Nome do cliente: ", anuncios[i][1], " ")
          print("Valor total investido: ", anuncios[i][4], " ")
          print("Quantidade máxima de visualizações: ", anuncios[i][9], " ")
          print("Quantidade máxima de cliques: ", anuncios[i][7], " ")
          print("Quantidade máxima de compartilhamentos: ", anuncios[i][8], "\n")  

          print("\n\n")

        i+=1

  else:

    # trava o programa antes de finalizar
    input("Obrigado por usar a calculadora de alcance de anúncio \n Pressione qualquer tecla para finalizar") 