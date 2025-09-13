def is_valid_line(line: str, sep: str) -> bool:
    return bool(
        line
        and sep in line
        and not line.startswith("#")
    )

def lines_to_simple_translate(lines: list[str], sep=",") -> list[dict]:
    """ Convert a list of lines into their simple_translate dict obj. """
    notes = []
    for line in lines:
        if not is_valid_line(line, sep):
            continue
        sentence, translation = line.split(sep)
        obj = {"type": "simple_translate", "obj": {"sentence": sentence.strip(), "translation": translation.strip()}}
        notes.append(obj)
    return notes
