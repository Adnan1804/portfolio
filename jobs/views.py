from django.shortcuts import render,get_object_or_404
from .models import Jobs
from .models import Certificates
from .models import Publications

# Create your views here.
def homepage(request):
    publication = Publications.objects.all()
    certificate = Certificates.objects.all()
    job = Jobs.objects.all()
    return render(request,'jobs/home.html',{'job': job,'certificate': certificate,'publication': publication})


def detail(request,job_id):
    job_detail = get_object_or_404(Jobs,pk=job_id)
    return render(request,'jobs/detail.html',{'job' : job_detail})


def details(request,certificate_id):
    certificate_detail = get_object_or_404(Certificates,pk=certificate_id)
    return render(request,'jobs/details.html',{'certificate' : certificate_detail})


def pdetail(request,publication_id):
    publication_detail = get_object_or_404(Publications,pk=publication_id)
    return render(request,'jobs/p_details.html',{'publication' : publication_detail})
