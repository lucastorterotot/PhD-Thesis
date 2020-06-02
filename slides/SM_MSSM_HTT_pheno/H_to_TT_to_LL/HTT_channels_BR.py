#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

import ltLaTeXpyplot as lt

# Create figure
fig = lt.ltFigure(name='HTT_channels_pie_chart', height_width_ratio=1, width_frac=.3)

# Define what to plot
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = '$\\tau_\\mathrm{h}\\tau_\\mathrm{h}$', '$\\mu\\tau_\\mathrm{h}$', '$e\\tau_\\mathrm{h}$', '$\\mu\\mu$', '$ee$', '$e\\mu$'
sizes = [42, 23, 23, 3, 3, 6]
explode = (0, 0.1, 0.1, 0, 0, 0)

def autopct(value):
    if int(value) > 10:
        return ''.join(['\\SI{', str(int(round(value,0))), '}{', '\\%', '}'])
    else:
        return ''
Pie = lt.ltPlotPie(sizes, labels=labels, explode=explode, autopct=autopct)
    
# Define graphs
fig.addgraph('graph1')

# Insert object in plots
Pie.plot(fig, 'graph1')

# Save figure
fig.save()
