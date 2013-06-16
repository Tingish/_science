'''
Created on 2013-06-16

@author: Ian
'''
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from _content.models import StructureNode, Rating, ViewCount, Paragraph, Image, Timelike

admin.site.register(StructureNode, MPTTModelAdmin)
admin.site.register(Rating)
admin.site.register(ViewCount)
admin.site.register(Paragraph)
admin.site.register(Image)
admin.site.register(Timelike)
