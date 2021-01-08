#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# fix randomness
np.random.seed(1)

# regression
x = np.linspace(0,1,20)
y_true = 0.3*x + 0.5*(x-.5)**2 + 0.075*np.exp(-50*(x-0.65)**2)
y_noise = y_true + 0.015*np.random.normal(size=len(y_true))

under_model_y = 0.3317879836849671 * x + 0.04601663644888622

from scipy.interpolate import interp1d
over_model_fct = interp1d(x,y_noise, kind='cubic')
x_dense = np.linspace(0,1,200)
over_model_y = over_model_fct(x_dense)

y_noise_2 = y_true + 0.019*np.random.normal(size=len(y_true))

def arrowed_spines(ax=None, arrowLength=30, labels=('X', 'Y'), arrowStyle='<|-'):
    xlabel, ylabel = labels

    for i, spine in enumerate(['left', 'bottom']):
        # Set up the annotation parameters
        t = ax.spines[spine].get_transform()
        xy, xycoords = [1, 0], ('axes fraction', t)
        xytext, textcoords = [arrowLength, 0], ('offset points', t)

        # create arrowprops
        arrowprops = dict( arrowstyle=arrowStyle,
                           facecolor=ax.spines[spine].get_facecolor(), 
                           linewidth=ax.spines[spine].get_linewidth(),
                           alpha = ax.spines[spine].get_alpha(),
                           zorder=ax.spines[spine].get_zorder(),
                           linestyle = ax.spines[spine].get_linestyle() )

        if spine is 'bottom':
            ha, va = 'left', 'center'
            xarrow = ax.annotate(xlabel, xy, xycoords=xycoords, xytext=xytext, 
                        textcoords=textcoords, ha=ha, va='center',
                        arrowprops=arrowprops)
        else:
            ha, va = 'center', 'bottom'
            yarrow = ax.annotate(ylabel, xy[::-1], xycoords=xycoords[::-1], 
                        xytext=xytext[::-1], textcoords=textcoords[::-1], 
                        ha='center', va=va, arrowprops=arrowprops)
    return xarrow, yarrow

# Définir le graphique
x_labels = [None, None, None, "Underfitting", "Good model", "Overfitting"]
y_labels = ["Training data", None, None, "Validating data", None, None]

with plt.xkcd():
    from matplotlib import patheffects
    plt.rcParams['path.effects'] = [patheffects.withStroke(linewidth=0)]

    fig = plt.figure(figsize=(10, 6), dpi=200)

    ax1 = plt.subplot(2,3,1)
    plt.plot(x, y_noise, marker='.', color='C0', linewidth=0)
    plt.plot(x, under_model_y, color='C2', linewidth=1)

    ax2 = plt.subplot(2,3,2)
    plt.plot(x, y_noise, marker='.', color='C0', linewidth=0)
    plt.plot(x, y_true, color='C2', linewidth=1)

    ax3 = plt.subplot(2,3,3)
    plt.plot(x, y_noise, marker='.', color='C0', linewidth=0)
    plt.plot(x_dense, over_model_y, color='C2', linewidth=1)

    ax4 = plt.subplot(2,3,4)
    plt.plot(x, y_noise_2, marker='.', color='C3', linewidth=0)
    plt.plot(x, under_model_y, color='C2', linewidth=1)

    ax5 = plt.subplot(2,3,5)
    plt.plot(x, y_noise_2, marker='.', color='C3', linewidth=0)
    plt.plot(x, y_true, color='C2', linewidth=1)

    ax6 = plt.subplot(2,3,6)
    plt.plot(x, y_noise_2, marker='.', color='C3', linewidth=0)
    plt.plot(x_dense, over_model_y, color='C2', linewidth=1)

    axs = [ax1, ax2, ax3, ax4, ax5, ax6]

    for index in range(1,7):
        ax = axs[index-1]

        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlabel(x_labels[index-1])
        ax.set_ylabel(y_labels[index-1])
        arrowed_spines(ax, arrowLength=1, labels=('',''))

    plt.savefig("examples_xkcd.png")
    
#    fig.addgraph(
#        'graph{}'.format(str(index)),
#        x_label = x_labels[index-1],
#        y_label = y_labels[index-1],
#        x_ticks = False,
#        y_ticks = False,
#        show_legend=False, legend_on_side=True,
#        position = int(230+index),
#    )
#
## Insérer les objets à tracer dans le plot
#for index in range(1,4):
#    points.plot(fig, 'graph{}'.format(str(index)))
#for index in range(4,7):
#    points_2.plot(fig, 'graph{}'.format(str(index)))
#
#under_model.plot(fig, 'graph1')
#good_model.plot(fig, 'graph2')
#over_model.plot(fig, 'graph3')
#
#under_model.plot(fig, 'graph4')
#good_model.plot(fig, 'graph5')
#over_model.plot(fig, 'graph6')
#
## Sauvegarder la figure
#fig.save()
#
