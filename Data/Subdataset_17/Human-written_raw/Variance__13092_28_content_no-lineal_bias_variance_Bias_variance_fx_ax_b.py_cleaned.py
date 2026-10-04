from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from numpy import arange, pi, sin
import random
import math
import os
experiments = 200
pendiente = []
interseccion = []
for i in range(experiments):
	x1 = random.uniform(-1, 1)
	x2 = random.uniform(-1, 1)
	y1 = sin(x1*pi)
	y2 = sin(x2*pi)
	m = (y2-y1)/(x2-x1)
	b = y1 - (m*x1)
	pendiente.append(m)
	interseccion.append(b)
t = arange(-1, 1.01, 0.01)
ft = sin(t*pi)
prom_pendiente = sum(pendiente)/len(pendiente)
prom_interseccion = sum(interseccion)/len(interseccion)
lista_bias = []
for elemento in t:
	bias_x = math.pow((prom_pendiente * elemento) + prom_interseccion - sin(elemento*pi), 2)
	lista_bias.append(bias_x)
pro_bias = sum(lista_bias)/len(lista_bias)
print('Bias = %f' % pro_bias)
recol_x = []
aux_lst = []
for i in range(len(t)):
	for j in range(experiments):
		aux = ((pendiente[j] - prom_pendiente)*t[i]) + (interseccion[j] - prom_interseccion)
		aux_lst.append(aux)
	recol_x.append(aux_lst)
	aux_lst = []
cuadrado = []
aux = []
for punto in recol_x:
	for recta in punto:
		cu = math.pow(recta, 2)
		aux.append(cu)
	cuadrado.append(aux)
	aux = []
sum_cuadrado = []
for punto in cuadrado:
	aux = sum(punto)/(len(punto)-1)
	sum_cuadrado.append(aux)
varian_med = sum(sum_cuadrado)/len(sum_cuadrado)
print('Variance: %f' %varian_med)
plt.plot(t, ft)
plt.grid(True)
plt.ylim(-2, 2)
plt.xlim(-1, 1)
for i in range(experiments):
	plt.plot(t, (pendiente[i]*t)+interseccion[i], alpha = 0.5, color = 'g')
plt.plot(t, (prom_pendiente*t)+prom_interseccion, alpha = 0.5, color = 'r', linewidth = 2)
plt.text(-0.9, 1.75, 'Bias: '+str(pro_bias))
plt.text(-0.9, 1.64, 'Variance: '+str(varian_med))
plt.savefig(os.path.join('Sinusoidal_dos.png'), dpi = 300, format = 'png', bbox_inches = 'tight')