from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import place
from .models import freedom
def demo (request):
    obj=place.objects.all()
    ob=freedom.objects.all()
    return render(request,'index.html',{'result':obj, 'res':ob})

#def addit(request):
  #  x=int(request.GET['num1'])
   # y=int(request.GET['num2'])
    # z1=x+y
    # z2=x-y
    #z3=x/y
    # z4=x*y
   # return render(request,"ope.html",{'add':z1,'sub':z2,'div':z3,'mul':z4 })
    #name='Nirma'
   # return render(request,'detail.html',{'obj': name})