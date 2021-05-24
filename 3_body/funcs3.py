import pysindy as ps
import numpy as np
import matplotlib.pyplot as plt
from pysindy.feature_library import CustomLibrary

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


def f_3(dat, coef):
    F0 = (dat[:, 2]-dat[:, 0])/((dat[:, 2]-dat[:, 0])**2+(dat[:, 3]-dat[:, 1])**2)**(3/2)
    F1 = (dat[:, 3]-dat[:, 1])/((dat[:, 2]-dat[:, 0])**2+(dat[:, 3]-dat[:, 1])**2)**(3/2)
    F2 = (dat[:, 4]-dat[:, 0])/((dat[:, 4]-dat[:, 0])**2+(dat[:, 5]-dat[:, 1])**2)**(3/2)
    F3 = (dat[:, 5]-dat[:, 1])/((dat[:, 4]-dat[:, 0])**2+(dat[:, 5]-dat[:, 1])**2)**(3/2)
    F4 = (dat[:, 4]-dat[:, 2])/((dat[:, 4]-dat[:, 2])**2+(dat[:, 5]-dat[:, 3])**2)**(3/2)
    F5 = (dat[:, 5]-dat[:, 3])/((dat[:, 4]-dat[:, 2])**2+(dat[:, 5]-dat[:, 3])**2)**(3/2)
    F = np.array([F0, F1, F2, F3, F4, F5])
    a = np.dot(coef, F)
    return a

def sindy(n, p, a, thres):
    if n == 2:
        functions = [
                    lambda x1, y1, x2, y2: (x2-x1)/((x2-x1)**2+(y2-y1)**2)**(3/2), 
                    lambda x1, y1, x2, y2: (y2-y1)/((x2-x1)**2+(y2-y1)**2)**(3/2)
                ]
    
        lib_custom = CustomLibrary(library_functions=functions)
        optimizer = ps.STLSQ(threshold=thres)
        
        t = np.arange(0, p.shape[0], 1)
        
        model = ps.SINDy(
                feature_library = lib_custom, 
                optimizer=optimizer)
    
        model.fit(p, t=t, x_dot=a)
        model.print(lhs=["x1''", "y1''", "x2''", "y2''"])
        coef = model.coefficients()
        print(coef)   
            
    elif n == 3:
        functions = [lambda x0, y0, x1, y1, x2, y2: (x1-x0)/((x1-x0)**2+(y1-y0)**2)**(3/2),
                     lambda x0, y0, x1, y1, x2, y2: (y1-y0)/((x1-x0)**2+(y1-y0)**2)**(3/2),
                     lambda x0, y0, x1, y1, x2, y2: (x2-x0)/((x2-x0)**2+(y2-y0)**2)**(3/2),
                     lambda x0, y0, x1, y1, x2, y2: (y2-y0)/((x2-x0)**2+(y2-y0)**2)**(3/2),
                     lambda x0, y0, x1, y1, x2, y2: (x2-x1)/((x2-x1)**2+(y2-y1)**2)**(3/2), 
                     lambda x0, y0, x1, y1, x2, y2: (y2-y1)/((x2-x1)**2+(y2-y1)**2)**(3/2)]
    
        lib_custom = CustomLibrary(library_functions=functions)
        optimizer = ps.STLSQ(threshold=thres)
        
        t = np.arange(0, p.shape[0], 1)
        
        model = ps.SINDy( 
                feature_library = lib_custom, 
                optimizer=optimizer)
        
        model.fit(p, t=t, x_dot=a)
        model.print(lhs=["x1''","y1''","x2''","y2''","x3''","y3''"])
        coef = model.coefficients()
        print(coef)
        
    else: 
        print('Number of bodies not supported')

        
        
def perdiff(a1, a2):
    perdiff = (np.abs(a2 - a1)/(a2 + a1)/2)*100
    return perdiff

def err(aTrue, aEst):
    error = (np.mean((aEst-aTrue)**2))/(np.mean(aTrue**2))
    return error