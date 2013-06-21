# Create your views here.
from django.shortcuts import render
from _content.models import StructureNode, Timelike


def home(request):
    top_article_list = StructureNode.objects.exclude(rating__isnull=True).order_by('-rating__rating')
    
    
    return render(request, 'homepage/home.html', {'top_article_list':top_article_list})