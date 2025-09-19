import genanki

import os
import random

from .models.simple_translate import SimpleTranslateNote
from .models.conjugate import ConjugateNote


def create_notes(all_notes: dict, translate_to: str):
    """ create multiple notes """
    results = []
    for type_, notes in all_notes.items():
        if type_ == "simple_translate":
            for note in notes:
                new_note = SimpleTranslateNote(note["farsi"], note["french"], translate_to, note.get("symbols", ""))
                results.append(new_note)
        if type_ == "conjugate":
            for note in notes:
                farsi_verbs=[note["far_" + str(i)] for i in range(6)]
                french_verbs=[note["fre_" + str(i)] for i in range(6)]
                new_note = ConjugateNote(
                    infinitive=note["infinitive"],
                    farsi_verbs=farsi_verbs,
                    french_verbs=french_verbs,
                    translate_to=translate_to
                )
                results.append(new_note)
        else:
            #raise NotImplementedError(f"Type {type_} does not exist")
            print(f"Type {type_} does not exist")
    return results

