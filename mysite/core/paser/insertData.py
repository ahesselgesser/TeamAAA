from mysite.core.models import aac_models
from mysite.core.models import assessment_models
from mysite.core.models import basic_models
from mysite.core.models import data_models
from mysite.core.models import decisionsActions_models
from mysite.core.models import slo_models
import datetime
import psycopg2
def insertCheckBox(list_of_lists):
    conn = psycopg2.connect(database="aaadb", user='teamaaa', password='aaapass', host='localhost', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    a = 0
    #cursor.execute('''INSERT INTO core_gradGoals(id, text, active) 
    #VALUES (1, "i CAN DI", True)''')
    
    #conn.commit()
    #TODO: Grad Goal stuff
    GradGoal1 = slo_models.GradGoal.objects.create(text="SampleGradGoal",active=True)
    GradGoal1.save()
    print("Records inserted........")

    conn.close()
    return 1
def insertReportHeader(match_list, list_of_lists, accredited1, length_slo, dec_act, assessment_methods, slo_list, data_coll_list):
    #insert College Table
    college1 = aac_models.College.objects.create(name=match_list[0], active=True)
    college1.save
    #insert department table
    depart = aac_models.Department.objects.create(name=match_list[1],college=college1 ,active=True)
    depart.save()
    #insert Report table
    title = match_list[1] + " " + match_list[2] + " " +match_list[3] + " " +match_list[4]
    report = basic_models.Report.objects.create(year=match_list[4], author= match_list[6], 
        degreeProgram=match_list[2], accredited=accredited1, date_range_of_reported_data=match_list[5],
        section1Comment=None, section2Comment=None,section3Comment=None,section4Comment=None,submitted=True,
        returned=False,numberOfSLOs= length_slo, uploader= match_list[1], title=title)
    report.save()
    #insert SLO table
    slos = []
    slonum = 1
    for x in range(length_slo):
        tempslo = slo_models.SLO.objects.create(blooms=list_of_lists[0][x + 1], numberOfUses=1)
        slos.append(tempslo)
        slonum = slonum + 1
    #insert SLO in Report Table
    sloIRs = []
    sloirnum = 1
    for slo in slos: #TODO: Find how to find number of assess
        sloIR = slo_models.SLOInReport.objects.create(goalText=slo_list[sloirnum - 1], slo=slo, changedFromPrior=False, report=report, number=sloirnum, numberOfAssess=0) #Number of asses unknown
        sloirnum = sloirnum + 1
        sloIRs.append(sloIR)
    #Assessment Methods

    assessmentVs = []
    today = datetime.datetime.now()
    date = today.strftime("%Y-%m-%d")
    assNum = 0
    statusCount = 1
    for assessmentMeth in assessment_methods:
        if (assessmentMeth[2] != 'Title of the Measure'):
            #TODO Where currently includes extraneous information
            #TODO All True/False flags are placeholders
            #TODO: Most of Assessment Version is placeholders
            assessment = assessment_models.Assessment.objects.create(title=assessmentMeth[1], domainExamination=False, domainProduct=False, domainPerformance=False, directMeasure=False, numberOfUses=1)
            assessmentVersion = assessment_models.AssessmentVersion.objects.create(report=report, slo=sloIRs[assNum], number=0, changedFromPrior=False, assessment=assessment, date=date, description=assessmentMeth[2], finalTerm=False, where=assessmentMeth[5][1], allStudents=False, sampleDescription="Placholder sample description", frequencyChoice="O", frequency="Placeholder Frequency", threshold="Placeholder Threshold", target=0)

            #SLO Status information
            sloStatus = data_models.SLOStatus(status=list_of_lists[6][statusCount], sloIR=sloIRs[assNum], override=False)
            statusCount = statusCount + 1

            assessmentVs.append(assessmentVersion)
        assNum = assNum + 1
    #Data Collection Methods
    #TODO: I don't know where the information on how results are communicated to stakeholders are because the file I was using doesn't have text there
    dataAdditional = data_models.ResultCommunicate.objects.create(text="Placeholder Communication", report=report)
    assVNum = 1
    for assessmentV in assessmentVs:
        assessmentData = data_models.AssessmentData.objects.create(assessmentVersion = assessmentV,dataRange=data_coll_list[assVNum][1], numberStudents=int(data_coll_list[assVNum][2]), overallProficient=float(data_coll_list[assVNum][3]))
        assessmentAgg = data_models.AssessmentAggregate.objects.create(assessmentVersion=assessmentV, aggregate_proficiency=float(data_coll_list[assVNum][3]), met=False)
        assVNum = assVNum + 1

        

    #insert decision Actions table
    decActNum = 0
    for info in dec_act:
        if (decActNum < len(sloIRs)):
            decisionAction = decisionsActions_models.DecisionsActions.objects.create(sloIR = sloIRs[decActNum], text=info[1])
        decActNum = decActNum + 1
    #
    print("Records inserted........")

