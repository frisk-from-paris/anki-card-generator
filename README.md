# Anki Card Generator

## Description

This project aims at easily converting data files to a deck of Anki cards.

## Types of cards

### Simple Translate

A SimpleTranslate card is one that only expects a sentence and its translation.
It interprets a text file as following:

``` file.txt
my sentence,my translation
my second sentence,my second translation
```

### To Fill

A ToFill card is one that expects the user to fill a sentence with missing words.
It interprets a text file as following:

``` file.txt
this is a sentence,this is the explanation,a
```

Here, you have the full sentence, followed by the explanation on why the missing word(s) is this,
then as many missing as you need in the end.


## Install and run

A CLI + Pypi is incomming.

## Compatible files

For now it's working with special text files but it will soon accept multiple types of files.
