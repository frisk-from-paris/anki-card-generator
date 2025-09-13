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

def lines_to_to_fill(lines: list[str], sep=",") -> list[dict]:
    notes = []
    for line in lines:
        if not is_valid_line(line, sep):
            continue
        parsed = line.split(sep)
        sentence = parsed[0]
        explanation = parsed[1]
        words = parsed[2:]
        obj = {"type": "to_fill", "obj": {"sentence": sentence.strip(), "words_to_hide": [w.strip() for w in words], "explanation": explanation}}
        notes.append(obj)
    return notes
