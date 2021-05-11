import re
import sys
import os

file = "/home/andrea/EN2033/final_project/doctor_who_corpus/prueba/d1_s1.txt"

def remove_parentheses():
    with open(file, "r") as f:
        data = f.read()

    with open(file, "w") as f:
        f.write(re.sub(r"\(([^\)]+)\)", "", data))


file2 = "/home/andrea/EN2033/final_project/doctor_who_corpus/prueba/d1_s1.txt"

def remove_brackets():
    with open(file2, "r") as z:
        data = z.read()

    with open(file2, "w") as z:
        z.write(re.sub(r"\[(.*?)\]", "", data))



def remove_blank_lines():
    with open(file2, "r") as f:
        lines = f.readlines()

    with open(file2, "w") as f:
        for line in lines:
            if line.strip("\n") != "":
                f.write(line)
                #print(f)


entries = os.listdir('/home/andrea/EN2033/final_project/doctor_who_corpus/prueba')
for entry in entries:
    #print(entry)
    remove_parentheses()
    remove_brackets()
    remove_blank_lines()



'''
file3 = "/home/andrea/EN2033/final_project/doctor_who_corpus/d1_s1.txt"

# Read lines as a list
fh = open(file3, "r")
lines = fh.readlines()
fh.close()

# Weed out blank lines with filter
lines = filter(lambda x: not x.isspace(), lines)

# Write
fh = open("output", "w")
fh.write("".join(lines))
# should also work instead of joining the list:
# fh.writelines(lines)
fh.close()
'''




#myfile = "/home/andrea/EN2033/final_project/doctor_who_corpus/myfile.txt"

#print(myfile)



