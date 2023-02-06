#!/bin/bash

echo Removing old repo...
git rm -r prog_ciencia_dados
git commit -m 'old repo removed'

echo Copying new data...
cp -r ../../git/prog_ciencia_dados/book/_build/html ./prog_ciencia_dados
git add prog_ciencia_dados/
git commit -m 'book update'

echo Uploading..
git push

echo Done.

