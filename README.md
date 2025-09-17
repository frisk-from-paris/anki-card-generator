# Anki Card Generator

## Description

This project is meant to turn an excel sheet or any data format to anki notes.

## Types of notes

The code is built to be able to support multiple types of notes in the future.
For now, we support 'simple_translate' notes, which are cards with a sentence in french
and farsi. You can chose which cards you want generated (either french to persian or vice versa.)

### Simple Translate

A SimpleTranslate card is one that only expects a sentence and its translation.
It interprets a text file as following:

``` file.csv
type,sentence,translation,explanation,words_to_hide
simple_translate,my sentence,my translation,,
simple_translate,my second sentence,my second translation,,
```

### To Fill

A ToFill card is one that expects the user to fill a sentence with missing words.
In csv the separator for the words_to_hide is ';'.
It interprets a text file as following:

``` file.csv
type,sentence,translation,explanation,words_to_hide
to_fill,this is a sentence,,this is the explanation,a;this
```

** THIS TYPE IS CURRENTLY (17/09/2025) DEPRECATED. **

## Install and run

### Installation

Clone the repository, create a virtual environment and run :

```bash
pip install -r requirements.txt
```

### Run

usage: run.py [-h] [--directory DIRECTORY] [--name NAME] [--output OUTPUT] [--file FILE] --translate-to TRANSLATE_TO

options:
  -h, --help            show this help message and exit
  --directory, -d DIRECTORY
                        A folder with the cards to create.
  --name, -n NAME       The name of the deck.
  --output, -o OUTPUT   The path where to create the deck.
  --file, -f FILE       Use a single file.
  --translate-to, -t TRANSLATE_TO
                        Which way should the translation go (persian or french).

### Example

To generate notes from the file 'test.csv' and export a deck named 'pishi-deck' to a folder named 'output' which translate_to french:

```bash
python run.py -f test.csv -o output -n pishi-deck -t french
```

A pishi-deck.apkg is now inside your output folder, and you can import it in your anki app.
