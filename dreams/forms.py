from django import forms

DREAM_TYPES = (
    ('SONHO', 'Sonho'),
    ('PESADELO', 'Pesadelo'),
)

class DreamRegister(forms.Form):
    title = forms.CharField(label="Título do Sonho")
    text = forms.CharField(widget=forms.Textarea, label="Descrição do Sonho")
    dream_type = forms.ChoiceField(choices=DREAM_TYPES, label="Tipo de Sonho")
    date = forms.DateField(label="Data do Sonho")