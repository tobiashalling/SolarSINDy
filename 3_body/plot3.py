def plot(ax0, ay0, name0, ax1, ay1, name1, ax2, ay2, name2, axm0, aym0, axm1, aym1, axm2, aym2):
    fig, ax = plt.subplots(1, 2, figsize=(12, 5.5))
    # Plots the planets
    ax[0, 0].plot(ax0, ax0, label='Data name0', color='darkorange')
    ax[0, 0].plot(ax1, ay1, label='Data name1', color='royalblue')
    ax[0, 0].plot(ax2, ay2, label='Data name2', color='saddlebrown')
    
    ax[1, 0].plot(axm0, aym0, label='SINDy name0', color='darkorange')
    ax[1, 0].plot(axm1, aym0, label='SINDy name1', color='royalblue')
    ax[1, 0].plot(axm2, aym0, label='SINDy name2', color='saddlebrown')
    
    ax[0, 0].set(xlabel='x', ylabel='y')
    ax[0, 1].set(xlabel='x', ylabel='y')
    ax[0, 0].set_title('Position')
    ax[0, 1].set_title('SINDy Position')
    ax[0, 0].legend()
    ax[0, 1].legend()