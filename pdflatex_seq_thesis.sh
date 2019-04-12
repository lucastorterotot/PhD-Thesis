#!/bin/bash
cd ~/Documents/PhD-Thesis/
for file in $(grep --include="*.tex" --include="*.pgf" --exclude="homedirs.tex" -rlHm1 $HOME) ; do
    echo '  '$file
    sed -i "s|$HOME|\\\homedir|g" $file
done
nbcompilmax=5
file=LT-These-main
pdflatex -draftmode $file
sleep 0.25
if [ -e $file.bcf ]; then biber $file ; fi &
if [ -e $file.idx ]; then makeindex $file.idx ; fi &
bash ~/Dropbox/scripts_bash/feynmp_compil.sh &
wait
sleep 0.25
pdflatex $file
nbcompil=2
while [[ $(grep -rlm1 --include="*.log" -e 'Rerun to get cross-references right' -e 'undefined references' -e 'undefined on input line') == *$file.log* ]] && ((nbcompil < nbcompilmax)); do
    pdflatex $file
    ((nbcompil+=1))
done
printf '\n\t' ; printf $nbcompil ; printf ' compilations.\n\n'
# rm -f *.1 *.mp *.t1 &
# rm -f $file.aux $file.out $file.toc $file.lof $file.nav $file.snm $file.synctex.gz $file.maf $file.mtc $file.ptc $file.bcf $file.bbl $file.run.xml $file-blx.bib $file.idx $file.ilg $file.ind &
