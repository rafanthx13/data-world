# algoritmo_genetico.py

from random import random
import matplotlib.pyplot as plt
import pymysql

# Problema
#	Resolver problema de encontara ausi produtos com um conjunto de valores
#	X e tamanho Y devem ser colocados de num caminhao limitado de forma a te
#	o melhor resultado possivel

# Passo a Passo do Algoritmo Genetico
#	1. Gerar população Inicial
#	2. Calcular fitnesse de cada inidviduo (aptidao, avaliaçâo)
#	3. Loop
#		3.1 Se atingiu população N ou encontrou opçâo otima?
#			3.1.2 Stop! Lista o Melhor inidividuo
#		3.2 Seleciona os pais (Seleção)
#		3.3 Faz Cruzamento (Crossover)
#		3.4 Faz mutação (Mutação)
#		3.5 Calucla Fintiness
#		3.6 Redefini nova populaçâo n+1 (Reinserçâo)
#		3.7 Descarta populaçâo anterior

# Definindo o objeto Produto ()
class Produto():

	# Metodo construtor
	def __init__(self, nome, espaco, valor):
		self.nome = nome
		self.espaco = espaco
		self.valor = valor

# Definido Indivíduo
#	+ Se não usásemos classe, teriamos que entao agrupar esse valores em
#		outra esttutura, como um dicionario. Para cada inidividuo ter essa
#		coleçâo de dados
class Individuo():

	def __init__(self, espacos, valores, limite_espacos, geracao = 0):
		self.espacos = espacos
		self.valores = valores
		self.limite_espacos = limite_espacos
		self.espaco_usado = 0
		self.nota_avaliacao = 0
		self.geracao = geracao
		self.cromossomo = []
		# Aqui defini o Cromossomo uma lista binaria
		for i in range(len(espacos)):
			if random() < 0.5:
				self.cromossomo.append("0")
			else:
				self.cromossomo.append("1")

	# Função de Avaliação
	def avaliacao(self):
		nota = 0
		soma_espacos = 0
		for i in range(len(self.cromossomo)):
			if(self.cromossomo[i] == '1'):
				nota += self.valores[i]
				soma_espacos += self.espacos[i]
		# Caso tiver passado o limite, envez de o desqualificálo
		# Vamos por uma nota baixa para ele
		if(soma_espacos > self.limite_espacos):
			nota = 1
		self.nota_avaliacao = nota
		self.espaco_usado = soma_espacos

	def crossover(self, outro_individuo):
		# Definimos a parte que vai fazer o curte, vai ser apartir de um valor random [0,1]
		# Pode ser algo que produza inteiros num intervalo
		sec_cut = round(random()  * len(self.cromossomo))

		cromo_filho1 = outro_individuo.cromossomo[0:sec_cut] + self.cromossomo[sec_cut::]
		cromo_filho2 = self.cromossomo[0:sec_cut] + outro_individuo.cromossomo[sec_cut::]

		filhos = [Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1),
		      Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1)]
		
		# Inserindo cromossomos nos novos inidivudos gerados, filhos
		filhos[0].cromossomo = cromo_filho1
		filhos[1].cromossomo = cromo_filho2
		return filhos

	# Mutação: Para todo gene, colocar gerr um valor random, se for menor que a
	# taxa passada como param, muda ele
	def mutacao(self, taxa_mutacao):
		#print("Antes %s " % self.cromossomo)
		for i in range(len(self.cromossomo)):
			if(random() < taxa_mutacao):
				if(self.cromossomo[i] == '1'):
					self.cromossomo[i] = '0'
				else:
					self.cromossomo[i] = '1'
		#print("Depois %s " % self.cromossomo)
		return self


