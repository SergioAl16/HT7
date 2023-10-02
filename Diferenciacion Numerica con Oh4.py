# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Sergio Alejandro Vasquez Marroquin
21/09/2023

DIFERENCIACION NUMERICA CON SERIE DE TAYLOR con error de O(h^4)
"""

import numpy as np
import matplotlib.pyplot as plt

h = 0.01
x = np.arange((-3*np.pi)/2,(3*np.pi)/2,h)
y = x**2 * np.cos(x)

yprima = []
ybiprima = []
ytriprima = []
ycuatriprima = []
x_new = x[2:len(x)-2] # Si se quiere sacar la 4ta derivada necesito quitar los 3 valores del inicio y el final asi... x[3:len(x)-3]

for i in range(2,len(x)-2): # de igual forma en el rango range(3,len(x)-3)
    yprimai = (-y[i+2]+8*y[i+1]-8*y[i-1]+y[i-2])/(12*h)
    ybiprimai = (-y[i+2]+16*y[i+1]-30*y[i]+16*y[i-1]-y[i-2])/(12*h**2)
    #ytriprimai = (-y[i+3]+8*y[i+2]-13*y[i+1]+13*y[i-1]-8*y[i-2]+y[i-3])/(8*h**3)
    #ycuatriprimai = (-y[i+3]+12*y[i+2]+39*y[i+1]+56*y[i]-39*y[i-1]+12*y[i-2]+y[i-3])/(6*h**4)
    yprima.append(yprimai)
    ybiprima.append(ybiprimai)
    #ytriprima.append(ytriprimai)
    #ycuatriprima.append(ycuatriprimai)

# Encontrar extremos locales
extremos_locales = []
for i in range(2, len(x_new)-2):
    if yprima[i-2] > 0 and yprima[i-1] < 0 and yprima[i] < 0:
        extremos_locales.append((x_new[i], y[i]))
    elif yprima[i-2] < 0 and yprima[i-1] > 0 and yprima[i] > 0:
        extremos_locales.append((x_new[i], y[i]))

# Encontrar puntos de inflexión
puntos_inflexion = []
for i in range(2, len(x_new)-2):
    if ybiprima[i-2] > 0 and ybiprima[i-1] < 0 and ybiprima[i] < 0:
        puntos_inflexion.append((x_new[i], y[i]))
    elif ybiprima[i-2] < 0 and ybiprima[i-1] > 0 and ybiprima[i] > 0:
        puntos_inflexion.append((x_new[i], y[i]))

# Encontrar intervalos de crecimiento y decrecimiento
intervalos_crecimiento = []
intervalos_decrecimiento = []
for i in range(2, len(x_new)-2):
    if yprima[i-2] < 0 and yprima[i-1] > 0 and yprima[i] > 0:
        intervalos_crecimiento.append((x_new[i-2], x_new[i]))
    elif yprima[i-2] > 0 and yprima[i-1] < 0 and yprima[i] < 0:
        intervalos_decrecimiento.append((x_new[i-2], x_new[i]))

# Encontrar intervalos de concavidad
intervalos_concavidad_arriba = []
intervalos_concavidad_abajo = []
for i in range(2, len(x_new)-2):
    if ybiprima[i-2] > 0 and ybiprima[i-1] > 0 and ybiprima[i] > 0:
        intervalos_concavidad_arriba.append((x_new[i-2], x_new[i]))
    elif ybiprima[i-2] < 0 and ybiprima[i-1] < 0 and ybiprima[i] < 0:
        intervalos_concavidad_abajo.append((x_new[i-2], x_new[i]))

plt.plot(x, y, 'b', label='Función Original')
plt.plot(x_new, yprima, 'g', label='Primera Derivada')
plt.plot(x_new, ybiprima, 'm', label='Segunda Derivada')
#plt.plot(x_new, ytriprima, 'r', label='Tercera Derivada')
#plt.plot(x_new, ycuatriprima, 'y', label='Cuarta Derivada')

extremos_x, extremos_y = zip(*extremos_locales)
plt.scatter(extremos_x, extremos_y, color='red', marker='o', label='Extremos Locales')

inflexion_x, inflexion_y = zip(*puntos_inflexion)
plt.scatter(inflexion_x, inflexion_y, color='orange', marker='o', label='Puntos de Inflexión')

plt.title('Derivados y Puntos Relevantes')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

print("Extremos Locales:", extremos_locales)
print("Puntos de Inflexión:", puntos_inflexion)
print("Intervalos de Crecimiento:", intervalos_crecimiento)
print("Intervalos de Decrecimiento:", intervalos_decrecimiento)
# print("Intervalos de Concavidad hacia arriba:", intervalos_concavidad_arriba)
# print("Intervalos de Concavidad hacia abajo:", intervalos_concavidad_abajo)

# HT 7 - PROBLEMA 1
# x = np.arange((-3*np.pi)/2,(3*np.pi)/2,h)
# y = x**2 * np.cos(x)

