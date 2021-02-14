import zipfile
from lxml import etree

def get_word_xml(docx_filename):
    with open(docx_filename) as f:
        zip = zipfile.ZipFile(f)
        xml_content = zip.read('word/document.xml')
    return xml_content

# def _check_element_is(self, element, type_char):
def _check_element_is(element, type_char):
    word_schema = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
    return element.tag == '{%s}%s' % (word_schema, type_char)

xml_tree = etree.parse('C:/Users/twins/Desktop/UNO classes/Spring 2021 Semester/CSCI 4970 - Capstone/Python tests/chxTest/word/document.xml')

print(etree.tostring(xml_tree))

# The CheckBox is &#9744;
# The CheckedBox is &#9746;

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