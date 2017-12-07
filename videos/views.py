from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
import random
def home(request) :
    return HttpResponse('<h1>Home</h1>')

class HomeView(View):
    def get(self, request,*args, **kwargs):
        number =str(random.randint(100,1000))
       #  text = "<h1>welcome</h1>"
       #  text += '<h3>randome</h3>['+number+']'
       # return HttpResponse('text')
        context ={
            "name" : "John",
            "number" : number,
            "present" : "<ul><li>내용</li><li>내용2</li></ul>"
        }
        return  render(request,"home.html", context )

