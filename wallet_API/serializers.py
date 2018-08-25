from rest_framework import serializers
from .models import Wallet

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model= Wallet
        fields=(
            'account_id',
            'master_seed',
            'master_seed_hex',
            'public_key',
            'public_key_hex',
        )
    
