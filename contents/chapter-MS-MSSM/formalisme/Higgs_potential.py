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
Lambda = mu**2/(2*vev**2)
    
maxrange = vev*1.225

r = np.linspace(0, maxrange, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)

X, Y = R*np.cos(P), R*np.sin(P)
Z = - mu**2 * R**2 + Lambda * R**4
Z2 =  .5*mu**2 * R**2 + Lambda * R**4

# Define graphs
fig.addgraph('graph1',
             position=121, show_cmap_legend=False, projection='3d',
             x_ticks=False, y_ticks=False, z_ticks=False,
             x_label="$\\Re(\\phi)", y_label="$\\Im(\\phi)",
             title="$\\mu\\geq0$")
fig.addgraph('graph2',
             position=122, show_cmap_legend=False, projection='3d',
             x_ticks=False, y_ticks=False, z_ticks=False,
             x_label="$\\Re(\\phi)", y_label="$\\Im(\\phi)",
             title="$\\mu<0$")

# Insert objects in graphs
cmap = 'coolwarm'
fig.graphs['graph2'].graph.plot_surface(X, Y, Z, cmap=cmap)
fig.graphs['graph1'].graph.plot_surface(X, Y, Z2, cmap=cmap)

# Save figure
fig.save()