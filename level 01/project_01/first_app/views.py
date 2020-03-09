from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    my_dict = {'insert_me': 'hi from views'}
    return render(request,'first_app/index.html',context=my_dict)
