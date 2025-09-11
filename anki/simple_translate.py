import genanki


class SimpleTranslateModel(genanki.Model):
    def __init__(self):
        super().__init__(
            1305534440,
            'Basic (type in the answer)',
            fields=[
                {
                'name': 'Sentence',
                'font': 'Arial',
                },
                {
                'name': 'Rule',
                'font': 'Arial',
                },
                {
                'name': 'Translation',
                'font': 'Arial',
                },
            ],
            templates=[
                {
                'name': 'To Persian',
                'qfmt': '{{Rule}}\n\n{{Sentence}}',
                'afmt': '{{FrontSide}}<hr>{{Translation}}',
                },
            ],
            css='.card {\n font-family: arial;\n font-size: 20px;\n text-align: center;\n color: black;\n background-color: white;\n}\n',
        )


class SimpleTranslateNote:
    rule: str = "Traduire la phrase"
    sentence: str = ""
    translation: str = ""

    def __new__(cls, sentence: str, translation: str):
        cls.sentence = sentence
        cls.translation = translation

        return genanki.Note(
            model = SimpleTranslateModel(),
            fields = [
                cls.rule,
                cls.sentence,
                cls.translation
            ]
        )
