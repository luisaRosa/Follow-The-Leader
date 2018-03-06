# coding=utf-8
#Follow The Leader

from random import *
import random


T = 10 # seta as rodadas do jogo
m = 7 # número de ações, ou especialistas
l1= [(0.5,0), (0.1,1),(1,0)] # vetor de perdas


def inicialize_vector(vector):

	for t in xrange(T):
		vector.append([0] * m)
	return vector


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



def solve_problem():
	pt = [] # vetor de ações que são decididas com base nos valores das perdas anteriores
	l = []
	l = generate_instances()
	print 'oi',l

	
	# inicializa o vetor de ações
	for t in xrange(T):
		pt.append([0] * m)
	

	# Escolhe as ações baseadas no vetor de perdas em t-1
	for t in xrange(T):	

		if t >=1:	
			sum_min_t, index_t= minimize(l[:t]) # escolhe a ação minima no tempo t, com base no vetor de perdas t-1
			print "Vetor de perda t-1:",l[:t]
			print " Soma minima em t =", sum_min_t 
			pt[t][index_t] = 1 # seta o valor que minimiza a perda, baseado nas perdas ateriores

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


def minimize(lost_vector):

	temp =[]
	temp = [0]*m
	sum_min = 1000
	index_min = 0
	
	for i in xrange(len(lost_vector)):
		for j in xrange(m):
			aux = temp[j]
			temp[j] =  aux+ lost_vector[i][j]

	for i in xrange(m):
		if sum_min > temp[i]:
			sum_min = temp[i]
			index_min = i

	return sum_min, index_min






'''def minimize(lost_vector):
	
	# inicializa a soma e o índice mínimo
	sum_min = 100 
	index_min = 0
	sum_total = []

	# verifica qual é a menor perda anterior para poder realizar a ação

	if len(lost_vector)>1:

		for t in xrange(len(lost_vector)-1):

			lv_t = lost_vector[t] 
			lv_t1 = lost_vector[t+1]
			for i in xrange(m-1):

				#sum_total.apend(lost_vector[t][i]+lost_vector[])

				"""if aux == lista_t:
					if sum_min > lista_t[i]:
						sum_min = lista_t[i]
						index_min = i+1
				else:"""
				if (lv_t[i] + lv_t1[i])==(lv_t[i+1] + lv_t1[i+1]):
					
					if (sum_min+(lv_t[index_min] + lv_t1[index_min])) >  (lv_t[i] + lv_t1[i]):
						s_p = sum_min
						index_min_prev = index_min
						index_min = i if index_min_prev!=i else i+1
						sum_min= (lv_t[i] + lv_t1[i])+100					

				elif (lv_t[i] + lv_t1[i]) >(lv_t[i+1] + lv_t1[i+1]):
					if sum_min > lv_t[i+1] + lv_t1[i+1]:
						sum_min += lv_t[i+1] + lv_t1[i+1]
						index_min = i+1
				else:
					if sum_min >(lv_t[i] + lv_t1[i]):
						sum_min += (lv_t[i] + lv_t1[i])
						index_min = i
	else:
		
		for t in xrange(m):
			if sum_min > lost_vector[0][t]:
				sum_min = lost_vector[0][t]+100
				index_min = t
				
	return (float(sum_min - 100), index_min )
'''

if __name__ == '__main__':
	solve_problem()
	#generate_instances()


	# ajustar o organiziation para ele juntar as  das escolhas anteriores para poder somar com a atual -- ok!
	# calcular a perda total -- ok! 
	# ajustar a soma minima e comentar a função minimize -- ok!
	# gerar instancias aleatórias para testar o algoritmo -- ok!
	# implementar a minimização com Cplex
		# verificar a resposta com algumas instancias maiores
		# Otimizar o algoritmo o máximo possível
	
		