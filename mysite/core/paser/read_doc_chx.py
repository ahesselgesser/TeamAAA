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

def copy_and_unzip(source_dir, source_fn, destination_fn, zip_dir):
    copyfile(source_dir + "/" + source_fn, source_dir + "/" + destination_fn)

    with zipfile.ZipFile(source_dir + "/" + destination_fn, 'r') as zip_ref:
        zip_ref.extractall(source_dir + "/" + zip_dir)

def find_checkbox_elements(xml_path):
    blooms_taxonomy_list = ['Knowledge', 'Comprehension', 'Application', 'Analysis', 'Synthesis', 'Evaluation']
    slo_count = 0

    chkbox_element_list = []

    ### This path is relative, and it needs to be an XML document.
    xml_tree = etree.parse(xml_path)

    xml_string = etree.tostring(xml_tree).decode()

    # Using this regex, we find all <w:t> tags, not sure if it works with the altered w:t tags though.
    reg = re.findall('(?:<w:t>|<w:t xml:space="preserve">).*?</w:t>', xml_string)

    prev_match = ""

    for index, match in enumerate(reg):
        empty_counter = 1
        while (match == '<w:t xml:space="preserve"> </w:t>'):
            match = reg[index + empty_counter]
            empty_counter += 1
        if (prev_match == "<w:t>&#9746;</w:t>" or prev_match == "<w:t xml:space=\"preserve\">&#9746;</w:t>"):
            match = remove_tags(match).strip()
            chkbox_element_list.append(match)
            if (match in blooms_taxonomy_list):
                slo_count += 1
        prev_match = match
    return (chkbox_element_list, slo_count)
    # 'C:\Users\twins\Desktop\UNO classes\Spring 2021 Semester\CSCI 4970 - Capstone\Python tests'
    # https://github.com/ahesselgesser/TeamAAA
    # The CheckBox is &#9744;
    # The CheckedBox is &#9746;
    # Unicode character code

#find_checkbox_elements(xml_path)