#!/bin/bash

echo ''
echo ''
echo 'Importing plot files from lyovis10 ...'
mkdir -p $lt_PhD_thesis_dir/plots_and_images/my_plots/ML/from_ML_plots
#rsync -auh --delete --progress --stats --exclude='__pycache__' --include='*.pdf' --include='*/' --exclude='*' lyovis10:/data2/ltorterotot/ML/ ~/Documents/ML_plots/
rsync -auh --progress --stats --exclude='__pycache__' --include='*.pdf' --include='*/' --exclude='*' lyovis10:/data2/ltorterotot/ML/ $lt_PhD_thesis_dir/plots_and_images/my_plots/ML/from_ML_plots/
echo ''
echo ''
