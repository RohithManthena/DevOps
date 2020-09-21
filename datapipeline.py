import os
import sys

# removing the name of this python file which is the first argument
sys.argv.pop(0)

#initializing a list that  has all the arguments 
arguments=sys.argv

#function to run all the files in a directory
def execfiles_in_folder():
    
    #no arguments are given to the python script in run time
    if len(arguments)==0:
        sys.exit("Folder name is not given")

    # only the folder is passed as argument
    elif len(arguments)==1:
        for root, dirs, files in os.walk("D:\\", topdown=False):
            for i in dirs:
                if i==folder:
                    path=root+"\\"+folder
                    break
        files = os.listdir(path)
        for file_ in files:
            exec(open(path+"\\"+file_).read())



    elif len(arguments)==2:
        if arguments[1] != "desc":
            sys.exit("script order ")
    elif len(arguments)==3:
    elif len(arguments)==4:
    elif len(arguments)==5:
    else:
        sys.exit("max 5 arguments should be passed")

    for root, dirs, files in os.walk("D:\\", topdown=False):
        for i in dirs:
            if i==folder:
                path=root+"\\"+folder
                break
    files = os.listdir(path)
    for file_ in files:
        exec(open(path+"\\"+file_).read())  



# removing the name of this python file which is the first argument
sys.argv.pop(0)

#initializing a list that  has all the arguments 
arguments=sys.argv

if len(arguments)==0:
    sys.exit("Folder name is not given")

# only the folder is passed as argument
elif len(arguments)==1:
    execfiles_in_folder(arguments[0])



elif len(arguments)==2:
elif len(arguments)==3:
elif len(arguments)==4:
elif len(arguments)==5:
else:
    sys.exit("max 5 arguments should be passed")

    pass
#

while True:
    folder=input("Input the folder name:")
    if folder:
        break
script_order=input("Do you want the files to be executed in descending ? answer with 'yes' or 'no'")
#while script_order!="yes" or script_order!="no":


for root, dirs, files in os.walk("D:\\", topdown=False):
    for i in dirs:
        if i==folder:
            path=root+"\\"+folder
            break
files = os.listdir(path)
for file_ in files:
    exec(open(path+"\\"+file_).read())





# def find_files(search_path):
#    result = []

# # Wlaking top-down from the root
#    for root, dir, files in os.walk(search_path):
#       if filename in files:
#          result.append(os.path.join(root, filename))
#    return result

# print(find_files("smpl.htm","D:"))


#    for name in files:
#       print(os.path.join(root, name))
#    for name in dirs:
#       print(os.path.join(root, name))

# path = 'D:\STUDY\COURSEWORK\DATA SCIENCE PROGRAMMING\ASSIGNMENTS\PRSA_Data_20130301-20170228'
# for file in os.listdir(path):
#     if (file != 'PRSA_Data_Aotizhongxin_20130301-20170228.csv'):
#         filepath="PRSA_Data_20130301-20170228/"+file
#         data=pd.read_csv(filepath)
#         df=df.append(data)

