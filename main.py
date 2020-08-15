import numpy as np
from matplotlib import pyplot as plt


b = 1.0          # хорда
gamma = 45.0     # угол установки
beta = np.array([75.0, 20.0])      # угол входа и выхода

gamma = np.deg2rad(gamma)
beta = np.deg2rad(beta)
print(beta)
print(gamma)
pm = np.array([[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]])    # координаты точек входа, средняя, выхода
bpart = np.array([0.0, 0.0])                       # длина входного и выходного участков
pm[0, 0] = 0.0
pm[0, 1] = 0.0
bpart[0] = b * np.sin(gamma - beta[1]) / np.sin(beta[0] + beta[1])
bpart[1] = b * np.sin(np.pi - gamma - beta[0]) / np.sin(beta[0] + beta[1])
print(bpart)
pm[1, :] = np.array([pm[0, 0] + bpart[0] * np.cos(beta[0]), pm[0, 1] + bpart[0] * np.sin(beta[0])])
pm[2, :] = np.array([pm[1, 0] - bpart[1] * np.cos(beta[1]), pm[1, 1] + bpart[1] * np.sin(beta[1])])
#n = 10
#dmp = np.array([[(pm[1, 0] - pm[0, 0]) / n, (pm[1, 1] - pm[0, 1]) / n],
#                [(pm[2, 0] - pm[1, 0]) / n, (pm[2, 1] - pm[1, 1]) / n]])
#print(pm)
#pmm1 = np.zeros([n + 1, 2])
#pmm2 = np.zeros([n + 1, 2])
#pmm2 = pm[1, :]

#for i in range(n):
#    pmm1[i + 1, :] = np.array([pmm1[0, 0] + i * dmp[0, 0], pmm1[0, 1] + i * dmp[1, 0]])
#    pmm2[i + 1, :] = np.array([pmm2[0, 0] + i * dmp[0, 1], pmm2[0, 1] + i * dmp[1, 1]])
#    plt.plot(pmm1[i,0],pmm2[i,1])
plt.plot(pm[:, 0], pm[:, 1])
plt.axis('equal')
plt.gca().invert_yaxis()
plt.show()
breakpoint()