import os

myFiles = os.path.normpath('MovFold') #Folder which contains the stuff
file = open('dirlist.txt', 'w')

for entry in os.scandir(myFiles):
    file.writelines(entry.name + os.linesep)

file.close()