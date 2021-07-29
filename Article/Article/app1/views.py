
from django.shortcuts import render
from app1.models import Articlemodel
from app1.forms import Articleform
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.
def Crud(request):
    if request.method == 'POST':
        fm = Articleform(request.POST)
        if fm.is_valid():
            Article_name = fm.cleaned_data['Article_name']
            Article_date = fm.cleaned_data['Article_date']
            Article_writer = fm.cleaned_data['Article_writer']
            Article_reviews = fm.cleaned_data['Article_reviews']

            db = Articlemodel(Article_name=Article_name,Article_date=Article_date,Article_writer=Article_writer,Article_reviews=Article_reviews)
            db.save()
            fm = Articleform()
    else:
        fm = Articleform()
    data = Articlemodel.objects.all()
    return render(request,'index.html',{'form':fm,'fetch': data})

def update(request,id):
    if request.method == 'POST':
        pi = Articlemodel.objects.get(pk=id)
        fm = Articleform(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.info(request,'Data Updated Successfully')

    else:
        pi = Articlemodel.objects.get(pk=id)
        fm = Articleform(instance=pi)

    return render(request,'update.html',{'form':fm})

def delete(request,id):
    if request.method == 'POST':
        fm = Articlemodel.objects.get(pk=id)
        fm.delete()
        return HttpResponseRedirect('/')


