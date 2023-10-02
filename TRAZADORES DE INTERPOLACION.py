# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Sergio Alejandro Vasquez Marroquin - 161259
20/07/2023

TRAZADORES DE INTERPOLACION
"""

from scipy.interpolate import CubicSpline, lagrange, interp1d
import numpy as np
import matplotlib.pyplot as plt
import random as rnd
from scipy.optimize import curve_fit

# Estos son los valores segun mi funcion en Excel
x = [1,1.5,1.6,2.5,3.5]
y = [0.6767,0.3734,0.3261,0.08422,0.01596]

# Esto lo utilizo cuando quiero valores aleatorios de x, y, pero cuando ya los tengo
# para aproximar algun valor, no es necesario
"""
for i in range(10):
    x.append(i)
    y.append(rnd.randint(-100,100))
    """

f = CubicSpline(x, y, bc_type='natural')
g = lagrange(x, y)
h = interp1d(x, y)


# Tengo que cambiar mi rango dependiendo de los datos mas grandes y pequeños de x, y
x_new = np.linspace(1, 3.5, 1000)

#"evaluo en el conjunto de x para hacer la grafica"
y_f = f(x_new)
y_g = g(x_new)
y_h = h(x_new)

y_f1 = f(x_new, 1)
y_f2 = f(x_new, 2)
y_f3 = f(x_new, 3)

plt.figure(figsize = (10,8))
plt.plot(x_new, y_f, 'b') #FUNCION
plt.plot(x_new, y_f1, 'g') #1ERA DERIVADA
plt.plot(x_new, y_f2, 'y') #2DA DERIVADA
#plt.plot(x_new, y_f3, 'm') #3RA DERIVADA

plt.plot(x_new, y_g, 'g')
plt.plot(x_new, y_h, 'y')
plt.plot(x, y, 'ro') #r es rojo y la o es q solo dibuja puntos
plt.title('Interpolate')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Evaluar la primera, segunda y tercera derivada en x = 1.6
x_eval = 1.6
y_f1_x = f(x_eval, 1)
y_f2_x = f(x_eval, 2)
y_f3_x = f(x_eval, 3)

# Imprimir los valores de las derivadas en x = 1.6
print(f'Primera derivada en x = {x_eval}: {y_f1_x}')
print(f'Segunda derivada en x = {x_eval}: {y_f2_x}')
print(f'Tercera derivada en x = {x_eval}: {y_f3_x}')

# Aqui dara los valores de la funcion de cada interpolacion
# print(f(3))
# print(g(3))
# print(h(3))

# Aqui evaluamos en las Primera y Segunda derivada los valores que querramos
# print (f(1.6, 1))
# print (f(1.6, 2))


# HT 7 - PROB4
# x = [1,1.5,1.6,2.5,3.5]
# y = [0.6767,0.3734,0.3261,0.08422,0.01596]

# Evaluar la primera, segunda y tercera derivada en x = 1.6
# x_eval = 1.6
# y_f1_x = f(x_eval, 1)
# y_f2_x = f(x_eval, 2)
# y_f3_x = f(x_eval, 3)