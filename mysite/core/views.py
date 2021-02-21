from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import ReportForm
from .models import Report


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


class ReportListView(ListView):
    model = Report
    template_name = 'class_report_list.html'
    context_object_name = 'reports'


class UploadReportView(CreateView):
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy('class_report_list')
    template_name = 'upload_report.html'
