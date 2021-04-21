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
def insertReportHeader(match_list):
    college1 = aac_models.College.objects.create(name=match_list[1], active=True)
    college1.save
    depart = aac_models.Department.objects.create(name=match_list[0],college=college1 ,active=True)
    depart.save()
    print("Header Records inserted........")
    return 1