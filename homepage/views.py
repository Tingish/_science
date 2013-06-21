# Create your views here.
from django.shortcuts import render
from _content.models import StructureNode, Timelike


def home(request):
    timelike_list = Timelike.objects.order_by('-id')
    
    return render(request, 'homepage/home.html', {'nodes':StructureNode.objects.all(), 'timelike_list':timelike_list})