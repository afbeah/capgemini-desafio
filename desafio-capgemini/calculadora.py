# importa o OS para limpar a tela posteriormente
import os

# inicilização da variável para entrar no laço While
investido = 1

# limpa a tela
os.system('cls') 

# repete enquanto o valor inserido não for 0
while (investido != 0):

	# lê do prompt convertendo para float
	investido = float(input("Insira o valor investido ou digite 0 para sair: "))

	# limpa a tela
	os.system('cls') 

	# verifica o valor inserido para calcular só quando necessário
	if investido != 0:

		# calculo das parciais para encontrar o alcance
		original = investido * 30
		cliques = original * (12/100)
		compart  = cliques * (3/20)
		novas_vis = compart * 40
		max_vis = novas_vis * 4

		# imprime o resultado
		print("O número máximo de visualizações é de aproximadamente: ", int(max_vis), "\n")
		
		# trava a tela para permitir a visualização do resultado
		input("Pressione qualquer tecla para continuar")
		
		# limpa a tela
		os.system('cls') 

# trava o programa antes de finalizar
input("Obrigado por usar a calculadora de alcance de anúncio \n Pressione qualquer tecla para finalizar")