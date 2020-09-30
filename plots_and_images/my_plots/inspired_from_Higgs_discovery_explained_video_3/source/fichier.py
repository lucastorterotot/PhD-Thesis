#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

import ltLaTeXpyplot as lt

# 6 faces sur un dé
dice_possibilities = [p for p in range(1,7)]
dice_possibilities.sort()

# le lapin tourne le dé sur 3
signal_value_real = 3

# le lapin est timide ( xsec analogy )
# et ne se manifeste qu'une fraction des jours
shyness_real = .05
    
# binning
binning = [p-0.5 for p in dice_possibilities]
binning.append(dice_possibilities[-1]+0.5)

# samples
#np.random.seed(3)
np.random.seed(16)

background = np.arange(1,7)
    
background_for_data_orig = np.random.uniform(
    low = binning[0],
    high = binning[-1],
    size = 10000,
)
#background_for_data_orig = background_for_data_orig.astype('int')
    
def get_samples(N_samples):
    background_for_data = background_for_data_orig[:int(N_samples*(1-shyness_real))]
    
    signal_real = signal_value_real * np.ones(int(N_samples*shyness_real))
    
    data = lt.ltPlotHist(data=np.concatenate([background_for_data, signal_real]), bins=binning, label="Données", color='black')
    bg_for_data = lt.ltPlotHist(data=background_for_data, bins=binning, label="BG", color = 'C9')
    bg = lt.ltPlotHist(data=background, weights = N_samples/len(background)*np.ones(len(background)), bins=binning, label="BG", color = 'C9')
    SR = lt.ltPlotHist(data=signal_real, bins=binning, label="Real signal", color='C3')
    SR_bak = lt.ltPlotHist(data=signal_real, bins=binning, label="Real signal", color='C3')

    return N_samples, data, bg_for_data, bg, SR, SR_bak


# Créer les figures
fig = lt.ltFigure(
    name='1-only_data_100',
    height_width_ratio = 2,
    tight_layout=True,
)
fig_for_ratio = lt.ltFigure(
    name='fig',
    height_width_ratio = 2,
    tight_layout=True,
)
fig2 = lt.ltFigure(
    name='fig2',
    height_width_ratio = 2,
    tight_layout=True,
)
    
# Définir les graphiques de base
fig.addgraph(
    'graph1',
    position=211,
    x_label='Valeur du dé',
    y_label='$N$',
    show_legend=True,
    legend_on_side=False,
    x_min = 0.5,
    x_max = 6.5,
    y_min = 0,
    y_max = 30,
)

fig_for_ratio.addgraph(
    'graph1',
    position=211,
    x_label=None,
    y_label='$N$',
    show_legend=True,
    legend_on_side=False,
    x_ticks = False,
    x_min = 0.5,
    x_max = 6.5,
    y_min = 0,
    y_max = 30,
)

fig2.addgraph(
    'graph1',
    position=211,
    x_label=None,
    y_label='$N$',
    show_legend=True,
    legend_on_side=False,
    x_ticks = False,
    x_min = 0.5,
    x_max = 6.5,
    y_min = 0,
    y_max = 10000,
)

# Cas à 100 essais
N_samples, data, bg_for_data, bg, SR, SR_bak = get_samples(100)
data.plot_pts(fig, 'graph1')
fig.save(format='pgf')
fig.x_label = None

# ajouter estimation bg
fig.name = '2-data_and_bg_estim_100'

bg.plot_stack(fig, 'graph1', [bg])
fig.save(format='pgf')

# ajouter ratio plot
fig = fig_for_ratio
fig.addgraph(
    'graph2',
    position=814,
    x_label='Valeur du dé',
    y_label='Obs./Bg.',
    show_legend=False,
    legend_on_side=False,
    share_x='graph1',
    y_min = 0,
    y_max = 2,
)
fig.name = '3-data_and_bg_estim_ratio_100'

data.plot_pts(fig, 'graph1')
bg.plot_stack(fig, 'graph1', [bg])

