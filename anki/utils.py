import genanki

import os
import random

from .simple_translate import SimpleTranslateNote


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


def export(
	    deck_name: str,
	    notes: list[genanki.Note],
	    output_dir: str = "output"
	) -> None:
    """ Export a deck of notes. """
    deck_id = random.randint(10**9, 10**10)
    deck = genanki.Deck(
        deck_id,
        deck_name
    )

    for note in notes:
        deck.add_note(note)

    print(f"Writing deck {deck_name}...")
    genanki.Package(deck).write_to_file(os.path.join(output_dir, deck_name + ".apkg"))
    print(f"Deck {deck_name} written.")
