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
        print("SLO Communication" + self.sloCoumminication + "\n")
        print("Communication Result:" + self.resultCommunication + "\n")
    
    def importToDB(self):
        print("This has not yet been implimented\n")
