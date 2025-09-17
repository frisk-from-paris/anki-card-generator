import genanki

import os
import random

from .models.simple_translate import SimpleTranslateNote


def create_notes(all_notes: dict, translate_to: str):
    """ create multiple notes """
    results = []
    for type_, notes in all_notes.items():
        if type_ == "simple_translate":
            for note in notes:
                new_note = SimpleTranslateNote(note["farsi"], note["french"], translate_to, note.get("symbols", ""))
                results.append(new_note)
        else:
            #raise NotImplementedError(f"Type {type_} does not exist")
            print(f"Type {type_} does not exist")
    return results

