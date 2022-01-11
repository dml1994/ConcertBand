from django import forms
from .models import *

class LedgerForm(forms.ModelForm):

    class Meta:
        model = Ledger

        fields = [
            "name",
            "initialBalance"
        ]

class PeriodForm(forms.ModelForm):

    class Meta:
        model = Period

        fields = [
            "name",
            "ledger"
        ]

class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry

        fields = [
            "concept",
            "amount",
            "spending",
            "period"
        ]