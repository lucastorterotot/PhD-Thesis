#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import ltLaTeXpyplot as lt

fig = lt.ltFigure(name='examples', tight_layout = True)

# Définir les grandeurs
# fix randomness
np.random.seed(1)

# regression
x = np.linspace(0,1,20)
y_true = 0.3*x + 0.5*(x-.5)**2 + 0.075*np.exp(-50*(x-0.65)**2)
y_noise = y_true + 0.015*np.random.normal(size=len(y_true))

points = lt.ltPlotPts(x, y_noise)
reglin = lt.ltPlotRegLin(x, y_noise, np.ones(len(x))*0.1, np.ones(len(y_noise))*0.1, verbose=True)
under_model = reglin.reglin
under_model.color = 'C2'
good_model = lt.ltPlotFct(x, y_true, color='C2')
from scipy.interpolate import interp1d
over_model_fct = interp1d(x,y_noise, kind='cubic')
x_dense = np.linspace(0,1,200)
over_model = lt.ltPlotFct(x_dense,over_model_fct(x_dense), color='C2')

y_noise_2 = y_true + 0.019*np.random.normal(size=len(y_true))
points_2 = lt.ltPlotPts(x, y_noise_2, color='C3')

def LossMSE(a,b):
    return 0.5*((b-a)**2).mean()

errors = {
    1 : LossMSE(points.y, reglin.popt[0]*x+reglin.popt[1]),
    2 : LossMSE(points.y, y_true),
    3 : LossMSE(points.y, over_model_fct(x)),
    4 : LossMSE(points_2.y, reglin.popt[0]*x+reglin.popt[1]),
    5 : LossMSE(points_2.y, y_true),
    6 : LossMSE(points_2.y, over_model_fct(x))
}

# Définir le graphique
x_labels = [None, None, None, "Sous-entraînement", "Bon modèle", "Surentraînement"]
y_labels = ["Entraînement", None, None, "Validation", None, None]
for index in range(1,7):
    fig.addgraph(
        'graph{}'.format(str(index)),
        x_label = x_labels[index-1],
        y_label = y_labels[index-1],
        x_ticks = False,
        y_ticks = False,
        show_legend=False, legend_on_side=True,
        position = int(230+index),
    )

# Insérer les objets à tracer dans le plot
for index in range(1,4):
    points.plot(fig, 'graph{}'.format(str(index)))
for index in range(4,7):
    points_2.plot(fig, 'graph{}'.format(str(index)))

under_model.plot(fig, 'graph1')
good_model.plot(fig, 'graph2')
over_model.plot(fig, 'graph3')

under_model.plot(fig, 'graph4')
good_model.plot(fig, 'graph5')
over_model.plot(fig, 'graph6')

for k in errors:
    fig.graphs['graph{}'.format(k)].graph.annotate(
        r"MSE $= \num{"+str(np.round(errors[k]*10**4,3))+"}",
        xy=(.1,.8),
        xycoords='axes fraction'
    )

# Sauvegarder la figure
fig.save()

