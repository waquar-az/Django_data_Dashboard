from django.shortcuts import render
from .models import Blackcoffer
from django.db.models.functions import Extract
from dateutil import parser
from django.template import loader
from django.db.models import Q
from django.db.models import Sum,Avg,Min,Max,Count,F

def base(request):
    return render(request,'base.html')
def dashboard(request):
    dataa=Blackcoffer.objects.all()
    dist=Blackcoffer.objects.values('end_year').distinct()
    #print(dist)   
    Blackcoffer.objects.filter(region__icontains='world').update(region='World')
    region_intensity_sum=Blackcoffer.objects.values('region').annotate(intensity=Sum('intensity')).order_by('intensity')
   
    topic_likelihood_sum=Blackcoffer.objects.values('topic').annotate(likelihood=Sum('likelihood')).order_by('-likelihood')[0:10]
    
    contry_relavance_sum=Blackcoffer.objects.values('country').annotate(relevance=Sum('relevance')).order_by('-relevance')[0:10]
    endyear_intensity_sum=Blackcoffer.objects.values('end_year').annotate(intensity=Sum('intensity')).order_by('intensity')
    
    context={
        'dataa':dataa,
        'reginten':region_intensity_sum,
        'toplik':topic_likelihood_sum,
        'conrel':contry_relavance_sum,
        'endyearimp':endyear_intensity_sum
    }
    return render(request,'dashboard.html',context)