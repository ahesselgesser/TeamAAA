from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.db.models import Q

from .forms import ReportForm
from .models.basic_models import Report
from .forms import FileFieldForm
from django.http import HttpResponse
import os
import datetime

class Home(TemplateView):
    template_name = 'home.html'



def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


def report_list(request):
    reports = Report.objects.all()
    return render(request, 'report_list.html', {
        'reports': reports
    })


def upload_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            dbform = Report.objects.create(year="1980", author="John Johnny", degreeProgram="Test2",accredited=False,date_range_of_reported_data="1908-1981",section1Comment="",section2Comment="",section3Comment="",section4Comment="",submitted=True,returned=True,numberOfSLOs=0,title="TestTitle2",uploader="placeholder",)
            dbform.save()
            form.save()
            return redirect('report_list')
    else:
        form = ReportForm()
    return render(request, 'upload_report.html', {
        'form': form
    })


def delete_report(request, pk):
    if request.method == 'POST':
        report = Report.objects.get(pk=pk)
        report.delete()
    return redirect('report_list')

def search(request):
    if request.method == 'GET':
        titleText= request.GET.get('titleText')
        degreeprogram = request.GET.get('degreeProgram')

        submitbutton= request.GET.get('submit')
        results = Report.objects.all()
        if (titleText != None):
            results = results.filter(title__contains=titleText)
        if ((degreeprogram != None) & (degreeprogram != "None")):
            results = results.filter(degreeProgram=degreeprogram)
        context={'results': results,
                    'submitbutton': submitbutton}

        return render(request, 'search.html', context)

    else:
        return render(request, 'search.html')

def view_report(request):
    if request.method == 'GET':
        reportId= request.GET.get('id')
        results = Report.objects.filter(id=reportId)
        context={'results': results}
        return render(request, 'report.hml', context)
    return render(request, 'report.hml')

class ReportListView(ListView):
    model = Report
    template_name = 'class_report_list.html'
    context_object_name = 'reports'


class UploadReportView(CreateView):
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy('class_report_list')
    template_name = 'upload_report.html'
