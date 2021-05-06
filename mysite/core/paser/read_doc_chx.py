import os
from shutil import copyfile
import zipfile
from lxml import etree
import re

def remove_tags(text):
    """! Remove < > tags from a string.

    @param text - The text that we are removing the tags from.
    @return The text after the tags have been removed.
    """
    clean = '<.*?>\s*'
    return re.sub(clean, '', text)

def copy_and_unzip(source_dir, source_fn, destination_fn, zip_dir):
    """! Copies a file, renames it as a ZIP document, and unzips it.

    @param source_dir - The directory that the original file resides in.
    @param source_fn - The source file name.
    @param destination_fn - The name of the copied file.
    @param zip_dir - The directory that you store the unzipped documents in.
    """
    copyfile(source_dir + "\\" + source_fn, source_dir + "\\" + destination_fn)

    with zipfile.ZipFile(source_dir + "/" + destination_fn, 'r') as zip_ref:
        zip_ref.extractall(source_dir + "/" + zip_dir)

def find_checkbox_elements(xml_path):
    """! Finds all the words directly after the marked checkboxes in the document.

    @param xml_path - The path to the XML document that we are finding marked checkboxes in.
    @return The list of check box elements, the number of SLOs in the document, and a list of lists.
    """
    ## A list of Bloom's Taxonomy keywords that we check for after the checkboxes.
    blooms_taxonomy_list = ['Knowledge', 'Comprehension', 'Application', 'Analysis', 'Synthesis', 'Evaluation']
    ## A list of assessment domain keywords that we check for after the checkboxes.
    assessment_domain_list = ['Examination', 'Product', 'Performance']
    ## A list of assessment type keywords that we check for after the checkboxes.
    assessment_type_list = ['Direct Measure', 'Indirect Measure']
    ## A list of assessment point in the semester keywords that we check for after the checkboxes.
    assessment_point_list = ['In final term of program', 'In final year of program']
    ## A list of assessment population keywords that we check for after the checkboxes.
    assessment_population_list = ['All students', 'Sample of students - Describe below']
    ## A list of assessment frequency keywords that we check for after the checkboxes.
    assessment_frequency_list = ['Once/semester', 'Once/year', 'Other - Describe below']
    ## A list of SLO status keywords that we check for after the checkboxes.
    slo_status_list = ['Met', 'Partially Met', 'Not Met', 'Unknown']
    ## A list of graduate common program keywords that we check for after the checkboxes.
    grad_common_program_list = ['1', '2', '3', '4', 'Not applicable for SLO']

    ## The number of SLOs found in the document. Determined by the number of Bloom's taxonomy keywords found after checked boxes.
    slo_count = 0

    ## Stores all values after checked boxes.
    chkbox_element_list = []
    ## Stores all values after checked boxes that are within the blooms_taxonomy_list.
    blooms_list = ["Bloom's Taxonomy List"]
    ## Stores all values after checked boxes that are within the assessment_domain_list.    
    domain_list = ["Assessment Domain List"]
    ## Stores all values after checked boxes that are within the assessment_type_list.    
    type_list = ["Assessment Type List"]
    ## Stores all values after checked boxes that are within the assessment_point_list.    
    point_list = ["Assessment Point in Program List"]
    ## Stores all values after checked boxes that are within the assessment_population_list.    
    population_list = ["Assessment Population List"]
    ## Stores all values after checked boxes that are within the assessment_frequency_list.    
    frequency_list = ["Assessment Frequency List"]
    ## Stores all values after checked boxes that are within the slo_status_list.    
    status_list = ["SLO Status List"]
    ## Stores all values after checked boxes that are within the grad_common_program_list .   
    common_program_list = ["Grad Common Program SLOs List"]


    ### This is an XML_Tree object that the etree module creates from the XML document.
    xml_tree = etree.parse(xml_path)

    ## This is the XML document in string form.
    xml_string = etree.tostring(xml_tree).decode()

    ## This stores the namespaces for Word documents.
    namespaces = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

    ## Find all the textbox tags in the XML Tree and store them here.
    textboxes = xml_tree.findall('.//w:txbxContent', namespaces)

    ## A list to store the contents of a single text box.
    one_box = []

    ## A set to contain all unique instances of a text box.
    all_box_set = set([])

    ## Append this number to the end of the text box text, because sets don't keep order. This allows us to find the order.
    set_order = 1

    ## Loop through all the textboxes found.
    for box in textboxes:
        ## Find all the text tags in the text boxes.
        text_tags = box.findall('.//w:t', namespaces)
        ## For all the text tags, append the text to one_box list.
        for text_element in text_tags:
            one_box.append(text_element.text)
        ## Join the elements in one_box and add it to the all_box_set.
        all_box_set.add(''.join(one_box) + str(set_order))
        set_order += 1
        ## Clear the one_box list, so that we can start fresh.
        one_box.clear()

    ## Stores the list of all above lists, minus the chckbox_element_list.
    list_of_lists = (blooms_list, domain_list, type_list, point_list, population_list, frequency_list, status_list, common_program_list, all_box_set)

    ## Regular expression used to capture all <w:t> tags.
    reg = re.findall('(?:<w:t>|<w:t xml:space="preserve">).*?</w:t>', xml_string)

    ## Used to store the previous match.
    prev_match = ""

    ## Index through each match found with the regular expression and append appropriate values to the lists.
    for index, match in enumerate(reg):
        ## Some of the matches return empty strings, this is used to increment through the matches to find an appropriate non-empty string.
        empty_counter = 1
        while (match == '<w:t xml:space="preserve"> </w:t>' or match == '<w:t> </w:t>'):
            match = reg[index + empty_counter]
            empty_counter += 1
        ## If the previous match was a checked box, append the current match to the appropriate list.
        if (prev_match == "<w:t>&#9746;</w:t>" or prev_match == "<w:t xml:space=\"preserve\">&#9746;</w:t>"):
            match = remove_tags(match).strip()
            chkbox_element_list.append(match)
            if (match in blooms_taxonomy_list):
                slo_count += 1
                blooms_list.append(match)
            if (match in assessment_domain_list):
                domain_list.append(match)                
            if (match in assessment_frequency_list):
                frequency_list.append(match)                
            if (match in assessment_point_list):
                point_list.append(match)                
            if (match in assessment_population_list):
                population_list.append(match)                
            if (match in assessment_type_list):
                type_list.append(match)                      
            if (match in slo_status_list):
                status_list.append(match)                
            if (match in grad_common_program_list):
                common_program_list.append(match)
        prev_match = match
    return (chkbox_element_list, slo_count, list_of_lists)
    # The CheckBox is &#9744;
    # The CheckedBox is &#9746;
    # Unicode character code