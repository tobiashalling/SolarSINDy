import matplotlib.pyplot as plt
import numpy as np

def plot2(ax0, ay0, name0, ax1, ay1, name1, axm0, aym0, axm1, aym1):
    fig, ax = plt.subplots(1, 2, figsize=(12, 5.5))
    fig.suptitle('Accelerations')
    # Plots the planets
    ax[0].plot(ax0, ay0, label='Data {}'.format(name0), color='royalblue')
    ax[0].plot(axm0, aym0, label='SINDy {}'.format(name0), color='darkorange')
    
    ax[1].plot(ax1, ay1, label='Data {}'.format(name1), color='royalblue')
    ax[1].plot(axm1, aym1, label='SINDy {}'.format(name1), color='darkorange')
    
    ax[0].set(xlabel='x', ylabel='y')
    ax[1].set(xlabel='x', ylabel='y')
  
    ax[0].legend()
    ax[1].legend()


def f_2(dat, coef):
    F0 = (dat[:, 2]-dat[:, 0])/((dat[:, 2]-dat[:, 0])**2+(dat[:, 3]-dat[:, 1])**2)**(3/2)
    F1 = (dat[:, 3]-dat[:, 1])/((dat[:, 2]-dat[:, 0])**2+(dat[:, 3]-dat[:, 1])**2)**(3/2)
    F = np.array([F0, F1])
    a = np.dot(coef, F)
    return a

def perdiff(a1, a2):
    perdiff = (np.abs(a2 - a1)/(a2 + a1)/2)*100
    return perdiff
    
def err(aTrue, aEst):
    error = (np.mean((aEst-aTrue)**2))/(np.mean(aTrue**2))
    return error