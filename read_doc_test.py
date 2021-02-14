import docx
from docx.oxml.ns import qn
doc = docx.Document("C:/Users/twins/Desktop/UNO classes/Spring 2021 Semester/CSCI 4970 - Capstone/Python tests/test.docx")

all_paras = doc.paragraphs
for para in all_paras:
    print(para.text)
    print("-------")

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