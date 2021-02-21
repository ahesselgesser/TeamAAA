import os
from shutil import copyfile

# 'C:\Users\twins\Desktop\UNO classes\Spring 2021 Semester\CSCI 4970 - Capstone\Python tests'
# https://github.com/ahesselgesser/TeamAAA

source = input("Enter the source location of the file: example C:/Users/bob/word.docx\n")

destination = input("Enter the destination and name of the file: example C:/Users/bob/word_2.docx\n")

# copyfile(source, destination)
copyfile(source, destination)
