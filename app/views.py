from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .form import PackageForm
from .models import *
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
@login_required
def index(request):
    packages=Packages.objects.all()
    context={"packages":packages}
    return render(request,'graduationProject/packages.html',context=context)
@login_required
def addPackage(request):
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse('<p>Info is not Valid</p>')


    else:
        form = PackageForm
        context = {
                'form': form,
        }

        return render(request, 'graduationProject/addpackage.html', context)

def deletePackage(request,id):
    package=Packages.objects.get(id=id)
    package.delete()
    return redirect('index')

@login_required
def search(request):
    q=request.GET['q']
    data=Packages.objects.filter(name__icontains=q).order_by('-id')
    context={"packages":data}
    return render(request,'graduationProject/packages.html',context=context)