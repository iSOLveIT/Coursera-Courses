#!/bin/bash

# n=1
# # -le => Less than 
# while [ $n -le 5 ]; do
#   echo "Iteration number $n"
#   # ((arithmetic calcs)) allows us to do arithmetic calculations
#   ((n+=1))
# done;

# n=0
# command=$1
# while ! $command && [ $n -le 5 ]; do
#   sleep $n
#   ((n=n+1))
#   echo "Retry #$n"
# done;

for fruit in peach orange apple;
do
  echo "I like $fruit"
done

for file in *.HTM;
do
  name=$(basename "$file" .HTM)
  mv "$file" "$name.html"
done