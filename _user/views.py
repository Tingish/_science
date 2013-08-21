# Create your views here.
# Create your views here.

from django.shortcuts import render
from _content.models import StructureNode, get_queryset_descendants, Paragraph, hashTagParser, tagSaveHelper, Image, Timelike, Dataset, datasetFormatter
from _user.forms import ParagraphFormLabbook, ImageFormLabbook, TimelikeFormLabbook, DataFormLabbook, PublishForm
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
    labbook_imageNode_list = StructureNode.objects.filter(isLabnote = True, author=request.user, content_type__model='image') #when filtering model must be lower case.
    labbook_timelikeNode_list = StructureNode.objects.filter(isLabnote = True, author=request.user, content_type__model='timelike')
    labbook_dataNode_list = StructureNode.objects.filter(isLabnote = True, author=request.user, content_type__model='dataset')
    publishForm = PublishForm()
    if (request.method == 'POST'):
        print(request.POST)
        publishForm = PublishForm(request.POST)
        if (publishForm.is_valid()):
            experimentNode = StructureNode()
            experimentNode.title = request.POST['publishFormTitle']
            experimentNode.author = request.user
            experimentNode.isPublished = True
            experimentNode.position = getPositionForRoots()
            experimentNode.save()
            tagList = hashTagParser(request.POST['publishFormTag'])
            for tag in tagList:
                experimentNode.tag_set.add(tagSaveHelper(tag))
            experimentNode.save()
            for sectionNodeIndex in range(0, int(request.POST['numberOfSections'])):
                sectionNode = StructureNode()
                sectionNode.title = request.POST['section_title_'+str(sectionNodeIndex)]
                sectionNode.parent = experimentNode
                sectionNode.author = request.user
                sectionNode.isPublished = True
                sectionNode.position = sectionNodeIndex + 1
                sectionNode.save()
                for tag in tagList:
                    sectionNode.tag_set.add(tagSaveHelper(tag))
                sectionNode.save()
                for contentNodeIndex in range(0, int(request.POST['numberOfContentSections_'+str(sectionNodeIndex)])):
                    contentNode = StructureNode()
                    contentNode.title = request.POST['section_title_'+str(sectionNodeIndex)] +"_content_"+str(contentNodeIndex)
                    contentNode.parent = sectionNode
                    contentNode.author = request.user
                    contentNode.isPublished = True
                    contentNode.position = contentNodeIndex +1
                    if (request.POST['contentType_section_content_'+str(sectionNodeIndex)+"_"+str(contentNodeIndex)] == "textContent"):
                        tempParagraph = Paragraph()
                        tempParagraph.text = request.POST['text_section_content_'+str(sectionNodeIndex)+"_"+str(contentNodeIndex)]
                        tempParagraph.save()
                        contentNode.content_type = ContentType.objects.get_for_model(Paragraph)
                        contentNode.object_id = tempParagraph.id                        
                        contentNode.save()
                    elif (request.POST['contentType_section_content_'+str(sectionNodeIndex)+"_"+str(contentNodeIndex)] == "imageContent"):
                        contentNode.content_type = ContentType.objects.get_for_model(Image)
                        if (request.POST.get('imageInputLinkSource_section_content_'+str(sectionNodeIndex)+"_"+str(contentNodeIndex))):
                            tempImage = Image()
                            tempImage.linkSource = request.POST['imageInputLinkSource_section_content_'+str(sectionNodeIndex)+"_"+str(contentNodeIndex)]
                            tempImage.save()
                            contentNode.object_id = tempImage.id
                            print("first")
                        elif (request.FILES.get('imageInputLocalSource_section_content_'+str(sectionNodeIndex)+"_"+str(contentNodeIndex))):
                            tempImage = Image()
                            tempImage.localSource = request.FILES['imageInputLocalSource_section_content_'+str(sectionNodeIndex)+"_"+str(contentNodeIndex)]
                            tempImage.save()
                            contentNode.object_id = tempImage.id
                            print("second")
                        elif (request.POST.get('imageInputLabbookSource_section_content_'+str(sectionNodeIndex)+"_"+str(contentNodeIndex))):
                            contentNode.object_id = int(request.POST['imageInputLabbookSource_section_content_'+str(sectionNodeIndex)+"_"+str(contentNodeIndex)])
                            print("third")
                        contentNode.save()
                    elif (request.POST['contentType_section_content_'+str(sectionNodeIndex)+"_"+str(contentNodeIndex)] == "timelikeContent"):
                        contentNode.content_type = ContentType.objects.get_for_model(Timelike)
                        if (request.POST.get('timelikeInputLinkSource_section_content_'+str(sectionNodeIndex)+"_"+str(contentNodeIndex))):
                            tempTimelike = Timelike()
                            tempTimelike.linkSource = request.POST['timelikeInputLinkSource_section_content_'+str(sectionNodeIndex)+"_"+str(contentNodeIndex)]
                            tempTimelike.save()
                            contentNode.object_id = tempTimelike.id
                            print("first")
                        elif (request.FILES.get('timelikeInputLocalSource_section_content_'+str(sectionNodeIndex)+"_"+str(contentNodeIndex))):
                            tempTimelike = Timelike()
                            tempTimelike.localSource = request.FILES['timelikeInputLocalSource_section_content_'+str(sectionNodeIndex)+"_"+str(contentNodeIndex)]
                            tempTimelike.save()
                            contentNode.object_id = tempTimelike.id
                            print("second")
                        elif (request.POST.get('timelikeInputLabbookSource_section_content_'+str(sectionNodeIndex)+"_"+str(contentNodeIndex))):
                            contentNode.object_id = int(request.POST['timelikeInputLabbookSource_section_content_'+str(sectionNodeIndex)+"_"+str(contentNodeIndex)])
                            print("third")
                        contentNode.save()
                    elif (request.POST['contentType_section_content_'+str(sectionNodeIndex)+"_"+str(contentNodeIndex)] == "dataContent"):
                        contentNode.content_type = ContentType.objects.get_for_model(Dataset)
                        if (request.POST.get('dataInputLabbookSource_section_content_'+str(sectionNodeIndex)+"_"+str(contentNodeIndex))):
                            contentNode.object_id = int(request.POST['dataInputLabbookSource_section_content_'+str(sectionNodeIndex)+"_"+str(contentNodeIndex)])
                        contentNode.save()
                    for tag in tagList:
                        contentNode.tag_set.add(tagSaveHelper(tag))
                    contentNode.save()
                        
    return render(request, '_user/publish.html', {'publishForm':publishForm, 'labbook_imageNode_list': labbook_imageNode_list, 'labbook_timelikeNode_list': labbook_timelikeNode_list, 'labbook_dataNode_list': labbook_dataNode_list, })

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
    print request.POST
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
            tempStructureNode.position = getPositionForRoots()
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
            tempStructureNode.position = getPositionForRoots()
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
            tempStructureNode.position = getPositionForRoots()
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
            tempStructureNode.position = getPositionForRoots()
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
        
def getPositionForRoots():
    if StructureNode.objects.filter(mptt_level=0).exists():
        return StructureNode.objects.filter(mptt_level=0).order_by('-position')[0].position+1
    else:
        return 1