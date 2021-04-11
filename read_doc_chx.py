import os
from shutil import copyfile
import zipfile
from lxml import etree
import re

## https://medium.com/@jorlugaqui/how-to-strip-html-tags-from-a-string-in-python-7cb81a2bbf44
def remove_tags(text):
    """Remove < > tags from a string"""
    clean = '<.*?>\s*'
    return re.sub(clean, '', text)

def copy_and_unzip(source_fn):
    # 'C:\Users\twins\Desktop\UNO classes\Spring 2021 Semester\CSCI 4970 - Capstone\Python tests'
    # https://github.com/ahesselgesser/TeamAAA

    source_dir = "C:\\Users\\twins\\Desktop\\UNO classes\\Spring 2021 Semester\\CSCI 4970 - Capstone\\Python tests"  # input("Enter the source location of the file: example C:/Users/bob/\n")
    #source_fn =  "undergrad2019-regular.docx" #input("Enter the name of the file to copy\n")

    #destination_dir = input("Enter the destination and name of the file: example C:/Users/bob/word_2.docx\n")
    destination_fn =  "undergrad2019-accredited.zip" # input("Enter the name of the copied file\n")

    # copyfile(source, destination)
    copyfile(source_dir + "\\" + source_fn, source_dir + "\\" + destination_fn)

    print(source_dir + "/" + destination_fn)

    zip_dir = "grad_chxBox_test" #input("Enter name of directory to unzip file\n")

    with zipfile.ZipFile(source_dir + "/" + destination_fn, 'r') as zip_ref:
        zip_ref.extractall(source_dir + "/" + zip_dir)



def find_checkbox_elements():
    ### UNCOMMENT THIS IN PRODUCTION
    #copy_and_unzip()
    blooms_taxonomy_list = ['Knowledge', 'Comprehension', 'Application', 'Analysis', 'Synthesis', 'Evaluation']
    slo_count = 0

    chkbox_element_list = []

    ### This path is relative, and it needs to be an XML document.
    xml_tree = etree.parse('C:/Users/twins/Desktop/UNO classes/Spring 2021 Semester/CSCI 4970 - Capstone/Python tests/grad_chxBox_test/word/document.xml')

    xml_string = etree.tostring(xml_tree).decode()

    # Using this regex, we find all <w:t> tags, not sure if it works with the altered w:t tags though.
    reg = re.findall('(?:<w:t>|<w:t xml:space="preserve">).*?</w:t>', xml_string)

    """ For testing purposes
    if (reg):
        print("We found a checked box!")
    else:
        print("My regex didn't work. :(")
    """

    prev_match = ""

    #print("Here are the matches for checked box results!")
    for index, match in enumerate(reg):
        if (match == ''):
            match[index] += 1
        if (prev_match == "<w:t>&#9746;</w:t>" or prev_match == "<w:t xml:space=\"preserve\">&#9746;</w:t>"):
            match = remove_tags(match).strip()
            #print(match)
            chkbox_element_list.append(match)
            if (match in blooms_taxonomy_list):
                slo_count += 1
        prev_match = match
    #print("SLO Count = " + str(slo_count))
    return (chkbox_element_list, slo_count)
    # 'C:\Users\twins\Desktop\UNO classes\Spring 2021 Semester\CSCI 4970 - Capstone\Python tests'
    # https://github.com/ahesselgesser/TeamAAA
    # The CheckBox is &#9744;
    # The CheckedBox is &#9746;
    # Unicode character code

find_checkbox_elements()