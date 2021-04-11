from rest_framework import serializers
from .models import *

class gov_thaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = gov_thai
        fields = '__all__'
        
class lao_vipSerializer(serializers.ModelSerializer):
    class Meta:
        model = lao_vip
        fields = '__all__'
        
class lao_lottoSerializer(serializers.ModelSerializer):
    class Meta:
        model = lao_lotto
        fields = '__all__'
        
class lao_starSerializer(serializers.ModelSerializer):
    class Meta:
        model = lao_star
        fields = '__all__'