#!/bin/bash

cernusername=ltortero
localoutputdir=$lt_PhD_thesis_dir/contents/chapter-JERC/plots/

mkdir -p $localoutputdir ; cd $localoutputdir
plotsdirbase=$(pwd)
lxplusoutput=$1
lxplusdate=$2
year=$3
run=$4

if [ "$lxplusoutput" == "JER" ] ; then
    lxplusdirbase=/afs/cern.ch/work/${cernusername::1}/$cernusername/JEC-task/JER_CMSSWs/CMSSW_8_0_25/src/JetMETCorrections/GammaJetFilter/
else
    lxplusdirbase=/afs/cern.ch/work/${cernusername::1}/$cernusername/JEC-task/CMSSW_8_0_25/src/JetMETCorrections/GammaJetFilter/
fi

echo ''
echo 'Importing plots from lxplus...'
echo ''
alpha='0_3'
echo '  Run '$year' '$run', '$lxplusoutput', from '$lxplusdate', alpha '$alpha
plotsdir=$lxplusoutput/Run$year$run/alpha_$alpha/
lxplusdir=PhotonJetPlots_DATA_$lxplusoutput'_'$alpha'_'$lxplusdate'_'$run'_'$lxplusoutput'_vs_MC_'$lxplusoutput'_'$alpha'_'$lxplusdate'_'$run'_'$lxplusoutput'_PFlowAK4chs_LUMI'
mkdir -p $plotsdirbase/$plotsdir/
rsync -auh --progress $cernusername@lxplus.cern.ch:$lxplusdirbase/$lxplusdir/{ptPhoton,ptFirstJet,ptSecondJet,MET}_log.pdf $plotsdirbase/$plotsdir/
echo ''
