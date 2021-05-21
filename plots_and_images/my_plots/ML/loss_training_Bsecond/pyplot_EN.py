#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import ltLaTeXpyplot as lt

fig = lt.ltFigure(name='fig-loss_history_EN', width_frac = .7)

loss_values_train = np.array([3.46883468834688, 3.42953929539295, 3.40921409214092, 3.40243902439024, 3.39159891598916, 3.38346883468835, 3.38211382113821, 3.38753387533875, 3.37940379403794, 3.37262872628726, 3.36991869918699, 3.37262872628726, 3.36585365853659, 3.36178861788618, 3.3550135501355, 3.35636856368564, 3.35365853658537, 3.3550135501355, 3.34552845528455, 3.34417344173442, 3.31707317073171, 3.22493224932249, 3.17886, 3.13414634146341, 3.1219512195122, 3.10027100271003, 3.08943089430894, 3.10027100271003, 3.09349593495935, 3.07723577235772, 3.09078590785908, 3.07723577235772, 3.07588075880759, 3.07317073170732, 3.07181571815718, 3.06368563685637, 3.06233062330623, 3.05691056910569, 3.05691056910569, 3.05284552845528, 3.05691056910569, 3.04471544715447, 3.06910569105691, 3.05691056910569, 3.03929539295393, 3.04878048780488, 3.04878048780488, 3.04878048780488, 3.04742547425474, 3.02574525745257, 3.04065040650407, 3.04065040650407, 3.03523035230352, 3.02574525745257, 3.02574525745257, 3.02981029810298, 3.03523035230352, 3.02574525745257, 3.01490514905149])
loss_values_valid = np.array([3.80216802168022, 3.28861788617886, 3.51490514905149, 3.47560975609756, 3.38753387533875, 3.62466124661247, 3.39837398373984, 3.55826558265583, 3.34146341463415, 3.28726287262873, 3.4579945799458, 3.37940379403794, 3.63143631436314, 3.51761517615176, 3.44715447154472, 3.55826558265583, 3.1869918699187, 3.24390243902439, 3.98915989159892, 3.15176151761518, 3.53387533875339, 3.22222222222222, 3.04065040650407, 3.08943089430894, 3.06233062330623, 2.95934959349593, 3.20325203252033, 2.92140921409214, 3.10569105691057, 3.01084010840108, 3.10027100271003, 2.98644986449864, 3.10840108401084, 3.27913279132791, 2.94850948509485, 3.15176151761518, 3.13821138211382, 3.19783197831978, 2.94579945799458, 3.14363143631436, 3.19783197831978, 3.30894308943089, 3.13550135501355, 3.40379403794038, 3.03794037940379, 3.15718157181572, 2.95121951219512, 3.03523035230352, 3.30352303523035, 2.99728997289973, 3.18428184281843, 3.30352303523035, 3.24390243902439, 3.21680216802168, 2.97560975609756, 3.14905149051491, 3.26829268292683, 3.38482384823848, 3.19512195121951])
xs = np.arange(len(loss_values_valid))

loss_train = lt.ltPlotFct(xs, loss_values_train, label='Training data', color='C0')
loss_valid = lt.ltPlotFct(xs, loss_values_valid, label='Validation data', color='C1')

fig.addgraph('graph1', x_label='Epoch', y_label='Loss value', show_legend=True, legend_on_side=False)

for plot in [loss_train, loss_valid]:
    fig.addplot(plot, 'graph1')

fig.save()
