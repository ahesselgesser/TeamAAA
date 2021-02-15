import zipfile
from lxml import etree
import re

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

xml_tree = etree.parse('C:/Users/twins/Desktop/UNO classes/Spring 2021 Semester/CSCI 4970 - Capstone/Python tests/chxTest/word/document.xml')

xml_string = etree.tostring(xml_tree).decode()

#reg = re.search('a', 'apple')
#print(type(xml_string))
#print(xml_tree)
#print(xml_string)

#if (reg):
    #print("We found a checked box!")
    #print(reg.group(0))
#else:
    #print("Our regex didn't work. :(")

# 'C:\Users\twins\Desktop\UNO classes\Spring 2021 Semester\CSCI 4970 - Capstone\Python tests'
# The CheckBox is &#9744;
# The CheckedBox is &#9746;
# Unicode character code

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