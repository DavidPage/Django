from django import forms

from trade.models import Match

class MatchForm(forms.ModelForm):
    competition = forms.ChoiceField
    homeTeam = forms.ChoiceField
    awayTeam = forms.CharField
    matchTime = forms.DateTimeField(
        widget=forms.DateTimeInput(),
        input_formats=('%d/%m/%Y', '%d/%m/%y', '%d-%m-%Y', '%d-%m-%y'),
        required=False,
    )

    class Meta:
        model = Match
