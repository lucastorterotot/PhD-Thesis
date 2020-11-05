#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

n_saves_counter = 1
image_name = "overfitting_explained-{}.png"

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

with plt.xkcd():
    # Based on "Stove Ownership" from XKCD by Randall Monroe
    # http://xkcd.com/418/

    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.1, 0.8, 0.8))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.xticks([])
    plt.yticks([])
    ax.set_ylim([0, 1])
    arrowed_spines(ax, arrowLength=1, labels=('',''))

    plt.xlabel('Amount of training')
    plt.ylabel('Loss value')

    xs = np.arange(0,100,1)
    ys_train = np.exp(-5*xs/xs[-1])
    ys_test = np.exp(-5*xs/xs[-1]) + .5*xs/xs[-1]

    ln1, = plt.plot(xs, ys_train, label='Training data', color="C0")
    fig.savefig(image_name.format(n_saves_counter))
    n_saves_counter+=1

    txt1 = plt.annotate(
         'Really good?',
         xy=(90, .05), arrowprops=dict(arrowstyle='->'), xytext=(50, .25))

    fig.savefig(image_name.format(n_saves_counter))
    n_saves_counter+=1

    txt1.remove()

    ln2, = plt.plot(xs, ys_test, label='Non-training data', color="C3")

    plt.legend()
    fig.savefig(image_name.format(n_saves_counter))
    n_saves_counter+=1

    txt2 = plt.annotate(
         'Good on training data',
         xy=(90, .05), arrowprops=dict(arrowstyle='->'), xytext=(50, .25))

    txt3 = plt.annotate(
         'Not quite on new data',
         xy=(90, .5), arrowprops=dict(arrowstyle='->'), xytext=(50, .65))

    fig.savefig(image_name.format(n_saves_counter))
    n_saves_counter+=1

    txt2.remove()
    txt3.remove()

    txt4 = plt.annotate(
         'Underfitting here',
         xy=(15, .65), arrowprops=dict(arrowstyle='->'), xytext=(33, .65))

    txt5 = plt.annotate(
         'Overfitting here',
         xy=(85, .45), arrowprops=dict(arrowstyle='->'), xytext=(33, .45))

    fig.savefig(image_name.format(n_saves_counter))
    n_saves_counter+=1

    txt4.remove()
    txt5.remove()

    txt6 = plt.annotate(
        "Stop training here: early stopping",
         xy=(45, .35), arrowprops=dict(arrowstyle='->'), xytext=(25, .55))

    fig.savefig(image_name.format(n_saves_counter))
    n_saves_counter+=1

    txt7 = plt.annotate(
         'Still overfits...',
         xy=(50, .25), arrowprops=dict(arrowstyle='->'), xytext=(60, .25))

    fig.savefig(image_name.format(n_saves_counter))
    n_saves_counter+=1

    txt6.remove()
    txt7.remove()

    ln1.remove()
    ln2.remove()
    xs = np.arange(0,50,1)
    ys_train = 0.25 + 0.75*np.exp(-5*xs/xs[-1])
    ys_test = ys_train * (1+.1*xs/xs[-1])
    plt.plot(xs, ys_train, label='Training data', color="C0")
    plt.plot(xs, ys_test, label='Non-training data', color="C3")

    txt8 = plt.annotate(
        'Tune model parameters!',
        xy=(25, .7),
    )
    txt9 = plt.annotate(
         'early stopping',
         xy=(50, .25), arrowprops=dict(arrowstyle='->'), xytext=(50, .1), horizontalalignment = 'center')
    txt10 = plt.annotate(
         'not overfitting',
         xy=(50, .25*1.05), arrowprops=dict(arrowstyle='->'), xytext=(60, .25))

    fig.savefig(image_name.format(n_saves_counter))
    n_saves_counter+=1

