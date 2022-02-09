# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 11:08:29 2021

@author: Renan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data_v = np.array(([1.05,
                    1.22,
                    1.40,
                    1.62,
                    1.82,
                    2.05,
                    2.26,
                    2.47,
                    2.67,
                    2.91,
                    3.17,
                    3.39,
                    3.64,
                    3.86,
                    4.13]))

data_t = np.array(([27,
                    30,
                    35,
                    40,
                    45,
                    50,
                    55,
                    60,
                    65,
                    70,
                    75,
                    80,
                    85,
                    90,
                    95]))

data_ve = np.array(([1.073,
                     1.196,
                     1.403,
                     1.611,
                     1.822,
                     2.035,
                     2.250,
                     2.467,
                     2.687,
                     2.908,
                     3.131,
                     3.357,
                     3.584,
                     3.813,
                     4.044]))

data_te = np.array(([27,
                    30,
                    35,
                    40,
                    45,
                    50,
                    55,
                    60,
                    65,
                    70,
                    75,
                    80,
                    85,
                    90,
                    95]))

data = pd.DataFrame((data_t, data_v)).T

data.to_excel(excel_writer = r"C:\Users\Renan\Documents\Renan\Graduação\7° Semestre\Lab. Física III\Relatórios\Relatório X3 - Termoeletricidade\tabela1.xlsx")

# criar modelo linear e otimizar
lm_model1 = LinearRegression()
lm_model1.fit(data_t.reshape(-1,1), data_v)
 
# extrair coeficientes
slope1 = lm_model1.coef_
intercept1 = lm_model1.intercept_

# criar modelo linear e otimizar
lm_model2 = LinearRegression()
lm_model2.fit(data_te.reshape(-1,1), data_ve)
 
# extrair coeficientes
slope2 = lm_model2.coef_
intercept2 = lm_model2.intercept_

##



fig, ax = plt.subplots(1)

ax.errorbar(data_t, data_v, fmt='o', xerr=0.5, yerr=0.01, markersize=1.5, color='black')
ax.plot(data_t, (data_t * slope1 + intercept1), color='r', label='experimental')
# plt.xlabel('Diferença de temperatura no termopar (°C)')
# plt.ylabel('Tensão (V)')


# ax.scatter(data_te, data_ve, color='black', s=3)
ax.plot(data_te, (data_te * slope2 + intercept2), color='b', label='teórico')
plt.legend()
plt.xlabel('Diferença de temperatura no termopar (°C)')
plt.ylabel('Tensão (V)')