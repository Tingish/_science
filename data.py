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

def DataTest(s, h, publish, words):
    numberOfExperiments = random.randint(s, h)
    print(numberOfExperiments)
    for x in range(1, numberOfExperiments+1):
        print(x)
        tempExp = StructureNode(title=words + "experiment" + str(x), slug="experiment" + str(x),  isPublished=publish, position=x)
        tempExp.save()
        numberOfArticles = random.randint(1, 5)
        for y in range(1, numberOfArticles+1):
            tempArt = StructureNode(title= words + "experiment" + str(x)+"Article" + str(y), slug="article" + str(y), parent_id=tempExp.id, isPublished=publish, position=y)
            tempArt.save()
            numberOfSubparts = random.randint(1,10)
            for z in range(1, numberOfSubparts+1):
                tempContent = StructureNode(title=words + "experiment" + str(x)+"Article" + str(y)+"Content" + str(z), slug="content" + str(z), parent_id=tempArt.id, content_type=GetObjectType(random.randint(1,3)), object_id = 1, isPublished=publish, position=z)
                tempContent.save()
DataTest(5,5, False, "test1")