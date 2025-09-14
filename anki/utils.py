import genanki

import os
import random
from types import SimpleNamespace

from .to_fill import ToFillNote
from .simple_translate import SimpleTranslateNote


def create_note(type_: str, note: dict):
    """ Create a note object from a note schema. """
    note_np = SimpleNamespace(**note)
    if type_ == "to_fill":
        return ToFillNote(
            note_np.sentence,
            note_np.explanation,
            note_np.words_to_fill
        )
    elif type_ == "simple_translate":
        return SimpleTranslateNote(note_np.sentence, note_np.translation)
    else:
        raise NotImplementedError("Type does not exist")

def create_notes(notes: list[dict]):
    """ create multiple notes """
    results = []
    for type_, notes in notes.items():
        if type_ == "to_fill":
            for note in notes:
                note_np = SimpleNamespace(**note)
                results.append(ToFillNote(
                    note_np.sentence,
                    note_np.words_to_fill,
                    note_np.explanation
                    )
                )
        elif type_ == "simple_translate":
            for note in notes:
                note_np = SimpleNamespace(**note)
                results.append(SimpleTranslateNote(note_np.sentence, note_np.translation))
        else:
            raise NotImplementedError("Type does not exist")
    return results


def export(
	    deck_name: str,
	    notes: list[genanki.Note],
	    output_dir: str = "output"
	) -> None:
    """Export a deck of notes. """
    deck_id = random.randint(10**9, 10**10)
    deck = genanki.Deck(
        deck_id,
        deck_name
    )
    for note in notes:
        deck.add_note(note)
    print("writing deck ...")
    genanki.Package(deck).write_to_file(os.path.join(output_dir, deck_name + ".apkg"))
    print("deck written.")
