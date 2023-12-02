from django import forms

DREAM_TYPES = (
    ('SONHO', 'Sonho'),
    ('PESADELO', 'Pesadelo'),
)

class DreamRegister(forms.Form):
    title = forms.CharField(help_text="teste")
    text = forms.CharField(widget=forms.Textarea)
    dream_type = forms.ChoiceField(choices=DREAM_TYPES)
    date = forms.DateField()