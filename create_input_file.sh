#!/bin/bash
name="input"$1".txt"
for (( counter=$1; counter>0; counter-- ))
do
	echo $RANDOM >> $name
done
