#!/bin/bash

masses=(600 800 1000 1200 1400 1600 1800 2000 2500 3000 3500 4000 4500)
sample=Wprime_WZ_WlepZlep

postfix=(_run_card.dat _customizecards.dat _proc_card.dat _extramodels.dat)

echo ${masses[*]}

for mass in ${masses[*]}; do
    echo generating cards for $sample M = $mass GeV

    mkdir ${sample}${mass}

    for i in {0..3}; do
        sed "s/<MASS>/${mass}/g" ${sample}/${sample}${postfix[$i]} > ${sample}$mass/${sample}$mass${postfix[$i]}
    done
done
