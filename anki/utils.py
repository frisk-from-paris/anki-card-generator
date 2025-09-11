from .to_fill import ToFillNote
from .simple_translate import SimpleTranslateNote


def create_note(note: dict):
    """ Create a note object from a note schema. """
    note_type = note.get("type")
    obj = note["obj"]
    if note_type == "to_fill":
        return ToFillNote(**obj)
    elif note_type == "simple_translate":
        return SimpleTranslateNote(**obj)
