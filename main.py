import numpy as np
from matplotlib import pyplot as plt
import curve

b = 1.0          # хорда
gamma = 35.0     # угол установки
beta = np.array([90.0, 17.0])      # угол входа и выхода
n = 50
r = np.array([0.1, 0.04])
x0 = 0
y0 = 0

B = curve.curve(x0, y0, b, beta, gamma, n)
inang = np.deg2rad(5)
outang = np.deg2rad(5)
spvh = np.array([B[0, 0]+r[0]*np.cos(np.pi/2 - np.deg2rad(beta[0])),
                 B[0, 1]-r[0]*np.sin(np.pi/2 - np.deg2rad(beta[0]))])
spvih = np.array([B[-1, 0]+r[1]*np.cos(np.pi/2 - np.deg2rad(beta[1])),
                  B[-1, 1]+r[1]*np.sin(np.pi/2 - np.deg2rad(beta[1]))])
corvh = np.array([B[0, 0]-r[0]*np.cos(np.pi/2 - np.deg2rad(beta[0])),
                  B[0, 1]+r[0]*np.sin(np.pi/2 - np.deg2rad(beta[0]))])
corvih = np.array([B[-1, 0]-r[1]*np.cos(np.pi/2 - np.deg2rad(beta[1])),
                   B[-1, 1]-r[1]*np.sin(np.pi/2 - np.deg2rad(beta[1]))])

angsp, distsp = curve.angndist(spvh, spvih)
angcor, distcor = curve.angndist(corvh, corvih)

A = curve.curve(corvh[0], corvh[1], distcor, beta, angcor, n)
C = curve.curve(spvh[0], spvh[1], distsp, beta, angsp, n)
#breakpoint()
fig, ax = plt.subplots()
plt.plot(spvh[0],spvh[1],'bo')
plt.plot(corvh[0],corvh[1],'ro')

circle1 = plt.Circle((B[0, 0], B[0, 1]), r[0])
circle2 = plt.Circle((B[-1, 0], B[-1, 1]), r[1])
ax.add_artist(circle1)
ax.add_artist(circle2)


plt.plot(spvih[0],spvih[1],'bo')
plt.plot(corvih[0],corvih[1],'ro')
plt.plot(A[:, 0], A[:, 1])
plt.plot(B[:, 0], B[:, 1])
plt.plot(C[:, 0], C[:, 1])
plt.axis('equal')
plt.gca().invert_yaxis()
plt.show()
breakpoint()