#!/bin/sh

INPUT_FILE=input
echo "" > $INPUT_FILE

for i in {1..1000000}
do
	n=$((RANDOM%100))
	val=$((RANDOM % 100))
	echo $n $val >> $INPUT_FILE
done
