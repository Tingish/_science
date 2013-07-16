# Create your views here.
from django.shortcuts import render
from _content.models import StructureNode, Timelike
from django.http import Http404


def home(request):
    top_article_list = StructureNode.objects.exclude(rating__isnull=True).order_by('-rating__rating')
    
    
    return render(request, '_home/home.html', {'top_article_list':top_article_list})

def getSubject(request, subject_url):
    try:
        top_article_list = StructureNode.objects.exclude(rating__isnull=True).order_by('-rating__rating').filter(tag__name__iexact=subject_url)
    except StructureNode.DoesNotExist:
        raise Http404
    
    return render(request, '_home/home.html', {'top_article_list':top_article_list})