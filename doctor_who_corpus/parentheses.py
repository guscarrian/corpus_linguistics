import re
import sys
import os

#This function removes everything inside parentheses (including the parentheses)
def remove_parentheses(file_path):
    with open(file_path, "r") as f:
        data = f.read()

    with open(file_path, "w") as f:
        f.write(re.sub(r"\(([^\)]+)\)", "", data))


#This function removes everything inside square brackets (including the square brackets)
def remove_brackets(file_path):
    with open(file_path, "r") as z:
        data = z.read()

    with open(file_path, "w") as z:
        z.write(re.sub(r"\[(.*?)\]", "", data))


#This function removes any blanck line
def remove_blank_lines(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    with open(file_path, "w") as f:
        for line in lines:
            if line.strip("\n") != "":
                f.write(line)
                #print(f)



file_folder = '/home/andrea/repos/corpus_linguistics/doctor_who_corpus/first_doctor'

#This function checks all the files in a directory and picks up only the .txt files.
#Once the .txt files are collected, it gets the path for every .txt file.
def complete_process(some_directory):
    txt_files = []
    for file_name in os.listdir(some_directory):
        #print(file_name)
        if file_name.endswith('.txt'):
            txt_files.append(file_name)
        
    #print(txt_files)
    for file in txt_files:
        #dict[file] = 
        file_path = some_directory + "/" + file
        #print(file_path)
        remove_parentheses(file_path)
        remove_brackets(file_path)
        remove_blank_lines(file_path)
    

complete_process(file_folder)
