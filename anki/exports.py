import genanki

import os
import random


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
