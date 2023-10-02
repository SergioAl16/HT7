# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Sergio Alejandro Vasquez Marroquin
21/09/2023

DIFERENCIACION NUMERICA CON SERIE DE TAYLOR O(h^2)
"""

import numpy as np
import matplotlib.pyplot as plt

h = 0.006
x = [0,0.006,0.012,0.018,0.024]
y = [0,0.899,1.915,3.048,4.299]

yprima = []
ybiprima = []
ytriprima = []
x_new = x[2:len(x)-2]

for i in range(2,len(x)-2):
    yprimai = (y[i+1]-y[i-1])/(2*h)
    ybiprimai = (y[i+1]-2*y[i]+y[i-1])/(h**2)
    ytriprimai = (y[i+2]-2*y[i+1]+2*y[i-1]-y[i-2])/(2*h**3)
    yprima.append(yprimai)
    ybiprima.append(ybiprimai)
    ytriprima.append(ytriprimai)

# Imprimir el tercer elemento de yprima y ybiprima

# Para identificar el numero de los valores en las listas son asi...
# Como eliminamos los dos primeros y los 2 ultimos por "range(2,len(x)-2)"
# [0,0,1,2,3,4,5,6,0,0]
indice_evaluado = 2  # Cambia este valor al índice que desees evaluar

# Imprimir el valor de la primera derivada en el índice seleccionado
print(f'Valor de la primera derivada en el índice {indice_evaluado}: {yprima[indice_evaluado - 2]}')

# Imprimir el valor de la segunda derivada en el índice seleccionado
print(f'Valor de la segunda derivada en el índice {indice_evaluado}: {ybiprima[indice_evaluado - 2]}')

plt.plot(x, y, 'b', label='Desplazamiento') # 'Función Original'
# plt.plot(x_new, yprima, 'g', label='Velocidad') # 'Primera Derivada'
# plt.plot(x_new, ybiprima, 'm', label='Aceleracion') # 'Segunda Derivada'
# plt.plot(x_new, ytriprima, 'y', label='Tercera Derivada') # 'Tercera Derivada'

plt.title('Funcion y Derivadas')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


# 1ER EJERCICIO EN CLASE
# x = np.arange(-5,5,h)
# y = np.sin(x) 

# 2DO EJERCICIO EN CLASE
# x = np.arange(1,10,h)
# y = np.sin(x-np.exp(x))/np.arctan(x)

# 3ER EJERCICIO EN CLASE
# x = np.arange(0.01,2,h)
# y = np.log(x**2) / (x**3) #Aqui log es logaritmo natural supuestamente xd

# 4ER EJERCICIO EN CLASE
# x = np.arange(-2, 5, h)
# y = np.cosh(x**2 - 1) / (1 - np.exp(x))

# HT7 PROBLEMA 2
# h = 4
# x = [0,4,8,12,16,20,24,28,32,36]
# y = [0,34.7,61.8,82.8,99.2,112.9,121.9,129.7,135.7,140.4]

# indice_tercero = 4  # El tercer elemento tiene índice 4
# print(f"yprima en su número de lista 4: {yprima[indice_tercero]}")
# print(f"ybiprima en su número de lista 4: {ybiprima[indice_tercero]}")

