'''
Created on 2013-06-17

@author: Ian
'''
from _content.models import StructureNode, Rating, ViewCount, Paragraph, Image, Timelike
import random
from django.contrib.contenttypes.models import ContentType


def GetObjectType(typeID):
    if(typeID==1):
        return ContentType.objects.get_for_model(Timelike)
    elif(typeID==2):
        return ContentType.objects.get_for_model(Image)
    elif(typeID==3):
        return ContentType.objects.get_for_model(Paragraph)

def DataTest(h, publish, words):
    numberOfExperiments = random.randint(1, h)
    print(numberOfExperiments)
    for x in range(1, numberOfExperiments+1):
        print(x)
        tempExp = StructureNode(title=words + "experiment" + str(x), slug=words + "experiment" + str(x),  isPublished=publish, position=x)
        tempExp.save()
        numberOfArticles = random.randint(1, 5)
        for y in range(1, numberOfArticles+1):
            tempArt = StructureNode(title= words + "experiment" + str(x)+"Article" + str(y), parent_id=tempExp.id, isPublished=publish, position=y)
            tempArt.save()
            tempArt.rating.rating = random.randint(1,50)
            tempArt.rating.save()
            numberOfSubparts = random.randint(1,10)
            for z in range(1, numberOfSubparts+1):
                tempContent = StructureNode(title=words + "experiment" + str(x)+"Article" + str(y)+"Content" + str(z), parent_id=tempArt.id, content_type=GetObjectType(random.randint(1,3)), object_id = 1, isPublished=publish, position=z)
                tempContent.save()


def DataTestWithComments(h, words):
    numberOfExperiments = random.randint(1, h)
    print(numberOfExperiments)
    for x in range(1, numberOfExperiments+1):
        print("x=" + str(x))
        tempExp = StructureNode(title=words + "experiment" + str(x), slug=words + "experiment" + str(x),  isPublished=True, position=x)
        tempExp.save()
        numberOfArticles = random.randint(1, 5)
        for y in range(1, numberOfArticles+1):
            print("y=" + str(y))
            tempArt = StructureNode(title= words + "experiment" + str(x)+"Article" + str(y), parent_id=tempExp.id, isPublished=True, position=y)
            tempArt.save()
            tempArt.rating.rating = random.randint(1,50)
            tempArt.rating.save()
            numberOfSubparts = random.randint(1,10)
            for z in range(1, numberOfSubparts+1):
                print("z=" + str(z))
                tempContent = StructureNode(title=words + "experiment" + str(x)+"Article" + str(y)+"Content" + str(z), parent_id=tempArt.id, content_type=GetObjectType(random.randint(1,3)), object_id = 1, isPublished=True, position=z)
                tempContent.save()
                numberofCommentThreads = random.randint(1,5)
                for xx in range(1, numberofCommentThreads+1):
                    print("xx=" + str(xx))
                    tempCommentThread = StructureNode(title=words + "experiment" + str(x) + "Article" + str(y) + "Content" + str(z) + "CommentThread" + str(xx), parent_id=tempContent.id, content_type=GetObjectType(3), object_id = 1, isPublished=False, position=xx)
                    tempCommentThread.save()
                    numberofComments = random.randint(1,5)
                    for yy in range(1, numberofComments+1):
                        print("yy=" + str(yy))
                        tempComment = StructureNode(title=words + "experiment" + str(x) + "Article" + str(y) + "Content" + str(z) + "CommentThread" + str(xx) + "Comment" + str(yy), parent_id=tempCommentThread.id, content_type=GetObjectType(3), object_id = 1, isPublished=False, position=yy)
                        tempComment.save()


#DataTest(10, True, "test10")
DataTestWithComments(5, "commenttest1")
