# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 21:21:47 2021

@author: Renan
"""

import numpy as np
import matplotlib.pyplot as plt


n_pares = 200
data_1 = np.array(([13, 8, 10, 15, 12, 9, 6, 4, 7, 11, 14, 10,
                    7, 9, 12, 13, 8, 11, 9, 12, 15, 11, 8, 6, 16]))

data_2 = np.array(([21, 24, 16, 12, 15, 5, 28, 20, 31, 25, 20, 24,
                    16, 19, 10, 17, 13, 22, 18, 39, 30, 24, 16, 19, 17, 15]))
#Exercício 1
frac_def = data_1 / n_pares

LM = sum(frac_def) / len(frac_def)
LSC = LM + 3 * ((LM * (1 - LM) / n_pares) ** (1 / 2))
LIC = LM - 3 * ((LM * (1 - LM) / n_pares) ** (1 / 2))
y_data = frac_def
y_label = 'fração defeituosa'
legend = 'Figura 1: Número de pares defeituosos.'

#Exercício 2
# LM = sum(data_2) / len(data_2)
# LSC = LM + 3 * (LM ** (1 / 2))
# LIC = LM - 3 * (LM ** (1 / 2))
# y_data = data_2
# y_label = 'número de defeitos'
# legend = 'Figura 2: Número de defeitos por bicicleta.'

fig, ax = plt.subplots()
ax.scatter(range(0,len(y_data)), y_data, s=10, marker='*')
ax.plot([0,25], [LSC, LSC], 'orange', linewidth=0.9)
ax.plot([0,25], [LIC, LIC], 'orange', linewidth=0.9)
ax.plot([0,25], [LM, LM], 'black', linestyle='--', linewidth=0.7)
plt.ylim(LM - LM * 1.2, LM + LM * 1.2)
plt.title(legend)
plt.ylabel(y_label, size=10)

