# Create your views here.

from django.shortcuts import render
from _content.models import StructureNode

def index(request):

    comment_list = StructureNode.objects.get(isPublished = False)
    
    return render(request, '_commentGarden/commentgarden.html', {'comment_list': comment_list,}) #'form':CommentForm()})