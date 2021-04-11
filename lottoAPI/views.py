from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .models import *
from .serializers import *

class ResultViewSet(viewsets.ModelViewSet):
    queryset = gov_thai.objects.all()
    serializer_class = gov_thaiSerializer
    
class VipResultViewSet(viewsets.ModelViewSet):
    queryset = lao_vip.objects.all()
    serializer_class = lao_vipSerializer
    
class LottoResultViewSet(viewsets.ModelViewSet):
    queryset = lao_lotto.objects.all()
    serializer_class = lao_lottoSerializer
    

def index(request):
    queryset = gov_thai.objects.all()
    serializer_class = gov_thaiSerializer(queryset, many=True)
    return render(request, 'index.html', {'data':serializer_class.data,})
