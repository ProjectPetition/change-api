#!/bin/bash
FILES=data/*
NEW_FILES=data/csv
for f in $FILES
do
    echo $f
    #python Json_To_Csv_Converter_main.py -i $f -o "$NEW_FILES '/' $f '.csv'"

done
