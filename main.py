import os

from anki import create_notes

from converters import lines_to_simple_translate, lines_to_to_fill
from exporter import export


DB_FOLDER = "data"
simple_file = os.path.abspath(os.path.join(DB_FOLDER, "simple_translate.txt"))
to_fill_file = os.path.abspath(os.path.join(DB_FOLDER, "to_fill.txt"))

with open(simple_file, "r") as f:
    simple_lines = f.readlines()

with open(to_fill_file, "r") as f:
    to_fill_lines = f.readlines()

simple_objs = lines_to_simple_translate(simple_lines)
simple_notes = create_notes(simple_objs)

to_fill_objs = lines_to_to_fill(to_fill_lines)
to_fill_notes = create_notes(to_fill_objs)

all_notes = []
#all_notes.extend(simple_notes)
all_notes.extend(to_fill_notes)

export("persian", all_notes, "output")
