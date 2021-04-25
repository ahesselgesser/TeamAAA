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
def insertReportHeader(match_list, list_of_lists, accredited1, length_slo, dec_act):
    #insert College Table
    college1 = aac_models.College.objects.create(name=match_list[0], active=True)
    college1.save
    #insert department table
    depart = aac_models.Department.objects.create(name=match_list[1],college=college1 ,active=True)
    depart.save()
    #insert Report table
    report = basic_models.Report.objects.create(year=match_list[4], author= match_list[6], 
        degreeProgram=match_list[2], accredited=accredited1, date_range_of_reported_data=match_list[5],
        section1Comment=None, section2Comment=None,section3Comment=None,section4Comment=None,submitted=True,
        returned=False,numberOfSLOs= length_slo, uploader= match_list[1])
    report.save()
    #insert SLO table
    slos = []
    slonum = 1
    for x in range(length_slo):
        tempslo = slo_models.SLO.objects.create(blooms=list_of_lists[0][x + 1], numberOfUses=1)
        slos.append(tempslo)
        #tempslo.save()
        slonum = slonum + 1
    #insert SLO in Report Table
    sloIRs = []
    sloirnum = 1
    for slo in slos: #TODO: Replace goal placeholder with goal text. Find how to find number of assess
        sloIR = slo_models.SLOInReport.objects.create(goalText="Placeholder Text", slo=slo, changedFromPrior=False, report=report, number=sloirnum, numberOfAssess=0) #Number of asses unknown
        sloirnum = sloirnum + 1
        sloIRs.append(sloIR)
        #sloIR.save()
    #Assessment Methods
    #TODO: All fields are currently placeholder because I do not know where the data is and due to a bug I can not run the parsing script
    assessmentVs = []
    today = datetime.datetime.now()
    date = today.strftime("%Y-%m-%d")
    #TODO: Add loop structure
    assessment = assessment_models.Assessment.objects.create(title="Placeholder Title", domainExamination=False, domainProduct=False, domainPerformance=False, directMeasure=False, numberOfUses=1)
    assessmentVersion = assessment_models.AssessmentVersion.objects.create(report=report, slo=sloIRs[0], number=0, changedFromPrior=False, assessment=assessment, date=date, description="Placeholder Description", finalTerm=False, where="Placeholder Location", allStudents=False, sampleDescription="Placholder sample description", frequencyChoice="O", frequency="Placeholder Frequency", threshold="Placeholder Threshold", target=0)
    assessmentVs.append(assessmentVersion)
    #Data Collection Methods
    #TODO: All fields are currently placeholder because I do not know where the data is and due to a bug I can not run the parsing script
    dataAdditional = data_models.DataAdditionalInformation.objects.create(report=report, comment="Placeholder Comment")
    dataAdditional = data_models.ResultCommunicate.objects.create(text="Placeholder Communication", report=report)
    for assessmentV in assessmentVs:
        assessmentData = data_models.AssessmentData.objects.create(assessmentVersion = assessmentV,dataRange="Placeholder Data Range", numberStudents=1, overallProficient=1)
        assessmentAgg = data_models.AssessmentAggregate.objects.create(assessmentVersion=assessmentV, aggregate_proficiency=1, met=False)
        #assessmentData.save()
        #assessmentAgg.save()
    for sloIR in sloIRs:
        sloStatus = data_models.SLOStatus(status="O", sloIR=sloIR, override=False)
        #sloStatus.save()


    #insert decision Actions table
    for info in dec_act:
        if info[0] == "SLO 1":
            print(info[1])
            decisionAction1 = decisionsActions_models.DecisionsActions.objects.create(sloIR = sloIRs[0], text=info[1])
        elif info[0] == "SLO 2":
            print(info[1])
            decisionAction1 = decisionsActions_models.DecisionsActions.objects.create(sloIR = sloIRs[1], text=info[1])
        elif info[0] == "SLO 3":
            print(info[1])
            decisionAction1 = decisionsActions_models.DecisionsActions.objects.create(sloIR = sloIRs[2], text=info[1])
        elif info[0] == "SLO 4":
            print(info[1])
            decisionAction1 = decisionsActions_models.DecisionsActions.objects.create(sloIR = sloIRs[3], text=info[1])
    #
    print("Records inserted........")

