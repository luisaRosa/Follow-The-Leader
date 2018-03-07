# coding=utf-8
#Follow The Leader - FTL

from random import *
import random



T = 10 # seta as rodadas do jogo
m = 7 # número de ações, ou especialistas
l1= [(0.5,0), (0.1,1),(1,0)] # vetor de perdas


# inicializa as listas com listas de tamanho m com zero's
def inicialize_vector(vector):

	for t in xrange(T):
		vector.append([0] * m)
	return vector

# gera instancias randômicas para o FTL
def generate_instances():

	l = []
	l = inicialize_vector(l)

	for i in xrange(T):
		for j in xrange(m):
			lost = uniform(0,1.1)
			if lost <=1:
				l[i][j] = lost
			else:
				l[i][j]= (uniform(0,1))
	return l


def follow_the_leader():
	pt = [] # vetor de ações que são decididas com base nos valores das perdas anteriores
	l = []
	l = generate_instances()
	print 'Instancia gerada:',l

	# inicializa o vetor de ações
	pt = inicialize_vector(pt)	

	# Escolhe as ações baseadas no vetor de perdas em t-1
	for t in xrange(T):	

		if t >=1:# verifica se já tem informações passadas para poder fazer a previsão	
			sum_min_t, index_t= minimize(l[:t]) # escolhe a ação minima no tempo t, com base no vetor de perdas t-1
			print "Vetor de perda t-1:",l[:t]
			print " Soma minima em t =", sum_min_t 
			pt[t][index_t] = 1 # seta o valor que minimiza a perda, baseado nas perdas ateriores

	# escolhe uma determinada ação randômica para p1
	rand = random.randint(0,m-1)
	print rand
	pt[0][rand] = 1

	print "Vetor de ações:",pt
	total_lost =0

    # calcula a perda total
	for t in xrange(T): 
		for i in xrange(m):
			if pt[t][i] == 1:
				total_lost+= l[t][i]
	print  'A perda total é: ',total_lost

# minimiza a a perda com base em t-1
def minimize(lost_vector):

	temp =[]
	temp = [0]*m
	sum_min = 1000
	index_min = 0

	# faz a soma dos indices de m a partir do vetor de perdas em t-1
	for i in xrange(len(lost_vector)):
		for j in xrange(m):
			aux = temp[j]
			temp[j] =  aux+ lost_vector[i][j]

	# identifica a soma mínima em t-1
	for i in xrange(m):
		if sum_min > temp[i]:
			sum_min = temp[i]
			index_min = i

	return sum_min, index_min


if __name__ == '__main__':
	follow_the_leader()
	#generate_instances()


	# ajustar o organiziation para ele juntar as  das escolhas anteriores para poder somar com a atual -- ok!
	# calcular a perda total -- ok! 
	# ajustar a soma minima e comentar a função minimize -- ok!
	# gerar instancias aleatórias para testar o algoritmo -- ok!
	# implementar a minimização com Cplex
		# verificar a resposta com algumas instancias maiores
		# Otimizar o algoritmo o máximo possível
	
		