from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Donors
from django.views.generic import TemplateView, UpdateView
# Create your views here.

def index(request):
    return render(request,'index.html')


class AddDonorView(TemplateView):
    template_name = 'index.html'
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        blood_grp = request.POST['blood_grp']
        rh=request.POST['rh']
        if 'consent' in request.POST:
            consent = request.POST['consent']
        else:
            consent = False
        image = request.FILES['image']
        newDonor = Donors(
            name=name,
            age=age,
            address=address,
            blood_grp=blood_grp,
            consent=consent,
            rh=rh,
            image=image
            )
        newDonor.save()
        return render(request,self.template_name)
    

class ListDonorView(TemplateView):
    template_name = 'list.html'
    def get(self,request): 
        context = {
            'donors': Donors.objects.all()
        }
        return render(request, self.template_name,context=context)

class DeleteDonorView(TemplateView):
    def get(self,request,pk):
        to_delete = Donors.objects.get(pk=pk)
        to_delete.delete()
        return redirect('list-donor')


class UpdateDonorView(TemplateView):
    template_name = 'update.html'
    def get(self,request,pk):
        to_update = Donors.objects.get(pk=pk)
        context = {
            'donor': to_update
        }
        return render(request,self.template_name,context)
    def post(self,request,pk):
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        blood_grp = request.POST['blood_grp']
        rh=request.POST['rh']
        if 'consent' in request.POST:
            consent = request.POST['consent']
        else:
            consent = False
        to_update = Donors.objects.get(pk=pk)
        to_update.name = name
        to_update.age = age
        to_update.address = address
        to_update.blood_grp=blood_grp
        to_update.rh=rh
        if 'image' in request.FILES:
            to_update.image = request.FILES['image']
        else:
            pass
        if 'consent' in request.POST:
            to_update.consent = True
        else:
            to_update.consent = False
        to_update.save()
        return redirect('list-donor')