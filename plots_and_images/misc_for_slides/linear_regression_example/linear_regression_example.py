#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Example taken from

import numpy as np
import ltLaTeXpyplot as lt
import os

data_file = "data.txt"

cols = np.genfromtxt(data_file,dtype='str')[0]
data = {}

def None_values(var):
    if any([s in var for s in ["PT"]]):
        return 0
    return -99

def get_binning(var):
    _min = 10
    _max = 160
    _step = 10
    if any([s in var for s in ["_E"]]):
        _min = 0
        _max = 1000
        _step = 20
    if any([s in var for s in ["Charge"]]):
        _min = -2
        _max = 2
        _step = .5
    if any([s in var for s in ["Eta"]]):
        _min = -2.5
        _max = 2.1
        _step = .1
    if any([s in var for s in ["Mass"]]):
        if "Higgs" in var:
            _min = 0
            _max = 500
            _step = 10
        elif "jet" in var:
            _min = 0
            _max = 60
            _step = 5
        elif "tau" in var:
            _min = 0
            _max = 2
            _step = .1
        else:
            _min = 0
            _max = 30
            _step = 3          
    if any([s in var for s in ["Phi"]]):
        _min = -np.pi
        _max = np.pi
        _step = .1
    return np.arange(_min, _max+_step, _step)

for k in range(len(cols)):
    col = cols[k]
    dtype='float'
    if any([s in col for s in ["DM1_", "DM2_", "channel"]]):
        dtype='str'
    _data = np.genfromtxt(data_file, dtype=dtype, usecols = k)[1:]
    if dtype!='str':
        data[col] = np.where(np.isnan(_data) , None_values(col), _data)

# mt tot
var = "mt_tot"
for ana in ["reco", "gen"]:
    data["_".join([var, ana])] = (
        (
            2 * (
                data["_".join(["tau1_PT", ana])] * np.cos(data["_".join(["tau1_Phi", ana])])
            ) * (
                data["_".join(["tau2_PT", ana])] * np.cos(data["_".join(["tau2_Phi", ana])])
            ) * (
                1-np.cos((data["_".join(["tau1_Phi", ana])])*(data["_".join(["tau2_Phi", ana])]))
            )
        ) + (
            2 * (
                data["_".join(["MET_PT", ana])] * np.cos(data["_".join(["MET_Phi", ana])])
            ) * (
                data["_".join(["tau2_PT", ana])] * np.cos(data["_".join(["tau2_Phi", ana])])
            ) * (
                1-np.cos((data["_".join(["MET_Phi", ana])])*(data["_".join(["tau2_Phi", ana])]))
            )
        ) + (
            2 * (
                data["_".join(["MET_PT", ana])] * np.cos(data["_".join(["MET_Phi", ana])])
            ) * (
                data["_".join(["tau1_PT", ana])] * np.cos(data["_".join(["tau1_Phi", ana])])
            ) * (
                1-np.cos((data["_".join(["MET_Phi", ana])])*(data["_".join(["tau1_Phi", ana])]))
            )
        )
    )**.5

