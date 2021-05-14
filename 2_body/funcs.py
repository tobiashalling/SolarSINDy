import matplotlib.pyplot as plt

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


def f_3(dat):
    F0 = (dat[:, 2]-dat[:, 0])/((dat[:, 2]-dat[:, 0])**2+(dat[:, 3]-dat[:, 1])**2)**(3/2)
    F1 = (dat[:, 3]-dat[:, 1])/((dat[:, 2]-dat[:, 0])**2+(dat[:, 3]-dat[:, 1])**2)**(3/2)
    F2 = (dat[:, 4]-dat[:, 0])/((dat[:, 4]-dat[:, 0])**2+(dat[:, 5]-dat[:, 1])**2)**(3/2)
    F3 = (dat[:, 5]-dat[:, 1])/((dat[:, 4]-dat[:, 0])**2+(dat[:, 5]-dat[:, 1])**2)**(3/2)
    F4 = (dat[:, 4]-dat[:, 2])/((dat[:, 4]-dat[:, 2])**2+(dat[:, 5]-dat[:, 3])**2)**(3/2)
    F5 = (dat[:, 5]-dat[:, 3])/((dat[:, 4]-dat[:, 2])**2+(dat[:, 5]-dat[:, 3])**2)**(3/2)
    return F0, F1, F2, F3, F4, F5