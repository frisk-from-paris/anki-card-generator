import genanki


class ToFillModel(genanki.Model):
    """ This is the genanki Model for the cards the user has "to fill".
    It has 3 fields :
        Text, Rule and Explanation.

    It is based on the built-in genanki.Model.CLOZE model.
    """
    def __init__(self):
        super().__init__(
            1550428389,
            'Cloze To Fill',
            model_type=genanki.Model.CLOZE,
            fields=[
                {
                'name': 'Text',
                'font': 'Arial',
                },
                {
                'name': 'Rule',
                'font': 'Arial',
                },
                {
                'name': 'Explanation',
                'font': 'Arial',
                }
            ],
            templates=[
                {
                'name': 'Cloze',
                'qfmt': '{{Rule}}<br>{{cloze:Text}}<br>{{type:Text}}',
                'afmt': '{{FrontSide}}<hr>{{Explanation}}',
                },
            ]
        )


class ToFillNote:
    rule: str = "Compléter les mots manquants"
    explanation: str = ""
    cloze_text: str = ""

    def __new__(cls, sentence: str, words_to_hide: list[str], explanation: str = ""):
        c_text = sentence
        for i, word in enumerate(words_to_hide, start=1):
            c_text = c_text.replace(word, f"{{{{c{i}::{word}}}}}")

        cls.cloze_text = c_text
        cls.explanation = "Explication: " + explanation

        return genanki.Note(
            model = ToFillModel(),
            fields = [
                cls.cloze_text,
                cls.rule,
                cls.explanation
            ]
        )