# os.system("mkdir -p vars")
# for var in data:
#     if not isinstance(data[var][0], float):
#         continue
#     if any([s in var for s in ["Event", "PID", "IsPU", "D0", "DZ", "METcov"]]):
#         continue
#     fig = lt.ltFigure(name='vars/{}'.format(var))
#     fig.addgraph('graph1', x_label=var, y_label='$N$ events', show_legend=False)
#     hist = lt.ltPlotHist(data=data[var], bins=get_binning(var))
#     hist.plot_pts(fig, 'graph1')
#     fig.save(format='pdf')
#     fig.close()
# 
# # MET ellipses
# scale = 10
# fig = lt.ltFigure(name='METcov_ellipses', height_width_ratio = 1)
# N_ellipse_max = 200
# N_ellipse = 0
# fig.addgraph('graph1', x_label='$x$', y_label='$y$', show_legend=False, title="${}\\times$ scaled METcov ellipses centered on MET vector".format(scale))
# for k in range(len(data["Event"])):
#     if N_ellipse >= N_ellipse_max:
#         break
#     # Get MET position
#     phi = data["MET_Phi_reco"][k]
#     X = data["MET_PT_reco"][k] * np.cos(phi)
#     Y = data["MET_PT_reco"][k] * np.sin(phi)
#     # define matrix
#     # see https://cookierobotics.com/007/
#     a = data["METcov_xx_reco"][k]
#     b = data["METcov_xy_reco"][k]
#     c = data["METcov_yy_reco"][k]
#     l1 = (a+c)/2 + (((a-c)/2)**2+b**2)**.5
#     l2 = (a+c)/2 - (((a-c)/2)**2+b**2)**.5
#     if b == 0 and a >= c:
#         theta = 0
#     elif b == 0 and a < c:
#         theta = np.pi /2
#     else:
#         theta = np.arctan((l1-a)/b)**2
#     t = np.linspace(0, 2*np.pi, 100)
#     x = X + (l1**.5 * np.cos(theta) * np.cos(t) - l2**.5 * np.sin(theta) * np.sin(t))*scale
#     y = Y + (l1**.5 * np.sin(theta) * np.cos(t) + l2**.5 * np.cos(theta) * np.sin(t))*scale
# 
#     # default color
#     color = "C0"
#     # check angle difference between ellipse axis and position
#     angle = abs(theta - phi)
#     while angle >= np.pi : # ellipses are pi-invariant
#         angle -= np.pi
#     if angle > np.pi/4: # if not aligned
#         color = "C3"
#     if angle < np.pi/4: # if well aligned
#         color = "C2"
#     if abs(1-(l2/l1)**.5) < .25: # if ellispe is close to circle
#         color = "C0"
#     if abs(1-(l2/l1)**.5) > .25:
#         N_ellipse += 1
#         lt.ltPlotFct(x, y, color=color).plot(fig, 'graph1')
# 
# lt.ltPlotPts([0], [0], color='red', marker="o").plot(fig, 'graph1')
# fig.save(format='pdf')
# fig.close()
# 
# # Gen/reco comparison
# os.system("mkdir -p gen_vs_reco")
# for recovar in data:
#     if not "_reco" in recovar:
#         continue
#     basevar = recovar[:-5]
#     genvar = "_".join([basevar, "gen"])
#     if not genvar in data:
#         continue
#     fig = lt.ltFigure(name='gen_vs_reco/{}'.format(basevar))
#     x_min = get_binning(recovar)[0]
#     x_max = get_binning(recovar)[-1]
#     y_min = get_binning(genvar)[0]
#     y_max = get_binning(genvar)[-1]
#     fig.addgraph('graph1', x_label=recovar, y_label=genvar, show_legend=False,
#                  x_min = x_min, x_max = x_max,
#                  y_min = y_min, y_max = y_max,
#     )
#     points = lt.ltPlotPts(data[recovar][:1000], data[genvar][:1000])
#     points.plot(fig, 'graph1')
#     lt.ltPlotFct([y_min, y_max], [y_min, y_max], color='C3').plot(fig, 'graph1')
#     fig.save(format='pdf')
#     fig.close()

# fig2 = lt.ltFigure(name='MET')
# fig2.addgraph('graph1', x_label='MET', y_label='N events', show_legend=False)
# hist = lt.ltPlotHist(data=data["MET_PT"], bins=15, range=[0,150], fill=True)

# hist.plot(fig2, 'graph1')
# fig2.save(format='pdf')
# Create figure
fig = lt.ltFigure(name='fig-linear_regression_example')

# Define what to plot
# data
_x = data["MET_PT_gen"]
_y = data["MET_PT_reco"]
x = _x[np.isnan(_y) != True]
y = _y[np.isnan(_y) != True]
# uncertainties (1 sigma)
ux = x/100
uy = y/100
reg = lt.ltPlotRegLin(x, y, ux, uy, info_placement='lower right', label='Data', label_reg='Regression')

# Définir le graphique
fig.addgraph('graph1', x_label='True value (a.u.)', y_label='Measured value (a.u.)', show_legend=True, x_min=0, x_max=175, y_min=0, y_max=175)

# Insérer les objets à tracer dans le plot
reg.reglin.plot(fig, 'graph1')
reg.plot_pts(fig, 'graph1')

# Sauvegarder la figure
fig.save()
