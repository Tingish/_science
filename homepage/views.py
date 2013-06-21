# Create your views here.
from django.shortcuts import render
from _content.models import StructureNode

def home(request):
    return render(request, 'homepage/home.html', {'nodes':StructureNode.tree.all()})