import zipfile
from lxml import etree
import re
from benedict import benedict 



xml_tree = etree.parse('C:/Users/twins/Desktop/UNO classes/Spring 2021 Semester/CSCI 4970 - Capstone/Python tests/chxTest/word/document.xml')

xml_string = etree.tostring(xml_tree).decode()

### Commenting out, because I'm not sure how to make use of the XML as a dict
#xml_dict = benedict(xml_string, format="xml")
#print(xml_dict.search('w:t', in_keys='true', exact='true'))

#reg = re.findall('([A-Za-z ]+)</w:t></w:r><w:sdt>(?:.*?)<w:t>&#9746;</w:t>', xml_string)
reg = re.findall('([A-Za-z ]+)</w:t></w:r><w:sdt>(?:.*?)<w:t>&#9746;</w:t>', xml_string)

### Commenting out so that I can focus on the results of the Regular Expression
#print(type(xml_string))
#print(xml_tree)
#print(xml_string)

# Try to research lookahead or lookbehind regex

if (reg):
    print("We found a checked box!")
    print(reg)
else:
    print("My regex didn't work. :(")

# 'C:\Users\twins\Desktop\UNO classes\Spring 2021 Semester\CSCI 4970 - Capstone\Python tests'
# The CheckBox is &#9744;
# The CheckedBox is &#9746;
# Unicode character code

### https://virantha.com/2013/08/16/reading-and-writing-microsoft-word-docx-files-with-python/ ###
def get_word_xml(docx_filename):
    with open(docx_filename) as f:
        zip = zipfile.ZipFile(f)
        xml_content = zip.read('word/document.xml')
    return xml_content
### https://virantha.com/2013/08/16/reading-and-writing-microsoft-word-docx-files-with-python/ ###

# def _check_element_is(self, element, type_char):
def _check_element_is(element, type_char):
    word_schema = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
    return element.tag == '{%s}%s' % (word_schema, type_char)

### https://github.com/python-openxml/python-docx/issues/224 ###
def isChecked(checkbox):
    val = False
    for child in checkbox:
        if _check_element_is(child, 'checked'):
            val = True
            return val
    return val

def checkboxValuesInElement(el):
    retVal = {}
    i = 0
    for child in el:
        if _check_element_is(child, 'checkBox'):
            retVal[i] = isChecked(child)
            i += 1
    return retVal
### https://github.com/python-openxml/python-docx/issues/224 ###