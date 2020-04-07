from django.shortcuts import render

from django.http import HttpResponse

def index(request):
     
    context_dict = {'boldmessage': 'corona, is the news'}
    return render(request, 'news/index.html', context=context_dict)
    return HttpResponse("news index.") 