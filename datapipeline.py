import os
import sys
import subprocess
from tabulate import tabulate

# removing the name of this python file which is the first argument
sys.argv.pop(0)

#initializing a list that  has all the arguments 
arguments=sys.argv

#the first argument is the folder name which is mandatory
folder=arguments[0]

# if help is passed in the command line, all the commands will be displayed
if "help" in arguments:
    print("MANDATORY - Provide the folder name when executing the python script as ----> python datapipeline.py foldername")
    print("OPTIONAL - If you want the files to executed in desc order use the keyword ----> python datapipeline.py foldername DESC")
    print("OPTIONAL - If you want all the output to be printed in a file use the keyword o- followed by the file name----> python datapipeline.py foldername o-filename.txt")
    print("The resut will be outputted in a file called output in the current directory")
    print("OPTIONAL - If you want only one file to be executed in the directory give the file name preceeded by f- -----> python datapipeline.py foldername f-test.py")
    

else:
    # finding the folder path using os.walk
    for root, dirs, files in os.walk("D:\\", topdown=False):
        for i in dirs:
            if i==folder:
                path=root+"\\"+folder
                break
    consoleoutput=list(tuple())
    headers = ["folder","file"]
    #checking if any file command is given
    fileinput='f-'
    fileinput_provided=[i for i in arguments if fileinput in i] 

    #checking if any output command is given
    outputfile='o-'
    outputfile_provided=[i for i in arguments if outputfile in i]

    # if the file command is passed
    if len(fileinput_provided)==1:
        #if the output command is passed
        if len(outputfile_provided)==1:
            #open a read file and put the output there
            with open(outputfile_provided[0][2:], "wb") as f:
                subprocess.check_call(["python", path+"\\"+fileinput_provided[0][2:]], stdout=f)
                consoleoutput.append((folder,fileinput_provided[0][2:]))
        else:
            exec(open(path+"\\"+arguments).read())
            consoleoutput.append((folder,fileinput_provided[0][2:]))

    
    else:
        #open a read file and put the output there
        if len(outputfile_provided)==1:
            with open(outputfile_provided[0][2:], "wb") as f:
            #run files in descending order
                if "DESC" in arguments:
                    files=os.listdir(path)
                    files.reverse()
                    for file_ in files:
                        print(type(file_))
                        subprocess.check_call(["python", path+"\\"+file_], stdout=f)
                        consoleoutput.append((folder,file_))
                else:
                    files=os.listdir(path)
                    for file_ in files:
                        subprocess.check_call(["python", path+"\\"+file_], stdout=f)
                        consoleoutput.append((folder,file_))

        else:
            if "desc" in arguments:
                files=os.listdir(path)
                files.reverse()
                for file_ in files:
                    exec(open(path+"\\"+file_).read())
                    consoleoutput.append((folder,file_))
            else:
                files=os.listdir(path)
                for file_ in files:
                    exec(open(path+"\\"+file_).read())
                    consoleoutput.append((folder,file_))


print(tabulate(consoleoutput,headers=headers))
