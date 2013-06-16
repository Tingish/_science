from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class node(MPTTModel):
    type = models.IntegerField()
    title = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')