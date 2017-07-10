#!/bin/bash


mkdir build/files -p
cd build/files 
wget -O- get.pharo.org/60+vmT | bash
./pharo-ui Pharo eval --save " Metacello new baseline: 'Iceberg'; repository: 'github://npasserini/iceberg';load. Metacello new baseline: 'RedBubble'; repository: 'github://sbragagnolo/rb/pharo'; load. "
cd ..
cp ../*.sh .
cp ../*.st .
cp ../contracts . -r
rm build.sh 
cd .. 
