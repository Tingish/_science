# Create your views here.
# Create your views here.

from django.shortcuts import render
from _content.models import StructureNode, get_queryset_descendants, Paragraph, hashTagParser, tagSaveHelper, Image, Timelike, Dataset, datasetFormatter
from _user.forms import ParagraphFormLabbook, ImageFormLabbook, TimelikeFormLabbook, DataFormLabbook
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

@login_required
def userDashboard(request):
                        
    top_article_list = get_queryset_descendants(StructureNode.objects.exclude(rating__isnull=True).order_by('-rating__rating').filter(subscribedUser=request.user)).filter(content_type=None).filter(isPublished=True)
    
    
    return render(request, '_home/home2.html', {'top_article_list':top_article_list})

@login_required
def userComment(request):

    comment_list = StructureNode.objects.filter(isPublished = False)
    
    return render(request, '_commentGarden/commentgarden.html', {'comment_list': comment_list,}) #'form':CommentForm()})

@login_required
def userPublish(request):
    
    return render(request, '_user/publish.html', { })

@login_required
def userSearchForm(request):
    if (request.method == 'POST'):
        return HttpResponseRedirect(reverse('userLabbookTag', args=[request.POST['search']]))


@login_required
def userLabbookTextForm(request, subject_url=None):
    if (request.method == 'POST'):    
        image_form = ImageFormLabbook()
        timelike_form = TimelikeFormLabbook()
        data_form = DataFormLabbook()
        text_form = ParagraphFormLabbook(request.POST)
        if textFormLabbookSave(request):
            return HttpResponseRedirect('/user/labbook/')
        else:
            if (subject_url):            
                labbook_list = StructureNode.objects.filter(isLabnote = True, author=request.user).exclude(content_type = None).order_by('-pubDate').filter(tag__name__iexact=subject_url)
            else:
                labbook_list = StructureNode.objects.filter(isLabnote = True, author=request.user).exclude(content_type = None).order_by('-pubDate')                
            return render(request, '_user/labbook.html', {'labbook_list': labbook_list, 'textForm': text_form, 'imageForm': image_form, 'timelikeForm':timelike_form,'dataForm': data_form, 'subject_url':subject_url}) 
            
         
@login_required
def userLabbookImageForm(request, subject_url=None):
    if (request.method == 'POST'):
        text_form = ParagraphFormLabbook()
        image_form = ImageFormLabbook(request.POST)
        timelike_form = TimelikeFormLabbook()
        data_form = DataFormLabbook()
        if imageFormLabbookSave(request):
            return HttpResponseRedirect('/user/labbook/')
        else:
            if (subject_url):            
                labbook_list = StructureNode.objects.filter(isLabnote = True, author=request.user).exclude(content_type = None).order_by('-pubDate').filter(tag__name__iexact=subject_url)
            else:
                labbook_list = StructureNode.objects.filter(isLabnote = True, author=request.user).exclude(content_type = None).order_by('-pubDate')                
            return render(request, '_user/labbook.html', {'labbook_list': labbook_list, 'textForm': text_form, 'imageForm': image_form, 'timelikeForm':timelike_form,'dataForm': data_form, 'subject_url':subject_url}) 
         
@login_required
def userLabbookTimelikeForm(request, subject_url=None):
    if (request.method == 'POST'):
        text_form = ParagraphFormLabbook()
        image_form = ImageFormLabbook()
        timelike_form = TimelikeFormLabbook(request.POST)
        data_form = DataFormLabbook(request)
        if timelikeFormLabbookSave(request):
            return HttpResponseRedirect('/user/labbook/')
        else:
            if (subject_url):            
                labbook_list = StructureNode.objects.filter(isLabnote = True, author=request.user).exclude(content_type = None).order_by('-pubDate').filter(tag__name__iexact=subject_url)
            else:
                labbook_list = StructureNode.objects.filter(isLabnote = True, author=request.user).exclude(content_type = None).order_by('-pubDate')                
            return render(request, '_user/labbook.html', {'labbook_list': labbook_list, 'textForm': text_form, 'imageForm': image_form, 'timelikeForm':timelike_form,'dataForm': data_form, 'subject_url':subject_url}) 
         
