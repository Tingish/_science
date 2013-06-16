from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.template.defaultfilters import slugify

# Create your models here.

class StructureNode(MPTTModel):
    title = models.CharField(max_length=200)
    pubDate = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, blank=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    #setting up content
    #If both content_type and id are null then it is a container node
    #Otherwise it is a content node.
    #setting up relationships for multiple model types
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    #need to create a smarter object id that would work across object types.
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()
    isPublished = models.BooleanField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    position = models.PositiveIntegerField()
    
    def __str__(self):
        return '%i %i %i %s' % (self.pubDate.year, self.pubDate.month, self.pubDate.day, self.title)
    
    def save(self):
        super(StructureNode, self).save()
        self.slug = '%i/%i/%i/%s' % (self.pubDate.year, self.pubDate.month, self.pubDate.day, slugify(self.title))
        super(StructureNode, self).save()
    
    class Meta:
        unique_together = ('parent', 'position')
        
    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by=['position']

class Rating(models.Model):
    structureNode = models.OneToOneField(StructureNode, primary_key=True)
    rating = models.PositiveIntegerField()
    
    def __str__(self):
        return self.structureNode.title
    
class ViewCount(models.Model):
    structureNode = models.OneToOneField(StructureNode, primary_key=True)
    viewCount = models.PositiveIntegerField()
    
    def __str__(self):
        return self.structureNode.title
    
class Paragraph(models.Model):
    structureNode = generic.GenericRelation(StructureNode)
    text = models.TextField()
    
    def __str__(self):
        if self.structureNode.order_by('pubDate').exists():
            return self.structureNode.order_by('pubDate')[0].title
        
        return "No Node"
    
class Image(models.Model):
    structureNode = generic.GenericRelation(StructureNode)
    linkSource = models.URLField(max_length=200, blank=True, null=True)
    localSource = models.FileField(upload_to='content/image', blank=True, null=True)
    
    def __str__(self):
        if self.structureNode.order_by('pubDate').exists():
            return self.structureNode.order_by('pubDate').title
        
        return "No Node"
    
    def clean(self):
        from django.core.exceptions import ValidationError
        #allow only one source for video/audio
        
        if not (not self.linkSource) ^ (not self.localSource):
            raise ValidationError('Please select exactly one source')
    
class Timelike(models.Model):
    structureNode = generic.GenericRelation(StructureNode)
    linkSource = models.URLField(max_length=200, blank=True, null=True)
    localSource = models.FileField(upload_to='content/image', blank=True, null=True)
    
    def __str__(self):
        if self.structureNode.order_by('pubDate').exists():
            return self.structureNode.order_by('pubDate').title
        
        return "No Node"
    
    def clean(self):
        from django.core.exceptions import ValidationError
        #allow only one source for video/audio
        
        if not (not self.linkSource) ^ (not self.localSource):
            raise ValidationError('Please select exactly one source')
    
    
    

    
    