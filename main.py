import numpy as np
from matplotlib import pyplot as plt
import curve

b = 1.0                              # хорда
gamma = 60.0                         # угол установки
beta = np.array([45.0, 30.0])        # угол входа и выхода (по скоростям)
n = 100                              # количество сегментов лопатки
r = np.array([0.08, 0.045])          # абсолютные значения радиуса вх и вых кромки
x0 = 0.0                             # нулевая координата
y0 = 0.0
angin = 30.0                         # угол входной кромки
angout = 10.0                        # угол выходной кромки
t = 1.0                              # абсолютный шаг

# центральная линия по углам потока
B = curve.curve(x0, y0, b, beta, gamma, n)

# координаты начала и конца профиля лопатки
spvh = np.array([B[0, 0] + r[0] * np.cos(np.pi / 2.0 - np.deg2rad(beta[0] - angin / 2.0)),
                 B[0, 1] - r[0] * np.sin(np.pi / 2.0 - np.deg2rad(beta[0] - angin / 2.0))])
spvih = np.array([B[-1, 0] + r[1] * np.cos(np.pi / 2.0 - np.deg2rad(beta[1] - angout / 2.0)),
                  B[-1, 1] + r[1] * np.sin(np.pi / 2.0 - np.deg2rad(beta[1] - angout / 2.0))])
corvh = np.array([B[0, 0] - r[0] * np.cos(np.pi / 2.0 - np.deg2rad(beta[0] + angin / 2.0)),
                  B[0, 1] + r[0]*np.sin(np.pi / 2.0 - np.deg2rad(beta[0] + angin / 2.0))])
corvih = np.array([B[-1, 0] - r[1] * np.cos(np.pi / 2.0 - np.deg2rad(beta[1] + angout / 2.0)),
                   B[-1, 1] - r[1] * np.sin(np.pi / 2.0 - np.deg2rad(beta[1] + angout / 2.0))])

# условный угол установки и длина профиля
angsp, distsp = curve.angndist(spvh, spvih)
angcor, distcor = curve.angndist(corvh, corvih)
if angcor < 0:
    angcor = angcor + 180.0
if angsp < 0:
    angsp = angsp + 180.0

# координаты корыта и спинки соответственно от входной до выходной кромки
A = curve.curve(corvh[0], corvh[1], distcor, np.array([beta[0] + angin / 2.0, beta[1] + angout / 2.0]), angcor, n)
C = curve.curve(spvh[0], spvh[1], distsp, np.array([beta[0] - angin / 2.0, beta[1] - angout / 2.0]), angsp, n)

# творческая часть с картинками
# первая лопатка
fig, ax = plt.subplots()
#plt.plot(spvh[0], spvh[1], 'bo')
#plt.plot(corvh[0], corvh[1], 'ro')
#plt.plot(spvih[0],spvih[1],'bo')
#plt.plot(corvih[0],corvih[1],'ro')
circle1 = plt.Circle((B[0, 0], B[0, 1]), r[0], color='r', fill=False)
circle2 = plt.Circle((B[-1, 0], B[-1, 1]), r[1], color='r', fill=False)
ax.add_artist(circle1)
ax.add_artist(circle2)
plt.plot(A[:, 0], A[:, 1], 'r')
plt.plot(B[:, 0], B[:, 1], 'b-.')
plt.plot(C[:, 0], C[:, 1], 'r')

# вторая лопатка
circle3 = plt.Circle((B[0, 0] + t, B[0, 1]), r[0], color='r', fill=False)
circle4 = plt.Circle((B[-1, 0] + t, B[-1, 1]), r[1], color='r', fill=False)
ax.add_artist(circle3)
ax.add_artist(circle4)
plt.plot(A[:, 0] + t, A[:, 1], 'r')
plt.plot(B[:, 0] + t, B[:, 1], 'b-.')
plt.plot(C[:, 0] + t, C[:, 1], 'r')
# настройка
plt.axis('equal')
plt.gca().invert_yaxis()
plt.show()
breakpoint()