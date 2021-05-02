from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.db.models import Q

from .forms import ReportForm
from .forms import UploadFileForm
from .choices import BLOOMS_CHOICES
from .models.basic_models import Report
from .models.slo_models import SLOInReport
from .models.slo_models import GradGoal
from .models.slo_models import SLO
from .models.assessment_models import Assessment
from .models.assessment_models import AssessmentVersion
from .models.decisionsActions_models import DecisionsActions
from .models.data_models import AssessmentData
from .models.data_models import ResultCommunicate
from .forms import FileFieldForm
from django.http import HttpResponse
import os
import datetime

from mysite.core.paser import main_parser
#from pip._internal.cli import main_parser


class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        # TODO:Add check so it doesn't error if someone doesn't upload a document
        if (request.FILES.get('document') is None):
            return render(request, 'upload.html')
        else:
            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = fs.url(name)
            main_parser.run(uploaded_file.name)
            return render(request, 'upload.html', context)
    
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
            dbform = Report.objects.create(year="2019", author="Arts and Sciences", degreeProgram="Mathematcis", accredited=False, date_range_of_reported_data="F2018", section1Comment="",
                                           section2Comment="", section3Comment="", section4Comment="", submitted=True, returned=True, numberOfSLOs=0, title="Undergrad2018-regular", uploader="Alex",)
            GradGoal1 = GradGoal.objects.create(
                text="SampleGradGoal", active=True)
            GradGoal1.save()
            SLO1 = SLO.objects.create(blooms=dict(
                BLOOMS_CHOICES).get('CO'), numberOfUses=1)
            SLOReport1 = SLOInReport.objects.create(date="1980-01-01", goalText="Students will be  be able to make and write correct,clear and concise arguments",
                                                    slo=SLO1, changedFromPrior=False, report=dbform, number=1, numberOfAssess=1)
            SLO1.save()
            SLOReport1.save()
            SLO2 = SLO.objects.create(blooms=BLOOMS_CHOICES[3], numberOfUses=1)
            SLOReport2 = SLOInReport.objects.create(date="1980-01-01", goalText="Be able to communicate mathematics effectively in oral form.",
                                                    slo=SLO2, changedFromPrior=False, report=dbform, number=1, numberOfAssess=1)
            SLO2.save()
            SLOReport2.save()
            SLO3 = SLO.objects.create(blooms=BLOOMS_CHOICES[2], numberOfUses=1)
            SLOReport3 = SLOInReport.objects.create(date="1980-01-01", goalText="Demonstrate substantive  comprehension of the major ideas in the core areas of their fields of study.",
                                                    slo=SLO3, changedFromPrior=False, report=dbform, number=1, numberOfAssess=1)
            SLO3.save()
            SLOReport3.save()

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
        titleText = request.GET.get('titleText')
        authorText = request.GET.get('authorText')
        degreeProgram = request.GET.get('degreeProgram')

        results = Report.objects.all()
        results.filter()
        if (titleText):
            results = results.filter(title__contains=titleText)

        if (authorText):
            results = results.filter(author__contains=authorText)

        if (degreeProgram and (degreeProgram != "None")):
            results = results.filter(degreeProgram=degreeProgram)

        context = {'results': results}

        return render(request, 'search.html', context)

    else:
        results = Report.objects.all()
        context = {'results': results}
        return render(request, 'search.html')


def view_report(request):
    if request.method == 'GET':
        dummy = 0
        reportId = request.GET.get('id')
        results = Report.objects.filter(id=reportId)
        slos = SLOInReport.objects.filter(report=reportId)
        sloIRs = []
        for slo in slos:
            temp = SLO.objects.filter(id=slo.slo.id)
            if (len(temp) != 0):
                sloIRs.append((list(temp)[0].blooms, slo))
        assessmentMethods = []
        for slo in slos:
            temp = AssessmentVersion.objects.filter(slo__id=slo.id)
            if (len(temp) != 0):
                assessmentMethods.append((slo.number, list(temp)[0], temp[0].assessment))
        assessmentDatas = []
        for slo in slos:
            temp = AssessmentData.objects.filter(
                assessmentVersion__slo__id=slo.id)
            if (len(temp) != 0):
                assessmentDatas.append((slo.number, list(temp)[0]))
        decisionActions = []
        for slo in slos:
            temp = DecisionsActions.objects.filter(sloIR=slo.id)
            if (len(temp) != 0):
                decisionActions.append((slo.number, list(temp)[0]))
        resultCommunicate = []
        if (len(ResultCommunicate.objects.filter(report=reportId)) != 0):
            resultCommunicate = ResultCommunicate.objects.filter(report=reportId)[0]
        context = {'results': results, 'slos': sloIRs,
                   'assessmentDatas': assessmentDatas, 'decisionActions': decisionActions, 'assessmentMethods':assessmentMethods, 'resultCommunicate':resultCommunicate}
        return render(request, 'report.html', context)
    return render(request, 'report.html')


class ReportListView(ListView):
    model = Report
    template_name = 'class_report_list.html'
    context_object_name = 'reports'


class UploadReportView(CreateView):
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy('class_report_list')
    template_name = 'upload_report.html'
