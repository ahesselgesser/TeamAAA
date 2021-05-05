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

"""
This the logic for the home page. 
It returns the home page html which has nothing useful on it.
"""
class Home(TemplateView):
    template_name = 'home.html'

"""
This the logic for the page where you can upload a file. 
If it is visited with a document uploaded (when the user presses upload) then runs the parser on the uploaded file and returns the upload page back to the visitor.
"""
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

"""
This the logic for the ould page where you could upload a file. 
However, this button has been removed and now the only function of the page is to delete reports from the database.
"""
def upload_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
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

"""
This the logic for the search page 
It creates a query set based on the input parameters from the URL and returns a page which will have a table of every report that meets the input parameters
"""
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
            results = results.filter(degreeProgram__contains=degreeProgram)

        context = {'results': results}

        return render(request, 'search.html', context)

    else:
        results = Report.objects.all()
        context = {'results': results}
        return render(request, 'search.html')

"""
This the logic for the page where you can view a report. 
It pulls all of the relevant information about a report from the report id and outputs that to the report.html page which displays it.
results should be just the report object corresponding to the id from the parameters
sloIRs should be the list of tuples of the bloom's taxonomy level of each SLO associated with the given report and the corresponding sloIR object associated with that slo
assessmentDatas should be a list of tuplesof the number of the slo associated with the given DescisionAction object, followed by a given assessmentVersion object that is associated with the slo
decisionActions should be be a list of tuples of the number of the slo associated with the given DescisionAction object, followed by a given descisionAction object which is associated with the slo
assessmentMethods should be a list of tuples of the number of the slo associated with the given assessment, a given assessmentVersion object which is associated with the previous slo 
    (which is associated with the report), and finally the assessment object that corresponds to this assessmentVersion object
resultCommunicate should be the result communicate object associated with the given report
"""
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
