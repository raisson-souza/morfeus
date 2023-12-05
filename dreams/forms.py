from django import forms

DREAM_TYPE = (
    ('Sonho', 'Sonho'),
    ('Pesadelo', 'Pesadelo')
)

FEELINGS = (
    ('Normal', 'Normal'),
    ('Feliz', 'Feliz'),
    ('Triste', 'Triste'),
    ('Raivoso', 'Raivoso'),
    ('Asssustado', 'Asssustado'),
    ('Indefinido', 'Indefinido'),
    ('Múltiplos', 'Múltiplos')
)

LUCID = (
    ('Não Lúcido', 'Não Lúcido'),
    ('Parcialmente Lúcido', 'Parcialmente Lúcido'),
    ('Lúcido', 'Lúcido')
)

PERIODS = (
    ('Indefinido', 'Indefinido'),
    ('Dia', 'Dia'),
    ('Noite', 'Noite'),
    ('Múltiplos', 'Múltiplos'),
)

class DreamRegister(forms.Form):
    title = forms.CharField(
        label="Título do Sonho",
        max_length=50
    )
    text = forms.CharField(
        widget=forms.Textarea,
        label="Descrição do Sonho"
    )
    dream_type = forms.ChoiceField(
        choices=DREAM_TYPE,
        label="Tipo de Sonho",
        
    )
    feeling = forms.ChoiceField(
        choices=FEELINGS,
        label="Sentimento"
    )
    lucid = forms.ChoiceField(
        choices=LUCID,
        label="Lucidez"
    )
    period = forms.ChoiceField(
        choices=PERIODS,
        label="Período do Sonho"
    )
    date = forms.DateField(
        label="Data do Sonho"
    )
    public = forms.BooleanField(
        label="Sonho Público",
        required=False
    )