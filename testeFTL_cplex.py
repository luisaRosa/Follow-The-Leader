#Follow the Leader with cplex
# coding=utf-8
import cplex
from cplex.exceptions import CplexError
import sys
from random import *
import random

T = 4
m = 2
# inicializa as listas com listas de tamanho m com zero's
def inicialize_vector(vector):

	for t in xrange(T):
		vector.append([0] * m)
	return vector

# gera as instancias das perdas para o problema
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

def populatebyrow(problem, lt):
	


	problem.objective.set_sense(problem.objective.sense.minimize)
	varnames = []
	lb =[]
	ub = []
	temp = [0]*m

	for i in xrange(len(lt)):
		for j in xrange(m):
			aux = temp[j]
			temp[j] =  aux+lt[i][j]
	print temp

	# nome das variáveis
	for j in xrange(m):
		varnames.append("p["+str(j)+"]")		

	# uper e lower bounds
	for t in xrange(m):
		lb.append(0.0)
		ub.append(1.0)

	problem.variables.add(obj=temp,lb=lb,ub=ub, names=varnames)
	linear_constraints = []
	rhs = []
	linear_constraints.append([varnames, ub])
	
	problem.linear_constraints.add(lin_expr=linear_constraints, rhs=[1.0], senses=["E"], names=["r1"])	
	

def follow_the_leader():

	problem = cplex.Cplex()
	lt = []
	lt = generate_instances() # vai ser os coeficientes da função objetivo
	print 'Instancia gerada:',lt
	
	
	# Escolhe as ações baseadas no vetor de perdas em t-1
	for t in range(1,T):	
			problem = cplex.Cplex()	
			handle = populatebyrow(problem, lt[:t]) # escolhe a ação minima no tempo t, com base no vetor de perdas t-1
			problem.solve()	

		
		
			solution = problem.solution
			print solution.status[solution.get_status()]
			print"Objective value = ", solution.get_objective_value()

			numrows = problem.linear_constraints.get_num()
			numcols = problem.variables.get_num() 
			print numcols, numrows
			slack =problem.solution.get_linear_slacks() 
			pi=problem.solution.get_dual_values() 
			x =problem.solution.get_values() 
			dj=problem.solution.get_reduced_costs() 
			for i in range(numrows): 
			  	print"Row %d: Slack = %10f Pi= %10f" % (i,slack[i],pi[i]) 
			for j in range(numcols):
			   	print "Column %d: Value = %10f Reduced cost = %10f" % (j,x[j],dj[j])

if __name__ == '__main__':
	follow_the_leader()

			