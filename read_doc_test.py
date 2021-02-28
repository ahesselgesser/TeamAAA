import docx
from docx.oxml.ns import qn
import re

## Change this file location to the location of the file you are parsing
doc = docx.Document("C:/Users/twins/Desktop/UNO classes/Spring 2021 Semester/CSCI 4970 - Capstone/Python tests/undergrad2018-regular.docx")

# 'C:\Users\twins\Desktop\UNO classes\Spring 2021 Semester\CSCI 4970 - Capstone\Python tests'
# https://github.com/ahesselgesser/TeamAAA

#### Variables to capture
## College, Department/School ?, Program, Degree Level, Academic Year of Report,
## Date Range of Reported Data, Person Preparing the Report, SLOs (maybe in an array, or tuple, or something)
## Bloom's Taxonomy (checkboxes)

regex_counter = 0

regex_tuple = ('College:\s*(.*)\s*Department/School:', )

all_paras = doc.paragraphs
for para in all_paras:
    regex = re.findall(regex_tuple[regex_counter], para.text)
    if (regex):
        print(regex[0])

    #print(para.text)


"""
### https://stackoverflow.com/questions/27861732/parsing-of-table-from-docx-file/27862205 ###
data = []

table = doc.tables[0]
for i, row in enumerate(table.rows):
    text = (cell.text for cell in row.cells)
    #print(row.cells)
    
    # Establish the mapping based on the first row
    # headers; these will become the keys of our dictionary
    if i == 0:
        keys = tuple(text)
        continue

    # Construct a dictionary for this row, mapping
    # keys to values for this row
    row_data = dict(zip(keys, text))
    data.append(row_data)

print(data)
###    https://stackoverflow.com/questions/27861732/parsing-of-table-from-docx-file/27862205 ###
"""