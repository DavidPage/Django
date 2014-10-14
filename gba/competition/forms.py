from django import forms

from trade.models import Trade

class TradeForm(forms.ModelForm):
    match = forms.ChoiceField
    market = forms.ChoiceField
    invested = forms.CharField
    profitLoss = forms.CharField

    class Meta:
        model = Trade
