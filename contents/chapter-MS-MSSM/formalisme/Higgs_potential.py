#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

import ltLaTeXpyplot as lt

# Create figure
fig = lt.ltFigure(name='fig', width_frac=1, height_width_ratio=.5, tight_layout=True)

# Define what to plot
mH = 125.18
vev = 246.22
mu = mH * .5**.5
Lambda = mu/vev
    
maxrange = vev*1.225

r = np.linspace(0, maxrange, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)

X, Y = R*np.cos(P), R*np.sin(P)
Z = - mu**2 * R**2 + .5*Lambda**2 * R**4
Z2 =  (.5*mu**2 * R**2 + .5*Lambda**2 * R**4)/4

z_max = 0
z_min = 0
for k in range(len(Z)):
    for l in range(len(Z[k])):
        if Z[k][l] > z_max:
            z_max = Z[k][l]
        if Z[k][l] < z_min:
            z_min = Z[k][l]
for k in range(len(Z2)):
    for l in range(len(Z2[k])):
        if Z2[k][l] > z_max:
            z_max = Z2[k][l]
        if Z2[k][l] < z_min:
            z_min = Z2[k][l]

# Define graphs
fig.addgraph('graph1',
             position=121, show_cmap_legend=False, projection='3d',
             x_ticks=True, y_ticks=True, z_ticks=True,
             z_min = z_min-z_min, z_max=z_max-z_min,
             x_ticks_min = 0, x_ticks_max = 1, x_ticks_step = 2,
             y_ticks_min = 0, y_ticks_max = 1, y_ticks_step = 2,
             z_ticks_min = 0, z_ticks_max = 1, z_ticks_step = 2,
             x_label="$\\Re(\\phi)", y_label="$\\Im(\\phi)",
             title="$\\mu\\geq0$")
fig.addgraph('graph2',
             position=122, show_cmap_legend=False, projection='3d',
             x_ticks=True, y_ticks=True, z_ticks=True,
             z_min = z_min, z_max=z_max,
             x_ticks_min = 0, x_ticks_max = 1, x_ticks_step = 2,
             y_ticks_min = 0, y_ticks_max = 1, y_ticks_step = 2,
             z_ticks_min = 0, z_ticks_max = 1, z_ticks_step = 2,
             x_label="$\\Re(\\phi)", y_label="$\\Im(\\phi)",
             title="$\\mu<0$")

# Insert objects in graphs
cmap = 'coolwarm'

import matplotlib as mpl
import matplotlib.pyplot as plt
norm = mpl.colors.Normalize(vmin=z_min, vmax=z_max)

fig.graphs['graph2'].graph.plot_surface(X, Y, Z, cmap=cmap, facecolors=getattr(mpl.cm, cmap)(norm(Z)), alpha=.7)
fig.graphs['graph1'].graph.plot_surface(X, Y, Z2, cmap=cmap, facecolors=getattr(mpl.cm, cmap)(norm(Z2)), alpha=.7)

# Save figure
fig.save()
