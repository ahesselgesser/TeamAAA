Team AAA
Team member

"Zijun Mei" and "Trent Wisecup" and "Alex Hesselgesser"
Abstract

We will be creating a web application that users can upload Student Learning Outcome reports in pdf or word formats to. The website will process the documents and convert them into a format consistent with the database created for SLOs during a previous capstone project. The website will also perform data analysis on the data uploaded, and natural language analysis.
Milestone 2

For milestone 2, we have made some work towards parsing the Word documents.
How to use the Application

First, clone the repository to your local machine:

git clone https://github.com/ahesselgesser/TeamAAA.git

You need to use the parse_script branch

Before running, you need to install several tools.

pip install os
pip install shutil
pip install zipfile
pip install lxml
pip install re
pip install docx

For "read_doc_chx.py":
  On line 17: You need to change the source_dir to the directory you are running the Python file from
  On line 18: You need to insure that the undergrad2018-regularv2.docx file is in that directory
  
The "copy_and_unzip()" function copies the source_fn file from the source_dir, renames it as the string in destination_fn.
It then unzips it into the zip_dir. 
The "find_checkbox_elements" uses the LXML package to in combination with the RE package to use regex to find instances of checkboxes within the document.xml of the original Word document.
This particularly finds the words immediately following the checkboxes. It also counts the SLO's by comparing the words to the bloom's taxonomy list.

Next is the "reading_ug2018.py" file:
  The "regex_inc()" method takes a regex list, a counter, and a list to hold the matches.
    It will run through the regexes in your regex list, until it hits the counter and append the matches to the list.
  On line 20, you will need to point docx.Document() to the undergrad2018-regularv2.docx file.
  We move down, and we loop through all of the captured paragraphs in the document. All the paragraphs that docx can read, at least.
  And we run our regex lists on those paragraphs, until we capture what we need.
  
  We then look at the first table in the document.
  We loop through the rows in the table and append the SLO data to a list.
  We move to the second table, which is unfortunately not the single-cell table just below the initial SLO table.
  We loop through that table capturing the information within, and do the same thing for the table below.
And that is the extent of our parser right now.

Here is the video instruction of the milestone2: https://use.vg/L1bZmy
Release Notes

What we are doing in this milestone is creating an parser script that we can integrate into our Django framework.
