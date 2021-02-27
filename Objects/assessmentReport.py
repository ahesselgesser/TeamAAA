from slo import SLO
class AssesssmentReport:
    def __init__(self):
        self.year = ""
        self.college = ""
        self.department = ""
        self.program = ""
        self.degreeLevel = ""
        self.academicYear = ""
        self.dateRangeOfData = ""
        self.personPreparingReport = ""
        self.SLOs = []
        self.sloCoumminication = ""
        self.resultCommunication = ""
    
    def toString(self):
        print("Year: " + self.year + "\n")
        print("College: " + self.college + "\n")
        print("Department: " + self.department + "\n")
        print("Program: " + self.program + "\n")
        print("Degree Level: " + self.degreeLevel + "\n")
        print("Academic Year: " + self.academicYear + "\n")
        print("Date Range of Data: " + self.personPreparingReport + "\n")
        print("Person Preparing Report: " + self.year + "\n")
        #SLO Stuff
        #First Each SLO and it's Bloom Taxonomy
        x = 0
        for slo in self.SLOs:
            x += 1
            print("SLO: " + x + " " + slo.taxonomy + " \n")
        print("SLO Communication" + self.sloCoumminication + "\n")
        #Then Each SLO Assessment Method
        x = 0
        for slo in self.SLOs:
            x += 1
            print("SLO: " + x + "\n")
            print("Title of the Measure: " + slo.measureTitle + "\n")
            print("Describe How the Measure Aligns to the SLO: " + slo.measureDescription + "\n")
            print("Domain: " + slo.domain + "\n")
            print("Type: " + slo.type + "\n")
            print("Point in Program Assessment is Administered: " + slo.pointProgramAdministered + "\n")
            print("Point in Program Assessment is Administered: " + slo.descriptionPointProgramAdministered + "\n")
            print("Population Measured: " + slo.populationMeasured + "\n")
            print("Population Measured: " + slo.descriptionPopulationMeasured + "\n")
            print("Frequency of Data Collection: " + slo.frequencyDataCollected + "\n")
            print("Frequency of Data Collection: " + slo.descriptionFrequencyDataCollected + "\n")
            print("Proficiency Threshold: " + slo.proficiencyThreshold + "\n")
            print("Program Proficiency Target: " + slo.proficiencyTarget + "\n")
        #Then Data Analysis of each SLO
        x = 0
        for slo in self.SLOs:
            x += 1
            print("SLO: " + x + " " + slo.taxonomy + " \n")
        #SLO Status Table
        x = 0
        for slo in self.SLOs:
            x += 1
            print("SLO: " + x + " " + slo.taxonomy + " \n")
        print("Communication Result:" + self.resultCommunication + "\n")
        #Decisions and Actions of Each
        x = 0
        for slo in self.SLOs:
            x += 1
            print("SLO: " + x + " " + slo.taxonomy + " \n")


    def importToDB(self):
        print("This has not yet been implimented\n")
