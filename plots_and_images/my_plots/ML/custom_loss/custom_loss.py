#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

import ltLaTeXpyplot as lt

# Create figure
fig = lt.ltFigure(name='mapesqrt_boundaries_loss', tight_layout=True, height_width_ratio=.725)

# Define what to plot
# make these smaller to increase the resolution
dx = 1
dy = dx

min_mass = 50
min_mass_pred = 0
max_mass = 1000
max_mass_pred = 1000
max_loss = 30

# generate 2 2d grids for the x & y bounds
x = np.arange(min_mass, max_mass + dx/2, dx)
y = np.arange(min_mass_pred, max_mass_pred + dy/2, dy)

def mapesqrt_boundaries(y_true, y_pred):
    loss = np.abs((y_true - y_pred)/(y_true**0.5))

    factor = np.ones(y_true.shape)
    factor[y_pred - y_true >= max_mass - y_pred] = 0
    factor[y_true - y_pred >= y_pred - min_mass] = 0.1

    loss *= factor

    loss[loss > max_loss] = max_loss

    return loss
    
# Define graphs
fig.addgraph('graph1', show_cmap_legend=True,
            x_label = "$y_t$", y_label="$y_p$",
            x_min=min_mass_pred, x_max=max_mass_pred, y_min=min_mass_pred, y_max=max_mass_pred)

# Insert object in plots
field = lt.ltPlotScalField(x, y, z_fct = mapesqrt_boundaries, cmap = "ocean_r")

field.plot(fig, 'graph1')

# Save figure
fig.save(format='pdf')
fig.save(format='pgf')
fig.save(format='png')
