import genanki


class SimpleTranslateModel(genanki.Model):
    def __init__(self):
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
            ],
            templates=[
                {
                'name': 'French',
                'qfmt': '<p>{{Rule}}: </p><p>{{Farsi}}<br>{{type:French}}</p>',
                'afmt': '<p>{{FrontSide}}</p><p><hr>{{French}}</p>',
                },
                {
                'name': 'Persian',
                'qfmt': '<p>{{Rule}}: </p><p>{{French}}<br>{{type:Farsi}}</p>',
                'afmt': '<p>{{FrontSide}}</p><p><hr>{{Farsi}}</p>',
                },

            ]
        )


class SimpleTranslateNote:
    rule: str = "Traduire la phrase"
    farsi: str = ""
    french: str = ""

    def __new__(cls, farsi: str, french: str):
        cls.farsi = farsi
        cls.french = french

        return genanki.Note(
            model = SimpleTranslateModel(),
            fields = [
                cls.rule,
                cls.farsi,
                cls.french
            ]
        )
