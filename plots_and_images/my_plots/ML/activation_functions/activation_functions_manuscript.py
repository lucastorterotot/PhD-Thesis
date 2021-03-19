#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import ltLaTeXpyplot as lt

x = np.arange(-5,5.01,0.01)

class activation_function():

    def __init__(
        self,
        x,
        y,
        name,
        label = None,
        color = 'C0',
        y_min = None,
        y_max = None
    ):
        self.x = x
        self.y = y
        self.name = name
        self.label = label
        self.color = color
        self.plot = lt.ltPlotFct(
            x,
            y,
            color = color
        )

        if y_min == None:
            self.y_min = np.min(y)
        else:
            self.y_min = y_min

        if y_max == None:
            self.y_max = np.max(y)
        else:
            self.y_max = y_max

activations = [
    activation_function(
        x, x,
        "linear", label="1",
        y_min = -5, y_max = 5
    ),
    activation_function(
        x, (x+abs(x))/2,
        "relu", label="\\mathrm{ReLU}",
        y_min = -2, y_max = 5
    ),
    activation_function(
        x, (x+abs(x))/2 + (np.exp(x)-1)*(1-np.sign(x))/2,
        "elu", label="\\mathrm{ELU}",
        y_min = -2, y_max = 5
    ),
    activation_function(
        x, 1.05070098*(x+abs(x))/2 + 1.05070098*1.67326324*(np.exp(x)-1)*(1-np.sign(x))/2,
        "selu", label="\\mathrm{SELU}",
        y_min = -2, y_max = 5
    ),
    activation_function(
        x, 1/(1+np.exp(-x)),
        "sigmoid", label="\\mathrm{sig}",
        y_min = -1.5, y_max = 1.5
    ),
    activation_function(
        x, np.tanh(x),
        "tanh", label="\\tanh",
        y_min = -1.5, y_max = 1.5
    ),
    activation_function(
        x, np.log(1+np.exp(x)),
        "softplus", label="\\mathrm{Spl}",
        y_min = -2, y_max = 5
    ),
    activation_function(
        x, x / (1+np.abs(x)),
        "softsign", label="\\mathrm{Ssg}",
        y_min = -1.5, y_max = 1.5
    )
]

for activation in activations:
    fig = lt.ltFigure(
        name = activation.name,
        height_width_ratio = 1, width_frac = .425
    )
    fig.addgraph(
        'graph',
        x_label= r"$x$",
        y_label= r"${}(x)$".format(activation.label),
        show_legend=False,
        legend_on_side=False,
        x_min = x.min(), x_max = x.max(),
        y_min = activation.y_min, y_max = activation.y_max,
    )
    fig.fig.axes[-1].axhline(color='C5', linewidth=.5)
    fig.fig.axes[-1].axvline(color='C5', linewidth=.5)
    fig.addplot(
        activation.plot,
        'graph',
    )

    fig.save()

