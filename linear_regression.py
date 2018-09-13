import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y, c):
	return 0*x+0*y+c

def output(teta, x):
	return teta[1]*x+teta[0]

def calc_cost(teta,entrada,profit,m):
	summ = 0
	for i in range(0, m):
		summ += (output(teta,entrada[i])-profit[i])**2
	return summ/(2*m)	

def gradient(teta,x,m,entrada,profit,alpha):
	tetanew = teta
	for j in range(0,len(teta)):
		summ = 0
		for i in range(0,m):
			summ += (output(teta,entrada[i])-profit[i])*x[i][j]
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
teta = [0,0]
cost = []
tetas_0 = []
tetas_1 = []

m = len(entrada)
iterations = 10000
alpha = 0.001

for i in range(0,iterations):
	teta = gradient(teta,x,m,entrada,profit,alpha)
	tetas_0.append(teta[0])
	tetas_1.append(teta[1])	
	cost.append(calc_cost(teta,entrada,profit,m))

out = []
for i in range(0,m):
	out.append(output(teta,entrada[i]))
#fig = plt.figure()
#ax = fig.gca(projection='3d')

plt.figure(1)
plt.xlabel("Price")
plt.ylabel("Profit")
plt.plot(entrada,profit,"x", label="Real data")
plt.plot(entrada,out,label="Linear Regression")
plt.legend()

plt.figure(2)
plt.xlabel("Age")
plt.ylabel("Cost")
plt.plot(cost[0:100])

"""
X = np.array(tetas_0)
Y = np.array(tetas_1)

X,Y = np.meshgrid(X, Y)
Z = f(X, Y, np.array(cost))

surf = ax.plot_surface(X, Y, Z)
"""
"""
% Contour plot
figure;
% Plot J_vals as 15 contours spaced logarithmically between 0.01 and 100
contour(theta0_vals, theta1_vals, J_vals, logspace(-2, 3, 20))
xlabel('\theta_0'); ylabel('\theta_1');
hold on;
plot(theta(1), theta(2), 'rx', 'MarkerSize', 10, 'LineWidth', 2);
"""

plt.show()

