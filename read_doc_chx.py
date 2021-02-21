import zipfile
from lxml import etree
import re

### This path is relative, and it needs to be an XML document.
xml_tree = etree.parse('C:/Users/twins/Desktop/UNO classes/Spring 2021 Semester/CSCI 4970 - Capstone/Python tests/grad_chxBox_test/word/document.xml')

xml_string = etree.tostring(xml_tree).decode()

# Using this regex, we find all <w:t> tags, not sure if it works with the altered w:t tags though.
reg = re.findall('(?:<w:t>|<w:t xml:space="preserve">).*?</w:t>', xml_string)

if (reg):
    print("We found a checked box!")
else:
    print("My regex didn't work. :(")

prev_match = ""

print("Here are the matches for checked box results!")
for match in reg:
    if (prev_match == "<w:t>&#9746;</w:t>"):
        print(prev_match + " " + match)
    prev_match = match

# 'C:\Users\twins\Desktop\UNO classes\Spring 2021 Semester\CSCI 4970 - Capstone\Python tests'
# https://github.com/ahesselgesser/TeamAAA
# The CheckBox is &#9744;
# The CheckedBox is &#9746;
# Unicode character code