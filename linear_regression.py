import math
import matplotlib.pyplot as plt

def output(teta, x):
	return teta[1]*x+teta[0]

def gradient(teta,x,m,entrada,profit,alpha):
	tetanew = teta
	for j in range(0,len(teta)):
		summ = 0
		for k in range(0,m):
			summ = (output(teta,entrada[k])-profit[k])*x[k][j]
		tetanew[j] -= (alpha/m)*summ
	return tetanew

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
m = len(entrada)
iterations = 1500
alpha = 0.01
for i in range(0,iterations):
	teta = gradient(teta,x,m,entrada,profit,alpha)
out = []
for i in range(0,m):
	out.append(output(teta,entrada[i]))
plt.plot(entrada,profit,"*")
plt.plot(entrada,out)
plt.show()