from django.shortcuts import render

from test_project.models import Province, Municipality, Zone

def index(request):
    """
    index.html page view logic
    """
    
    return render(request, 'test_project/index.html', {});


        