import docx
from docx.oxml.ns import qn
import re
import read_doc_chx

def regex_inc(regex_list, regex_counter, match_list):
    if(regex_counter < len(regex_list)):
        regex = re.findall(regex_list[regex_counter], para.text)
        if (regex):
            match_list.append(regex[0])
            #if (regex_counter < len(regex_list) - 1):
            regex_counter += 1
    return (regex_counter, match_list)


(chkbox_element_list, slo_count) = read_doc_chx.find_checkbox_elements()
print(slo_count)

## Change this file location to the location of the file you are parsing
doc = docx.Document("C:/Users/twins/Desktop/UNO classes/Spring 2021 Semester/CSCI 4970 - Capstone/Python tests/undergrad2018-regularv2.docx")

# 'C:\Users\twins\Desktop\UNO classes\Spring 2021 Semester\CSCI 4970 - Capstone\Python tests'
# https://github.com/ahesselgesser/TeamAAA

#### Variables to capture
## College, Department/School ?, Program, Degree Level, Academic Year of Report,
## Date Range of Reported Data, Person Preparing the Report, SLOs (maybe in an array, or tuple, or something)
## Bloom's Taxonomy (checkboxes)

### Creating lists to hold all the different regex's and matches, then iterate through them.
regex_counter = 0
ug18_regex_header_list = ['College:\s*(.*)\s*Department/School:', 'Department/School:\s*(.*)', 'Program:\s*(.*)\s*Degree Level:', 'Degree Level:\s*(.*)', 'Academic Year of Report:\s*(.*)\s*Date', 'Data:\s*(.*)',
'Person Preparing the Report:\s(.*)']   

### Match 1 is Colleges
### Match 2 is Department/School
### 
match_list = []

all_paras = doc.paragraphs

for para in all_paras:
    (regex_counter, match_list) = regex_inc(ug18_regex_header_list, regex_counter, match_list)
    (regex_counter, match_list) = regex_inc(ug18_regex_header_list, regex_counter, match_list)
    """
    if (regex_counter >= 7):
        print(para.text)
    """
print(match_list)

### https://stackoverflow.com/questions/27861732/parsing-of-table-from-docx-file/27862205 ###
data = []

### UG 2018 Regular Tables
## SLO Table
# Checkboxes
## SLO communication to stakeholders
## Assessment Methods
# Separate table for EACH SLO
# Will have to devise a method to determine when these tables end and the next category begins
# Checkboxes in these tables
## Data Collection And Analysis Table
# Two tables
# 
## Resuls communicated within program Table
## Decisions & Actions Table
### END

table = doc.tables[0]
for i, row in enumerate(table.rows):
    text = (cell.text for cell in row.cells)
    
    # Establish the mapping based on the first row
    # headers; these will become the keys of our dictionary
    if i == 0:
        keys = tuple(text)
        continue
    elif i == slo_count - 1:
        break

    # Construct a dictionary for this row, mapping
    # keys to values for this row
    row_data = dict(zip(keys, text))
    data.append(row_data)

print(data)
#print(data[0]['Student Learning Outcomes'])
###    https://stackoverflow.com/questions/27861732/parsing-of-table-from-docx-file/27862205 ###