@login_required
def userLabbookDataForm(request, subject_url=None):
    if (request.method == 'POST'):
        text_form = ParagraphFormLabbook()
        image_form = ImageFormLabbook()
        timelike_form = TimelikeFormLabbook()
        data_form = DataFormLabbook(request.POST)
        if textFormLabbookSave(request):
            return HttpResponseRedirect('/user/labbook/')
        else:
            if (subject_url):            
                labbook_list = StructureNode.objects.filter(isLabnote = True, author=request.user).exclude(content_type = None).order_by('-pubDate').filter(tag__name__iexact=subject_url)
            else:
                labbook_list = StructureNode.objects.filter(isLabnote = True, author=request.user).exclude(content_type = None).order_by('-pubDate')                
            return render(request, '_user/labbook.html', {'labbook_list': labbook_list, 'textForm': text_form, 'imageForm': image_form, 'timelikeForm':timelike_form,'dataForm': data_form, 'subject_url':subject_url})      

@login_required
def userLabbook(request, subject_url=None):

    text_form = ParagraphFormLabbook()
    image_form = ImageFormLabbook()
    timelike_form = TimelikeFormLabbook()
    data_form = DataFormLabbook()
    print(request.POST)
  
    if (subject_url):            
        labbook_list = StructureNode.objects.filter(isLabnote = True, author=request.user).exclude(content_type = None).order_by('-pubDate').filter(tag__name__iexact=subject_url)
    else:
        labbook_list = StructureNode.objects.filter(isLabnote = True, author=request.user).exclude(content_type = None).order_by('-pubDate')                
    return render(request, '_user/labbook.html', {'labbook_list': labbook_list, 'textForm': text_form, 'imageForm': image_form, 'timelikeForm':timelike_form,'dataForm': data_form, 'subject_url':subject_url}) #'form':CommentForm()})

def userLabbookNameTag(request, user_url, subject_url=None):
    userName = user_url
    if (subject_url):            
        labbook_list = StructureNode.objects.filter(isLabnote = True, author__username=request.user__username).exclude(content_type = None).order_by('-pubDate').filter(tag__name__iexact=subject_url)
    else:
        labbook_list = StructureNode.objects.filter(isLabnote = True, author__username=request.user__username).exclude(content_type = None).order_by('-pubDate')
    return render(request, '_user/labbookUser.html', {'labbook_list': labbook_list, 'userName':userName, 'subject_url':subject_url})      

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
            return True
        else:
            print("nothing is ever valid")
            return False
        
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
            return True
        else:
            print("nothing is ever valid")
            return False
        
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
            return True
        else:
            print("nothing is ever valid")
            return False
        
def dataFormLabbookSave(request):
        if (DataFormLabbook(request.POST).is_valid()):
            tempDataset = Dataset()
            tempDataset.data = datasetFormatter(request.POST) 
            tempDataset.save()
            tempStructureNode = StructureNode()
            tempStructureNode.title = request.POST['dataFormTitle']
            tempStructureNode.author = request.user
            tempStructureNode.content_type = ContentType.objects.get_for_model(Dataset)
            tempStructureNode.object_id = tempDataset.id
            tempStructureNode.isPublished = False
            if StructureNode.objects.order_by('-position').exists():
                tempStructureNode.position = StructureNode.objects.order_by('-position')[0].position+1
            else:
                tempStructureNode.position = 1
            tempStructureNode.isComment = False
            tempStructureNode.isLabnote = True
            tempStructureNode.save()
            tagList = hashTagParser(request.POST['dataFormTag'])
            for tag in tagList:
                tempStructureNode.tag_set.add(tagSaveHelper(tag))
            tempStructureNode.save()    
            print("something is valid")
            return True
        else:
            print("nothing is ever valid data")
            return False