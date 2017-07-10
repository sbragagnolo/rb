#!/bin/bash


mkdir build/files -p
cd build/ 
wget -O- get.pharo.org/60+vmT | bash
./pharo-ui Pharo eval --save "Pharo3Theme beCurrent. Metacello new baseline: 'Iceberg'; repository: 'github://pharo-vcs/iceberg';load. Metacello new baseline: 'RedBubble'; repository: 'github://sbragagnolo/rb/pharo'; load. "
cd .. 
