from django import forms


class WatchNewStock(forms.Form):
    company_name = forms.CharField(help_text="Please enter stock symbol",
                                   max_length=8,
                                   strip=True,
                                   required=True,
                                   label='Ticker Symbol')