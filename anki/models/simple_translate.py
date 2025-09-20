import genanki


TEMPLATES = {
    "french":
    {
        'name': 'French',
        'qfmt': '<p>{{Rule}}: </p><p>{{Farsi}} {{Symbols}}<br>{{type:French}}</p>',
        'afmt': '<p>{{FrontSide}}</p><p><hr>{{French}}</p>',
    },
    "farsi": {
        'name': 'Farsi',
        'qfmt': '<p>{{Rule}}: </p><p>{{French}}<br>{{type:Farsi}}</p>',
        'afmt': '<p>{{FrontSide}}</p><p><hr>{{Farsi}} {{Symbols}}</p>',
    },
}


class SimpleTranslateModel(genanki.Model):
    def __init__(self, templates: list[dict]):
        super().__init__(
            1305534440,
            'Basic (type in the answer)',
            fields=[
                {
                'name': 'Rule',
                'font': 'Arial',
                },
                {
                'name': 'Farsi',
                'font': 'Arial',
                },
                {
                'name': 'French',
                'font': 'Arial',
                },
                {
                'name': 'Symbols',
                'font': 'Arial',
                },
            ],
            templates=templates
        )


class SimpleTranslateNote:
    rule: str = "Translate the sentence"
    symbols: str
    farsi: str
    french: str

    def __new__(cls, farsi: str, french: str, translate_to: str, symbols: str = ""):
        cls.farsi = farsi
        cls.french = french
        cls.symbols = symbols

        templates = TEMPLATES[translate_to]

        fields = []
        fields.append(cls.rule)
        fields.append(farsi)
        fields.append(french)
        fields.append(symbols)

        return genanki.Note(
            model = SimpleTranslateModel(templates=[templates]),
            fields = fields
        )
