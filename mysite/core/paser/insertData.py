from mysite.core.models import aac_models
from mysite.core.models import assessment_models
from mysite.core.models import basic_models
from mysite.core.models import data_models
from mysite.core.models import decisionsActions_models
from mysite.core.models import slo_models
import datetime
import psycopg2
import re


def insertCheckBox(list_of_lists):
    conn = psycopg2.connect(database="aaadb", user='teamaaa',
                            password='aaapass', host='localhost', port='5432')
    conn.autocommit = True
    cursor = conn.cursor()
    a = 0
    # cursor.execute('''INSERT INTO core_gradGoals(id, text, active)
    # VALUES (1, "i CAN DI", True)''')

    # conn.commit()
    # TODO: Grad Goal stuff
    GradGoal1 = slo_models.GradGoal.objects.create(
        text="SampleGradGoal", active=True)
    GradGoal1.save()
    print("Records inserted........")

    conn.close()
    return 1


def insertReportHeader(match_list, list_of_lists, accredited1, length_slo, dec_act, assessment_methods, slo_list, data_coll_list):
    # insert College Table
    college1 = aac_models.College.objects.create(
        name=match_list[0], active=True)
    college1.save
    # insert department table
    depart = aac_models.Department.objects.create(
        name=match_list[1], college=college1, active=True)
    depart.save()
    # insert Report table
    title = match_list[1] + " " + match_list[2] + \
        " " + match_list[3] + " " + match_list[4]
    report = basic_models.Report.objects.create(year=match_list[4], author=match_list[6],
                                                degreeProgram=match_list[
                                                    2], accredited=accredited1, date_range_of_reported_data=match_list[5],
                                                section1Comment=None, section2Comment=None, section3Comment=None, section4Comment=None, submitted=True,
                                                returned=False, numberOfSLOs=length_slo, uploader=match_list[1], title=title)
    report.save()
    # insert SLO table
    slos = []
    slonum = 1
    for x in range(length_slo):
        tempslo = slo_models.SLO.objects.create(
            blooms=list_of_lists[0][x + 1], numberOfUses=1)
        slos.append(tempslo)
        slonum = slonum + 1
    # insert SLO in Report Table
    sloIRs = []
    sloirnum = 1
    for slo in slos:
        sloIR = slo_models.SLOInReport.objects.create(
            goalText=slo_list[sloirnum - 1][7:], slo=slo, changedFromPrior=False, report=report, number=sloirnum, numberOfAssess=0)  # Number of asses unknown
        sloirnum = sloirnum + 1
        sloIRs.append(sloIR)
    # Assessment Methods

    assessmentVs = []
    today = datetime.datetime.now()
    date = today.strftime("%Y-%m-%d")
    assNum = 0
    statusCount = 1
    for assessmentMeth in assessment_methods:
        # Not a great solution may come back to this
        if (len(assessmentMeth[1]) > 24):
            # TODO Where currently includes extraneous information
            # TODO All True/False flags are placeholders
            # TODO: Most of Assessment Version is placeholders

            # Title
            title = assessmentMeth[1]

            # Description
            description = assessmentMeth[2]

            # Domain
            domainExamination = False
            domainProduct = False
            domainPerformance = False
            domainText = assessmentMeth[3][1]
            temp = re.findall("☒\s+\w+", domainText)
            for result in temp:
                temp = re.search("☒\s+(\w+)", result)
                result = temp.group(1)
                print(result)
                if (result == "Product"):
                    domainProduct = True
                if (result == "Examination"):
                    domainExamination = True
                if (result == "Performance"):
                    domainPerformance = True

            # Type
            directMeasure = False
            directText = assessmentMeth[4][1]
            temp = re.findall("☒\s+\w+", directText)
            for result in temp:
                temp = re.search("☒\s+(\w+)", result)
                result = temp.group(1)
                if (result == "Direct"):
                    directMeasure = True
                if (result == "Indirect"):
                    directMeasure = False

            # Point in Program
            finalTerm = False
            termText = assessmentMeth[5][1]
            temp = re.findall("☒\s+(?:\w+\s)+", termText)
            for result in temp:
                temp = re.search("☒\s+((?:\w+\s)+)", result)
                result = temp.group(1)
                if (result == "In final year of "):
                    finalTerm = True
                if (result == "In final term of program "):
                    finalTerm = True


            # Sample Description
            sampleDescription = "Placeholder sample description"

            # Population Measured
            allStudents = False
            studentText = assessmentMeth[6][1]
            temp = re.findall("☒\s+\w+", studentText)
            for result in temp:
                temp = re.search("☒\s+(\w+)", result)
                result = temp.group(1)
                if (result == "All"):
                    finalTerm = True
                if (result == "Sample"):
                    finalTerm = False
                    temp = re.search("\n(.*)", studentText)
                    sampleDescription = temp.group(1)


            # Frequency of Data Collection
            frequencyChoice = "Once"
            frequency = ""
            frequencyText = assessmentMeth[7][1]
            temp = re.findall("☒\s+\w+", frequencyText)
            for result in temp:
                temp = re.search("☒\s+(\w+)", result)
                result = temp.group(1)
                if (result == "Once/semester"):
                    frequencyChoice = "Once/Semester"
                if (result == "Once/year"):
                    frequencyChoice = "Once/Year"
                if (result == "Other"):
                    frequencyChoice = "Other"
                    temp = re.search("\n(.*)", frequencyText)
                    frequency = temp.group(1)

            # Proficiency Threshold
            threshold = "Placeholder threshold"
            thresholdText = assessmentMeth[8][1]
            temp = re.search("((?:\w+\s)+.*)\n", thresholdText)
            if (temp):
                threshold = temp.group(1)

            # Program Proficiency Target
            target = 0
            targetText = assessmentMeth[9][1]
            temp = re.search("([0123456789]+)%", targetText)
            if (temp):
                target = int(temp.group(1))

            # Where
            assessmentWhere = ""
            temp = re.search(":(.*)", assessmentMeth[5][1])
            if (temp):
                assessmentWhere = temp.group(1)

            assessment = assessment_models.Assessment.objects.create(
                title=title, domainExamination=domainExamination, domainProduct=domainProduct, domainPerformance=domainPerformance, directMeasure=directMeasure, numberOfUses=1)
            assessmentVersion = assessment_models.AssessmentVersion.objects.create(report=report, slo=sloIRs[assNum], number=1, changedFromPrior=False, assessment=assessment, date=date, description=description, finalTerm=finalTerm,
                                                                                   where=assessmentWhere, allStudents=allStudents, sampleDescription=sampleDescription, frequencyChoice=frequencyChoice, frequency=frequency, threshold=threshold, target=target)

            # SLO Status information
            statusDesc = "Unkown"
            if (len(list_of_lists[6]) > statusCount):
                statusDesc = list_of_lists[6][statusCount]
            sloStatus = data_models.SLOStatus(
                status=statusDesc, sloIR=sloIRs[assNum], override=False)
            statusCount = statusCount + 1

            assessmentVs.append(assessmentVersion)
        assNum = assNum + 1
    # Data Collection Methods
    additionalInfo = ""
    for item in list_of_lists[-1]:
        if (item[-1] == "1"):
            additionalInfo = item[:-2]
    if (additionalInfo):
        dataAdditional = data_models.ResultCommunicate.objects.create(
            text=additionalInfo, report=report)
    assVNum = 1
    for x in range(len(data_coll_list) - 1):
        # Which SLO Check
        sloNumber = 0
        if (len(data_coll_list[assVNum]) > 0 and data_coll_list[assVNum][0]):
            temp = re.search("([123456789])", data_coll_list[assVNum][0])
            if (temp):
                sloNumber = int(temp.group(1))

        
        if (sloNumber != 0):
            # Get the correct assessment
            for assessmentV in assessmentVs:
                if (assessmentV.slo.number == sloNumber):
                    assessmentVersion = assessmentV

            # Number of students Check
            numberOfStudents = 0
            if (len(data_coll_list[assVNum]) > 1 and data_coll_list[assVNum][2]):
                temp = re.findall("([0123456789]+)", data_coll_list[assVNum][2])
                for value in temp:
                    numberOfStudents = numberOfStudents + int(value)

            # Overall Proficency Chck
            overallProficient = 0
            if (len(data_coll_list[assVNum]) > 2 and data_coll_list[assVNum][3]):
                temp = re.search("(.*?)%", data_coll_list[assVNum][3])
                overallProficient = float(temp.group(1))

            assessmentData = data_models.AssessmentData.objects.create(
                assessmentVersion=assessmentVersion, dataRange=data_coll_list[assVNum][1], numberStudents=numberOfStudents, overallProficient=overallProficient)
            #assessmentAgg = data_models.AssessmentAggregate.objects.create(assessmentVersion=assessmentVersion, aggregate_proficiency=overallProficient, met=False)
            assVNum = assVNum + 1

    # insert decision Actions table
    for info in dec_act:
        # Which SLO Check
        sloNumber = 0
        if (info[0]):
            temp = re.search("([123456789])", info[0])
            sloNumber = int(temp.group(1))

        # Get the correct assessment
        for sloIR in sloIRs:
            if (sloIR.number == sloNumber):
                decisionAction = decisionsActions_models.DecisionsActions.objects.create(
                    sloIR=sloIR, text=info[1])

    print("Records inserted........")
