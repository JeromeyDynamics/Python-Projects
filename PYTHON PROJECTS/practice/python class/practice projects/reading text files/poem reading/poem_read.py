import os

def lines_count():
    #open file
    file = open('PYTHON PROJECTS\practice\python class/reading text files\poem reading\poem.txt', 'r')
    #checking first char
    for line in file:
        line = line.rstrip()
        if line[0] in 'aeiouAEIOU': #same as if line[0] == 'a' or same as if line[0] == 'e'...
            print(line)
    
    #close the file
    file.close()

lines_count()