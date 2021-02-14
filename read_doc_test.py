import docx
from docx.oxml.ns import qn
doc = docx.Document("C:/Users/twins/Desktop/UNO classes/Spring 2021 Semester/CSCI 4970 - Capstone/Python tests/test.docx")

all_paras = doc.paragraphs
for para in all_paras:
    print(para.text)
    print("-------")