def get_ratio_plot(data, bg, SR_bak):
    bg_for_data.plot_stack(fig2, 'graph1', [SR, bg_for_data])

    data_over_MC_x = []
    data_over_MC_y = []
    data_over_MC_y_err = []
    
    data_over_MC_SR_x = []
    data_over_MC_SR_y = []
    data_over_MC_SR_y_err = []
    
    for dice_value in dice_possibilities:
        data_over_MC_x.append(dice_value)
        data_over_MC_y.append(data.y[dice_value-1]/bg.y[dice_value-1])
        data_over_MC_y_err.append(
            (data.y[dice_value-1]/bg.y[dice_value-1]**2 + bg.y[dice_value-1] * (data.y[dice_value-1]/bg.y[dice_value-1]**2)**2)**.5
        )
        
        data_over_MC_SR_x.append(dice_value)
        data_over_MC_SR_y.append(data.y[dice_value-1]/(bg.y[dice_value-1]*(1-shyness_real)+SR_bak.y[dice_value-1]))
        data_over_MC_SR_y_err.append(
            (data.y[dice_value-1]/(bg.y[dice_value-1]*(1-shyness_real)+SR_bak.y[dice_value-1])**2 + (bg.y[dice_value-1]*(1-shyness_real)+SR_bak.y[dice_value-1]) * (data.y[dice_value-1]/(bg.y[dice_value-1]*(1-shyness_real)+SR_bak.y[dice_value-1])**2)**2)**.5
        )

    return data_over_MC_x, data_over_MC_y, data_over_MC_y_err, data_over_MC_SR_x, data_over_MC_SR_y, data_over_MC_SR_y_err

data_over_MC_x, data_over_MC_y, data_over_MC_y_err, data_over_MC_SR_x, data_over_MC_SR_y, data_over_MC_SR_y_err = get_ratio_plot(data, bg, SR_bak)
data_over_MC = lt.ltPlotPts(data_over_MC_x, data_over_MC_y, yerr = data_over_MC_y_err, marker='o', color = 'black')
data_over_MC_SR = lt.ltPlotPts(data_over_MC_SR_x, data_over_MC_SR_y, yerr = data_over_MC_SR_y_err, marker='s', color = 'C3')
data_over_MC.plot(fig, 'graph2')
#data_over_MC_SR.plot(fig, 'graph2')

lt.ltPlotFct([0,7], [1,1], color='black', linewidth=.5).plot(fig, 'graph2')

fig.save(format='pgf')

# refaire 100 mais échelle différente
fig.name = '4-up_to_100'
fig.graphs['graph1'].y_max = 2500
fig.graphs['graph2'].y_max = 1.5
fig.graphs['graph2'].y_min = 0.5
fig.save(format='pgf')

# cas de 1000 à 10000
N_fig=4
N_samples_to_plot = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10000]
for N_samples in N_samples_to_plot:
    N_fig+=1
    if N_fig != 4 + len(N_samples_to_plot):
        N_samples, data, bg_for_data, bg, SR, SR_bak = get_samples(N_samples)
        data_over_MC_x, data_over_MC_y, data_over_MC_y_err, data_over_MC_SR_x, data_over_MC_SR_y, data_over_MC_SR_y_err = get_ratio_plot(data, bg, SR_bak)

    fig = lt.ltFigure(
        name='{}-up_to_{}'.format(N_fig, N_samples),
        height_width_ratio = 2,
        tight_layout=True,
    )
    fig.addgraph(
        'graph1',
        position=211,
        x_label=None,
        y_label='$N$',
        show_legend=True,
        legend_on_side=False,
        x_ticks = False,
        x_min = 0.5,
        x_max = 6.5,
        y_min = 0,
        y_max = 2500,
    )
    fig.addgraph(
        'graph2',
        position=814,
        x_label='Valeur du dé',
        y_label='Obs./Bg.',
        show_legend=False,
        legend_on_side=False,
        share_x='graph1',
        y_min = 0.5,
        y_max = 1.5,
    )
    
    data.plot_pts(fig, 'graph1')
    bg.plot_stack(fig, 'graph1', [bg])
    
    data_over_MC = lt.ltPlotPts(data_over_MC_x, data_over_MC_y, yerr = data_over_MC_y_err, marker='o', color = 'black')
    data_over_MC_SR = lt.ltPlotPts(data_over_MC_SR_x, data_over_MC_SR_y, yerr = data_over_MC_SR_y_err, marker='s', color = 'C3')
    data_over_MC.plot(fig, 'graph2')
    if N_fig == 4 + len(N_samples_to_plot):
        data_over_MC_SR.plot(fig, 'graph2')
        fig.name += "_SR"
        xs = [0]
        ys = [0]
        for dice_value in dice_possibilities:
            xs.append(dice_value-.5)
            xs.append(dice_value-.5)
            ys.append(ys[-1])
            if dice_value != signal_value_real:
                ys.append(N_samples * (1-shyness_real) * 1./6)
            else:
                ys.append(N_samples * (1-shyness_real) * 1./6 + N_samples * shyness_real)
        xs.append(xs[-1]+1)
        ys.append(ys[-1])
        lt.ltPlotFct(xs, ys, color='C3', label = "Lapin, 3").plot(fig, 'graph1')
        
    lt.ltPlotFct([0,7], [1,1], color='black', linewidth=.5).plot(fig, 'graph2')
    
    fig.save(format='pgf')
