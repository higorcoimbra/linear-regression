import math
import matplotlib.pyplot as plt

def output(teta, x):
	h.append(teta[1]*x+teta[0])

def gradient(teta,x,m,entrada,profit,alpha):
	for i in range(0,len(teta)):
		summ = 0
		for k in range(0,m):
			summ = (output(teta,entrada[k])-profit[k])*x[i]
		teta[i] -= (alpha/m)*summ
	return teta

#leitura dos dados
file = open("ex1data1.txt")
entrada = []
x = []
profit = []
for line in file:
	x.append([1,float(line.split(",")[0])])
	entrada.append(float(line.split(",")[0]))
	profit.append(float(line.split(",")[1].replace("\n","")))
print(entrada)
teta = [1,2]
m = len(size_pop)
iterations = 1500
alpha = 0.01
for i in range(0,iterations):
	teta = gradient(teta,x,m,entrada,profit,alpha)
out = []
for i in range(0,m):
	out.append(output(teta,entrada[i]))
plt.plot(size_pop,profit,"*")
plt.plot(size_pop,)