class AlgoritmoGenetico():

	def __init__(self, tamanho_populacao):
		self.tamanho_populacao = tamanho_populacao
		self.populacao = []
		self.geracao = 0
		self.melhor_solucao = 0 # Quem tem a maior nota, e por colocarmos 1 quando passa do limeite, nao vai ser um que tem amsi espaço
		self.lista_solucoes = [] 

	# Gerar a População
	def inicializa_populacao(self, espacos, valores, limite_espacos):
		for i in range(self.tamanho_populacao):
			self.populacao.append(Individuo(espacos, valores, limite_espacos))
		self.melhor_solucao = self.populacao[0] # Por enquanto, ao criar, nos colocamos que começa sendo o primeiro como melhor fitness, isso sera mudadao posteriormente

	# avaliar a população
	def ordena_populacao(self):
		# Iremos ordenar a lista pela nota_avaliacao, reverse = Ture => descendente
		self.populacao = sorted(self.populacao,
		 key = lambda populacao: populacao.nota_avaliacao, reverse = True)

	# Na forma que é utilizadao, ele comprar o atual melhor individuo com um outro possivel
	# Que sera o primeiro da lista ordenada de outra geração
	def melhor_individuo(self, individuo):
		if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
			self.melhor_solucao = individuo

	# Seu objetivo é para fazer a seleçâo dos inidivduos que fazremos posteriormente
	# Colcalula a soma de todas as avaliaçôes de uma população
	# Será usado para definir a Roleta e a prorpoção dos fitness
	def soma_avaliacoes(self):
		soma = 0
		for individuo in self.populacao:
			soma += individuo.nota_avaliacao
		return soma

	# Metodo Roleta Viciada: Irá Selecionar o Index de um pai selecionado
	# 	Observe que ele representa essa roleta a partir de uma Somatoria Acumulada
	# 	Quando a soma alcançar um limite, é entao escolhido
	# 	Particulamente não gostei dessa forma, pelo menos não capaz de confiar que ela dárá certo mesmo
	#		Percebi que funciona sim, so que, no caso, nao é uma roleta
	#		Imagina uma fita divida em cores e cada cor emgloba random dela toda
	#		Ao escolher valores random dela, quem tiver mais espaço tera mais chances
	#		Doq eu quem não tem tanto, ainda assim, pode ser selecionada
	# OBS: 
	# soma_avaliaco => funtcion soma_avaliacoes
	def seleciona_pai(self, soma_avaliacao):
		pai = -1 # de inicio, nao escolhe nenhum
		# sorteia de [0,1] e multiplica pela soma, asism temos uma faixa total
		valor_sorteado = random() * soma_avaliacao 
		soma = 0
		i = 0 # i é o indice, no caso, ira de 1 até 14
		while(i < len(self.populacao) and soma < valor_sorteado):
			soma += self.populacao[i].nota_avaliacao
			pai += 1
			i += 1
		return pai # retorna o inidice, de [0,14]

	# Serve para mostrar o melhor individuo da atual geraçâo
	def visualiza_geracao(self):
		melhor = self.populacao[0]
		print("G:%s -> Valor: %s Espaço: %s Cromossomo: %s" % (self.populacao[0].geracao,
			melhor.nota_avaliacao,
			melhor.espaco_usado,
			melhor.cromossomo))

	def resolver(self, taxa_mutacao, numero_geracoes, espacos, valores, limite_espacos):
		# Inicializa População Inicial
		self.inicializa_populacao(espacos, valores, limite_espacos)

		# Calcula o Fitness de Cada Indivíduo
		for individuo in self.populacao:
			individuo.avaliacao()

		# Identifica melhor individuo e o poe na lista de soluções
		self.ordena_populacao()
		self.melhor_solucao = self.populacao[0]
		self.lista_solucoes.append(self.melhor_solucao.nota_avaliacao)
		self.visualiza_geracao()

		# Passagem das Gerações
		for geracao in range(numero_geracoes):
			nova_populacao = []

			# Valor para o calculo da Roletoa
			soma_avaliacao = self.soma_avaliacoes()
			
			# Operações Genéticas
			for individuos_gerados in range(0, self.tamanho_populacao, 2):
				# Operação de Seleção
				pai1 = self.seleciona_pai(soma_avaliacao)
				pai2 = self.seleciona_pai(soma_avaliacao)
				# Crossoover
				filhos = self.populacao[pai1].crossover(self.populacao[pai2])
				# Adicionando os novos filhas a nova população
				nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
				nova_populacao.append(filhos[1].mutacao(taxa_mutacao))
			# Reinserçâo, deleta a anteiror e sobreescreve pela nova
			self.populacao = list(nova_populacao)

			# Agora vaos reclacular o fitnesse e descobrir a maelhor solução
			# Calculo de Fitness
			for individuo in self.populacao:
				individuo.avaliacao()

			self.ordena_populacao()
			self.visualiza_geracao()

			melhor = self.populacao[0]
			self.lista_solucoes.append(melhor.nota_avaliacao)
			# No Final de tudo, oesse sera executado e vai buscar o mehlor de todos e por em melhor_solucao
			self.melhor_individuo(melhor)

		print("\nMelhor solução -> G: %s Valor: %s Espaço: %s Cromossomo: %s" %
			(self.melhor_solucao.geracao,
			self.melhor_solucao.nota_avaliacao,
			self.melhor_solucao.espaco_usado,
			self.melhor_solucao.cromossomo))
		return self.melhor_solucao.cromossomo

		

