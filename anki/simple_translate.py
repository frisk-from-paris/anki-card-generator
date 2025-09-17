import genanki


templates = [
    {
        'name': 'French',
        'qfmt': '<p>{{Rule}}: </p><p>{{Farsi}} {{Symbols}}<br>{{type:French}}</p>',
        'afmt': '<p>{{FrontSide}}</p><p><hr>{{French}}</p>',
    },
    {
        'name': 'Farsi',
        'qfmt': '<p>{{Rule}}: </p><p>{{French}}<br>{{type:Farsi}}</p>',
        'afmt': '<p>{{FrontSide}}</p><p><hr>{{Farsi}} {{Symbols}}</p>',
    },

]


class SimpleTranslateModel(genanki.Model):
    def __init__(self, templates: list[dict]):
        self._templates = templates
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
    symbols: str = ""
    farsi: str
    french: str

    def __new__(cls, farsi: str, french: str, translate_to: str, symbols: str = ""):
        cls.farsi = farsi
        cls.french = french
        cls.symbols = symbols
        template_to_use = []

        for t in templates:
            if t["name"].casefold() == translate_to.casefold():
                template_to_use.append(t)
                break

        return genanki.Note(
            model = SimpleTranslateModel(templates=template_to_use),
            fields = [
                cls.rule,
                cls.farsi,
                cls.french,
                cls.symbols
            ]
        )
