from django import forms
from .models import Wallet
from django.forms import ModelForm
class WalletForm(forms.ModelForm):
    class Meta:
        model=Wallet
        fields=[
            'account_id',
            'master_seed',
            'master_seed_hex',
            'public_key',
            'public_key_hex'
        ]

