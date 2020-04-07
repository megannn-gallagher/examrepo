from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("news index.")  
    context_dict = {'boldmessage': 'corona'}
    return render(request, 'news/index.html', context=context_dict)