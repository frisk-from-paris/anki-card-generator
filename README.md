# Anki Card Generator

## Description

This project aims at easily converting data files to a deck of Anki cards.

## Types of cards

In one file you can have multiple types of notes, which are the following

### Simple Translate

A SimpleTranslate card is one that only expects a sentence and its translation.
It interprets a text file as following:

``` file.txt
simple_translate,my sentence,my translation
simple_translate,my second sentence,my second translation
```

### To Fill

A ToFill card is one that expects the user to fill a sentence with missing words.
It interprets a text file as following:

``` file.txt
to_fill,this is a sentence,this is the explanation,a,this
```

Here, you have the full sentence, followed by the explanation on why the missing word(s) is this,
then as many missing as you need in the end.


## Install and run

python run.py --directroy 'folder where data is present' --output 'output folder' --name 'deck name'

## Compatible files

For now it's working with special text files but it will soon accept multiple types of files.
