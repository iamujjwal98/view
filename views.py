from django.shortcuts import render

from holidays.models import EX_hol, Bank_hol
from holidays.serializers import bankSerializer, exSerializer
from rest_framework import generics, permissions, serializers
#from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import *
   
class bankHeaderList(generics.ListCreateAPIView):
    serializer_class =bankSerializer
   
    def get_queryset(self):
        queryset = Bank_hol.objects.all()
        fromdate=self.request.query_params.get('fromdate')
        todate=self.request.query_params.get('todate')
        sc_group=self.request.query_params.get('sc_gp')
        h_type=self.request.query_params.get('h_type')
        return queryset.filter(h_date__range=[fromdate, todate],sc_gp=sc_group,h_type=h_type).order_by('h_date')
    
      
class exHeaderList(generics.ListCreateAPIView):
    serializer_class =exSerializer

    def get_queryset(self):
        queryset = EX_hol.objects.all()
        fromdate=self.request.query_params.get('fromdate')
        todate=self.request.query_params.get('todate')
        sc_group=self.request.query_params.get('sc_gp')
        h_type=self.request.query_params.get('h_type')
        return queryset.filter(h_date__range=[fromdate, todate],sc_gp=sc_group,h_type=h_type).order_by('h_date')
        
