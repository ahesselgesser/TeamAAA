import os
from shutil import copyfile
import zipfile

# 'C:\Users\twins\Desktop\UNO classes\Spring 2021 Semester\CSCI 4970 - Capstone\Python tests'
# https://github.com/ahesselgesser/TeamAAA

source_dir = input("Enter the source location of the file: example C:/Users/bob/\n")
source_fn = input("Enter the name of the file to copy\n")

#destination_dir = input("Enter the destination and name of the file: example C:/Users/bob/word_2.docx\n")
destination_fn = input("Enter the name of the copied file\n")

# copyfile(source, destination)
copyfile(source_dir + "\\" + source_fn, source_dir + "\\" + destination_fn)

print(source_dir + "/" destination_fn)

zip_dir = input("Enter name of directory to unzip file\n")

with zipfile.ZipFile(source_dir + "/" + destination_fn, 'r') as zip_ref:
    zip_ref.extractall(source_dir + "/" + zip_dir)