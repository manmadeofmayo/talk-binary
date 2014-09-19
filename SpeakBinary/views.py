# Create your views here.
from models import Visit, theForm
from binary import *
from django.shortcuts import render_to_response

from django.template import RequestContext
def render_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)


def speakBinary(request):

    is_robot = False
    if request.method == "POST":
        form = theForm(request.POST)
        if form.is_valid():
            v = Visit.objects.create()
            v.save()
            
            text = form.cleaned_data["theOneField"] 
            if text.replace(" ", "").isdigit():
                is_robot = True
                output = from_bin(text)
            else: output = to_bin(text)
            
    else:
        form = theForm()
        output = ""
    count = Visit.objects.count()
    #return render_response(request, "the_template.html", {"form":form, "output": output, "count":count, "is_robot":is_robot})
    return render_response(request, "template.html", {"form":form, "output": output, "count":count, "is_robot":is_robot})    
            
        
        
    
    
    