if __name__ == '__main__':
	lista_produtos = []

	# conexao = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='AG_List_Products')
	# cursor = conexao.cursor()
	# cursor.execute('select nome, espaco, valor, quantidade from produtos')
	# for produto in cursor:
	# 	# Cada produto tem uma lista na ordme indicada
	# 	for i in range(produto[3]): # vai percorre na quantidade, fazemos isso para que, a quantidade duplique os itens, para que o cromossomo respeita [1,0]
	# 		lista_produtos.append(Produto(produto[0], produto[1], produto[2]))

	# cursor.close()
	# conexao.close()


	lista_produtos.append(Produto("Geladeira Dako", 0.751, 999.90))
	lista_produtos.append(Produto("Iphone 6", 0.0000899, 2911.12))
	lista_produtos.append(Produto("TV 55' ", 0.400, 4346.99))
	lista_produtos.append(Produto("TV 50' ", 0.290, 3999.90))
	lista_produtos.append(Produto("TV 42' ", 0.200, 2999.00))
	lista_produtos.append(Produto("Notebook Dell", 0.00350, 2499.90))
	lista_produtos.append(Produto("Ventilador Panasonic", 0.496, 199.90))
	lista_produtos.append(Produto("Microondas Electrolux", 0.0424, 308.66))
	lista_produtos.append(Produto("Microondas LG", 0.0544, 429.90))
	lista_produtos.append(Produto("Microondas Panasonic", 0.0319, 299.29))
	lista_produtos.append(Produto("Geladeira Brastemp", 0.635, 849.00))
	lista_produtos.append(Produto("Geladeira Consul", 0.870, 1199.89))
	lista_produtos.append(Produto("Notebook Lenovo", 0.498, 1999.90))
	lista_produtos.append(Produto("Notebook Asus", 0.527, 3999.00))

	espacos = []
	valores = []
	nomes = []
	for produto in lista_produtos:
		espacos.append(produto.espaco)
		valores.append(produto.valor)
		nomes.append(produto.nome)
	limite = 10 # limite do caminhao
	tamanho_populacao = 20
	taxa_mutacao = 0.01
	numero_geracoes = 100
	ag = AlgoritmoGenetico(tamanho_populacao)
	resultado = ag.resolver(taxa_mutacao, numero_geracoes, espacos, valores, limite)
	for i in range(len(lista_produtos)):
		if resultado[i] == '1':
			print("Nome: %s R$ %s " % (lista_produtos[i].nome, lista_produtos[i].valor), flush = True)
	#for valor in ag.lista_solucoes:	
	#	print(valor)
	plt.plot(ag.lista_solucoes)
	plt.title("Acompanhamento dos valores")
	plt.show()
    