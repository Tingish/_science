# Create your views here.
# Create your views here.

from django.shortcuts import render
from _content.models import StructureNode, get_queryset_descendants, Paragraph, hashTagParser, tagSaveHelper, Image, Timelike
from _user.forms import ParagraphFormLabbook, ImageFormLabbook, TimelikeFormLabbook
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType


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

    
    text_form = ParagraphFormLabbook()
    image_form = ImageFormLabbook()
    timelike_form = TimelikeFormLabbook()
    print(request.POST)
    if (request.method == 'POST'): #if form has been submitted
        if (request.POST['formType'] == 'textForm'):
            text_form = textFormLabbookSave(request)
        elif (request.POST['formType'] == 'imageForm'):
            image_form = imageFormLabbookSave(request)
        elif (request.POST['formType'] == 'timelikeForm'):
            timelike_form = timelikeFormLabbookSave(request)
                
    labbook_list = StructureNode.objects.filter(isLabnote = True, author=request.user).exclude(content_type = None).order_by('-pubDate')            
    return render(request, '_user/labbook.html', {'labbook_list': labbook_list, 'textForm': text_form, 'imageForm': image_form, 'timelikeForm':timelike_form,}) #'form':CommentForm()})

def textFormLabbookSave(request):
        if (ParagraphFormLabbook(request.POST).is_valid()):
            tempParagraph = Paragraph()
            tempParagraph.text = request.POST['textFormText'] 
            tempParagraph.save()
            tempStructureNode = StructureNode()
            tempStructureNode.title = request.POST['textFormTitle']
            tempStructureNode.author = request.user
            tempStructureNode.content_type = ContentType.objects.get_for_model(Paragraph)
            tempStructureNode.object_id = tempParagraph.id
            tempStructureNode.isPublished = False
            if StructureNode.objects.order_by('-position').exists():
                tempStructureNode.position = StructureNode.objects.order_by('-position')[0].position+1
            else:
                tempStructureNode.position = 1
            tempStructureNode.isComment = False
            tempStructureNode.isLabnote = True
            tempStructureNode.save()
            tagList = hashTagParser(request.POST['textFormTag'])
            for tag in tagList:
                tempStructureNode.tag_set.add(tagSaveHelper(tag))
            tempStructureNode.save()    
            print("something is valid")
            return ParagraphFormLabbook()
        else:
            print("nothing is ever valid")
            return ParagraphFormLabbook(request.POST)
        
def imageFormLabbookSave(request):
        if (ImageFormLabbook(request.POST, request.FILES).is_valid()):
            tempImage = Image()
            if (request.POST.get('imageFormLinkSource',False)):
                tempImage.linkSource = request.POST['imageFormLinkSource']
            if (request.FILES.get('imageFormLocalSource', False)):
                tempImage.localSource = request.FILES['imageFormLocalSource']
            tempImage.save()
            tempStructureNode = StructureNode()
            tempStructureNode.title = request.POST['imageFormTitle']
            tempStructureNode.author = request.user
            tempStructureNode.content_type = ContentType.objects.get_for_model(Image)
            tempStructureNode.object_id = tempImage.id
            tempStructureNode.isPublished = False
            if StructureNode.objects.order_by('-position').exists():
                tempStructureNode.position = StructureNode.objects.order_by('-position')[0].position+1
            else:
                tempStructureNode.position = 1
            tempStructureNode.isComment = False
            tempStructureNode.isComment = False
            tempStructureNode.isLabnote = True
            tempStructureNode.save()
            tagList = hashTagParser(request.POST['imageFormTag'])
            for tag in tagList:
                tempStructureNode.tag_set.add(tagSaveHelper(tag))
            tempStructureNode.save()    
            print("something is valid")
            return ImageFormLabbook()
        else:
            print("nothing is ever valid")
            return ImageFormLabbook(request.POST)
        
def timelikeFormLabbookSave(request):
        if (TimelikeFormLabbook(request.POST, request.FILES).is_valid()):
            tempTimelike = Timelike()
            if (request.POST.get('timelikeFormLinkSource',False)):
                tempTimelike.linkSource = request.POST['timelikeFormLinkSource']
            if (request.FILES.get('timelikeFormLocalSource', False)):
                tempTimelike.localSource = request.FILES['timelikeFormLocalSource']
            tempTimelike.save()
            tempStructureNode = StructureNode()
            tempStructureNode.title = request.POST['timelikeFormTitle']
            tempStructureNode.author = request.user
            tempStructureNode.content_type = ContentType.objects.get_for_model(Timelike)
            tempStructureNode.object_id = tempTimelike.id
            tempStructureNode.isPublished = False
            if StructureNode.objects.order_by('-position').exists():
                tempStructureNode.position = StructureNode.objects.order_by('-position')[0].position+1
            else:
                tempStructureNode.position = 1
            tempStructureNode.isComment = False
            tempStructureNode.isComment = False
            tempStructureNode.isLabnote = True
            tempStructureNode.save()
            tagList = hashTagParser(request.POST['timelikeFormTag'])
            for tag in tagList:
                tempStructureNode.tag_set.add(tagSaveHelper(tag))
            tempStructureNode.save()    
            print("something is valid")
            return TimelikeFormLabbook()
        else:
            print("nothing is ever valid")
            return TimelikeFormLabbook(request.POST)
    