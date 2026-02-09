from django.shortcuts import render, get_object_or_404
from .models import Tutorial
import markdown2

def tutorial_list(request):
    tutorials = Tutorial.objects.all().order_by('id')
    return render(request, 'tutorial.html', {
        'tutorials': tutorials,
        'tutorial': None,
        'content_html': None
    })

def tutorial_detail(request, slug):
    tutorials = Tutorial.objects.all().order_by('id')
    tutorial = get_object_or_404(Tutorial, slug=slug)
    content_html = markdown2.markdown(tutorial.content_md, extras=["fenced-code-blocks", "tables"])
    
    return render(request, 'tutorial.html', {
        'tutorials': tutorials,
        'tutorial': tutorial,
        'content_html': content_html
    })
