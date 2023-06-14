from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView
from .models import Material

class MaterialView(View): 
    def get(self, request): 
        mat = Material.objects.all()
        return render(request, 'main/index.html', {"index": mat})
    
    
class MaterialListView(ListView): 
    model = Material
    template_name = 'main/categories.html'
    context_object_name = "mat"
    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        queryset = Material.objects.filter(category_id=category_id)
        return queryset
