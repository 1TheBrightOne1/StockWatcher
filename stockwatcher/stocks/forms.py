from django import forms
from django.core.exceptions import ValidationError
import urllib.request
import lxml.html
from .models import Stock


class WatchNewStock(forms.Form):
    company_name = forms.CharField(help_text="Please enter stock symbol",
                                   max_length=8,
                                   strip=True,
                                   required=True,
                                   label='Ticker Symbol')

    def clean_company_name(self):
        company = self.cleaned_data["company_name"]
        with urllib.request.urlopen(
                f'https://money.cnn.com/quote/quote.html?symb={company}') as req:
            if Stock.objects.filter(company=company).count() != 0:
                raise ValidationError('Stock already watched')
            if len(lxml.html.document_fromstring(req.read()).find_class('wsod_quoteData')) == 0:
                raise ValidationError('Invalid stock symbol')
        return company
