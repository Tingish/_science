# Create your views here.
# Create your views here.

from django.shortcuts import render
from _content.models import StructureNode, get_queryset_descendants
from django.contrib.auth.decorators import login_required


@login_required
def userDashboard(request):
                        
    top_article_list = get_queryset_descendants(StructureNode.objects.exclude(rating__isnull=True).order_by('-rating__rating').filter(subscribedUser=request.user)).filter(content_type=None).filter(isPublished=True)
    
    
    return render(request, '_home/home2.html', {'top_article_list':top_article_list})

@login_required
def userComment(request):

    comment_list = StructureNode.objects.filter(isPublished = False)
    
    return render(request, '_commentGarden/commentgarden.html', {'comment_list': comment_list,}) #'form':CommentForm()})

@login_required
def userLabbook(request):

    labbook_list = StructureNode.objects.filter(isPublished = False, author=request.user).exclude(content_type = None).order_by('-pubDate')
    
    return render(request, '_user/labbook.html', {'labbook_list': labbook_list,}) #'form':CommentForm()})