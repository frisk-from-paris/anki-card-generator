def lines_to_simple_translate(lines: list[str], sep=",") -> list[dict]:
    """ Convert a list of lines into their simple_translate dict obj. """
    notes = []
    for line in lines:
        sentence, translation = line.split(sep)
        obj = {"type": "simple_translate", "obj": {"sentence": sentence.strip(), "translation": translation.strip()}}
        notes.append(obj)
    return notes
