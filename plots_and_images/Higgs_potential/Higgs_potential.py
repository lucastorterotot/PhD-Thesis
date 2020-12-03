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
Lambda = (mu/vev)**2

minimum_V = vev * .5**.5
    
maxrange = minimum_V*1.225

r = np.linspace(0, maxrange, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)

X, Y = R*np.cos(P), R*np.sin(P)
Z = - mu**2 * R**2 + Lambda * R**4
Z2 =  (.5*mu**2 * R**2 + Lambda * R**4)/4

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
             title="$\\mu^2\\geq0$")
fig.addgraph('graph2',
             position=122, show_cmap_legend=False, projection='3d',
             x_ticks=True, y_ticks=True, z_ticks=True,
             z_min = z_min, z_max=z_max,
             x_ticks_min = 0, x_ticks_max = 1, x_ticks_step = 2,
             y_ticks_min = 0, y_ticks_max = 1, y_ticks_step = 2,
             z_ticks_min = 0, z_ticks_max = 1, z_ticks_step = 2,
             x_label="$\\Re(\\phi)", y_label="$\\Im(\\phi)",
             title="$\\mu^2<0$")

# Insert objects in graphs
cmap = 'coolwarm'

def rp_to_x(r,p):
    return r * np.cos(p)

def rp_to_y(r,p):
    return r * np.sin(p)

fig.addplot(
    lt.ltPlotSurf(r, p,
                  x_fct = rp_to_x, y_fct = rp_to_y, z_fct = Z2,
                  cmap=cmap, use_cmap=True, cmap_low = z_min, cmap_high=z_max, alpha = .7, linewidth=None, only_lines=False),
    'graph1')

fig.addplot(
    lt.ltPlotSurf(r, p,
                  x_fct = rp_to_x, y_fct = rp_to_y, z_fct = Z,
                  cmap=cmap, use_cmap=True, cmap_low = z_min, cmap_high=z_max, alpha = .7, linewidth=None, only_lines=False),
    'graph2')

# Save figure
fig.save()

fig = lt.ltFigure(name='fig_for_slides', width_frac=.45, height_width_ratio=1, tight_layout=False)
fig.addgraph('graph2',
             position=111, show_cmap_legend=False, projection='3d',
             x_ticks=True, y_ticks=True, z_ticks=True,
             z_min = z_min, z_max=z_max,
             x_ticks_min = 0, x_ticks_max = 1, x_ticks_step = 2,
             y_ticks_min = 0, y_ticks_max = 1, y_ticks_step = 2,
             z_ticks_min = 0, z_ticks_max = 1, z_ticks_step = 2,
             x_label="$\\Re(\\phi)", y_label="$\\Im(\\phi)",
             title="$\\mu^2<0$")

fig.addplot(
    lt.ltPlotSurf(r, p,
                  x_fct = rp_to_x, y_fct = rp_to_y, z_fct = Z,
                  cmap=cmap, use_cmap=True, cmap_low = z_min, cmap_high=z_max, alpha = .7, linewidth=None, only_lines=False),
    'graph2')

fig.save()
