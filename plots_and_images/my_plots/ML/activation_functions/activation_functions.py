#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import ltLaTeXpyplot as lt

fig = lt.ltFigure(name='activation_functions', tight_layout=True)

x = np.arange(-5,5.01,0.01)

linear = lt.ltPlotFct(x, x, label="Linear", color='C0')
relu = lt.ltPlotFct(x, (x+abs(x))/2, label="ReLU", color='C0')
elu = lt.ltPlotFct(x, (x+abs(x))/2 + (np.exp(x)-1)*(1-np.sign(x))/2, label="ELU", color='C0')
selu = lt.ltPlotFct(x, 1.05070098*(x+abs(x))/2 + 1.05070098*1.67326324*(np.exp(x)-1)*(1-np.sign(x))/2, label="SeLU", color='C0')
sigmoid = lt.ltPlotFct(x, 1/(1+np.exp(-x)), label="Sigmoïd", color='C0')
tanh = lt.ltPlotFct(x, np.tanh(x), label="Tanh", color='C0')

acs = [linear, sigmoid, tanh, relu, elu, selu]
y_mins = [-5, -1.1, -1.1, -2, -2, -2]
y_maxs = [5, 1.1, 1.1, 5, 5, 5]

index=0
for ac in acs:
    index+=1
    fig.addgraph(
        'graph{}'.format(str(index)),
        x_label= None,
        y_label= None,
        show_legend=False,
        legend_on_side=False,
        position = int(230+index),
        x_min = x.min(), x_max = x.max(),
        y_min = y_mins[index-1], y_max = y_maxs[index-1],
        title = ac.label,
    )
    fig.fig.axes[-1].axhline(color='C5', linewidth=.5)
    fig.fig.axes[-1].axvline(color='C5', linewidth=.5)
    fig.addplot(
        ac,
        'graph{}'.format(str(index)),
    )

fig.save()

