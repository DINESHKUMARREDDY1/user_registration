from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *
from django.core.mail import send_mail



def register(request):
    UFO=Userform()
    PFO=Profileform()
    d={'UFO':UFO,'PFO':PFO}
    if request.method=='POST' and request.FILES :
        UFDO=Userform(request.POST)
        PFDO=Profileform(request.POST,request.FILES)
        if UFDO.is_valid and PFDO.is_valid :
            MUFDO=UFDO.save(commit=False)
            MUFDO.set_password(UFDO.cleaned_data['password'])
            MUFDO.save()

            MPFDO=PFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
        
        
        
            send_mail('regster',
                       'thank u, register done!!!!!!',
                       ' dineshreddypatta@gmail.com',
                       ['dineshreddy398937@gmail.com',],
                       fail_silently=False)
            return HttpResponse('Register Done Successfull !!!!')
        else:
            return HttpResponse('invalid data')


    return render(request,'register.html',d)