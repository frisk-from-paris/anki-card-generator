import os

from anki import create_note

from converters import lines_to_simple_translate
from exporter import export


DB_FOLDER = "data"
simple_file = os.path.abspath(os.path.join(DB_FOLDER, "simple_translate.txt"))

print(simple_file)
with open(simple_file, "r") as f:
    lines = f.readlines()

objs = lines_to_simple_translate(lines)
notes = [create_note(obj) for obj in objs]

export("persian", notes, "output")
