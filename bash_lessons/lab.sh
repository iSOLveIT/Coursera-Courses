#!/bin/bash

> oldFiles.txt
files=$(grep 'mesg' ~/list.txt)
for file in $files; do
  if test -e ~/$file; then
    filename=$HOME$file
    echo $filename >> oldFiles.txt
  fi
done
