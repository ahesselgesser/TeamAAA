import os
from shutil import copyfile
import zipfile
from lxml import etree
import re

# 'C:\Users\twins\Desktop\UNO classes\Spring 2021 Semester\CSCI 4970 - Capstone\Python tests'
# https://github.com/ahesselgesser/TeamAAA

source_dir = input("Enter the source location of the file: example C:/Users/bob/\n")
source_fn = input("Enter the name of the file to copy\n")

#destination_dir = input("Enter the destination and name of the file: example C:/Users/bob/word_2.docx\n")
destination_fn = input("Enter the name of the copied file\n")

# copyfile(source, destination)
copyfile(source_dir + "\\" + source_fn, source_dir + "\\" + destination_fn)

print(source_dir + "/" + destination_fn)

zip_dir = input("Enter name of directory to unzip file\n")

with zipfile.ZipFile(source_dir + "/" + destination_fn, 'r') as zip_ref:
    zip_ref.extractall(source_dir + "/" + zip_dir)

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
    if (prev_match == "<w:t>&#9746;</w:t>" and match != '<w:t xml:space="preserve"> </w:t>'):
        print(prev_match + " " + match)
    prev_match = match

# 'C:\Users\twins\Desktop\UNO classes\Spring 2021 Semester\CSCI 4970 - Capstone\Python tests'
# https://github.com/ahesselgesser/TeamAAA
# The CheckBox is &#9744;
# The CheckedBox is &#9746;
# Unicode character code