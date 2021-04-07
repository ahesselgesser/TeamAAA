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
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(content__icontains=query)

            reports = Report.objects.all()

            context={'results': reports,
                     'submitbutton': submitbutton}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')


class ReportListView(ListView):
    model = Report
    template_name = 'class_report_list.html'
    context_object_name = 'reports'


class UploadReportView(CreateView):
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy('class_report_list')
    template_name = 'upload_report.html'
