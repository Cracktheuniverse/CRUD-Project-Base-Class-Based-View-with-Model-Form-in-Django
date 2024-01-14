from typing import Any
from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from.models import User
from django.views.generic.base import TemplateView,RedirectView
# Create your views here.


class UserAddShowView(TemplateView):
    template_name='enroll/addandshow.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        fm= StudentRegistration()
        stud=User.objects.all()
        context={'stu':stud, 'form':fm }
        return context
    
    def post (self,request):
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            return HttpResponseRedirect('/')















# def add_show(request):
#     if request.method =='POST':
#        fm=StudentRegistration(request.POST)
#        if fm.is_valid():
#            nm=fm.cleaned_data['name']
#            em=fm.cleaned_data['email']
#            pw=fm.cleaned_data['password']
#            reg=User(name=nm,email=em,password=pw)
#            reg.save()
#            fm=StudentRegistration()
          
#     else:
#             fm=StudentRegistration()
#     stud=User.objects.all()
    
#     return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})








# def delete_data(request,id):
#     if request.method=="POST":
#         pi= User.objects.get(pk=id)
        
#         pi.delete()
        
#         return HttpResponseRedirect('/')


class UserDeleteView(RedirectView):
    url='/'
    def get_redirect_url(self, *args: Any, **kwargs: Any):
        # print(kwargs)
        del_id=kwargs['id']
        User.objects.get(pk=del_id).delete()
        
        return super().get_redirect_url(*args, **kwargs)










    
    
    
    
    
    
# This Function will Update/Edit Data
def update_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
   
    return render(request,'enroll/updatestudent.html' ,{'form':fm})