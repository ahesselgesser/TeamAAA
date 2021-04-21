from mysite.core.models import aac_models
from mysite.core.models import assessment_models
from mysite.core.models import basic_models
from mysite.core.models import data_models
from mysite.core.models import decisionsActions_models
from mysite.core.models import slo_models
import psycopg2
def insertCheckBox(list_of_lists):
    conn = psycopg2.connect(database="aaadb", user='teamaaa', password='aaapass', host='localhost', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    a = 0
    #cursor.execute('''INSERT INTO core_gradGoals(id, text, active) 
    #VALUES (1, "i CAN DI", True)''')
    
    #conn.commit()
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
    report1 = basic_models.Report.objects.create(year=match_list[4], author= match_list[6], 
        degreeProgram=match_list[2], accredited=accredited1, date_range_of_reported_data=match_list[5],
        section1Comment=None, section2Comment=None,section3Comment=None,section4Comment=None,submitted=True,
        returned=False,numberOfSLOs= length_slo, uploader= match_list[1])
    report1.save()
    #insert SLO table
    slo1 = slo_models.SLO.objects.create(blooms=list_of_lists[0][1])
    slo2 = slo_models.SLO.objects.create(blooms=list_of_lists[0][1])
    slo3 = slo_models.SLO.objects.create(blooms=list_of_lists[0][1])
    #insert SLO in Report Table
    sloIR1 = slo_models.SLOInReport.objects.create(slo = slo1, report = report1, number = 1)
    sloIR2 = slo_models.SLOInReport.objects.create(slo = slo2, report = report1, number = 2)
    sloIR3 = slo_models.SLOInReport.objects.create(slo = slo3, report = report1, number = 3)
    #insert decision Actions table
    for info in dec_act:
        if info[0] == "SLO 1":
            decisionAction1 = decisionsActions_models.DecisionsActions.objects.create(sloIR = sloIR1, text=info[1])
        elif info[0] == "SLO 2":
            decisionAction1 = decisionsActions_models.DecisionsActions.objects.create(sloIR = sloIR2, text=info[1])
        elif info[0] == "SLO 3":
            decisionAction1 = decisionsActions_models.DecisionsActions.objects.create(sloIR = sloIR3, text=info[1])
    print("Records inserted........")

