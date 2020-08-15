import numpy as np
from matplotlib import pyplot as plt

def curve(x0, y0, b, beta, gamma, n):
    gamma = np.deg2rad(gamma)
    beta = np.deg2rad(beta)
    pm = np.array([[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]])
    bpart = np.array([0.0, 0.0])
    pm[0, 0] = x0
    pm[0, 1] = y0
    bpart[0] = b * np.sin(gamma - beta[1]) / np.sin(beta[0] + beta[1])
    bpart[1] = b * np.sin(np.pi - gamma - beta[0]) / np.sin(beta[0] + beta[1])
    pm[1, :] = np.array([pm[0, 0] + bpart[0] * np.cos(beta[0]), pm[0, 1] + bpart[0] * np.sin(beta[0])])
    pm[2, :] = np.array([pm[1, 0] - bpart[1] * np.cos(beta[1]), pm[1, 1] + bpart[1] * np.sin(beta[1])])

    #plt.plot( pm[:, 0], pm[:, 1] )

    t = np.linspace(0, 1, n)
    B = np.zeros([n, 2])
    B[:, 0] = (1 - t[:]) * (1 - t[:]) * pm[0, 0] + 2 * t[:] * (1 - t[:]) * pm[1, 0] + t[:] * t[:] * pm[2, 0]
    B[:, 1] = (1 - t[:]) * (1 - t[:]) * pm[0, 1] + 2 * t[:] * (1 - t[:]) * pm[1, 1] + t[:] * t[:] * pm[2, 1]
    return B


def angndist(t0, t1):
    dx = t1[0] - t0[0]
    dy = t1[1] - t0[1]
    dist = np.sqrt((dx)**2 + (dy)**2)
    ang = np.arctan(-dy/dx)
    ang = np.rad2deg(ang)
    return ang, dist
