# Create your views here.
from django.shortcuts import render
from _content.models import StructureNode, Timelike
from django.http import Http404

def index(request):
   
    tree_list = StructureNode.objects.filter(isPublished=True)
    return render(request, '_article/article.html', {'nodes':tree_list, })

def getArticle(request, article_url):
    
    print(article_url)
    #creating a tree with ancestors and descendents of a node.
    try:
        nodeItem = StructureNode.objects.get(url = article_url)
        descList = nodeItem.get_descendants(include_self=True)
        ancestorList = nodeItem.get_ancestors()
        #concatenating lists
        tree_list = ancestorList | descList
    except StructureNode.DoesNotExist:
        raise Http404
    
    return render(request, '_article/article.html', {'nodes':tree_list,})