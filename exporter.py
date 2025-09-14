import os
import random

import genanki


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
    print(deck)
