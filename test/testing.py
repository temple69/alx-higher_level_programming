""" from git import Repo

files =['test/hello.py','test/doe.py']
commits= ['prints hello world','prints john doe']
repo =Repo('')
print(repo.git.status())
print(repo.git.commit('-m','hello world',author='temple69'))
repo.git.add('test/hello.py','test/doe.py')

for  i in range(len(files)):
    repo.git.add(files[i])
    print(commits[i])
 """
 
import os
files2=[]
stringtxt=[]
""" def ReadTextFromFile(filepath):
    with open(filepath) as f:
        lines = f.readlines()
        return lines


returnedFiles=ReadTextFromFile('./text.txt') 
 #print(returnedFiles )

def Readfile(arr):
    for i in range(len(arr)):
       stripped = arr[i].strip()
       print(stripped )
       if stripped.endswith("O"):
           files.append(arr[i])

Readfile(returnedFiles) 
print(files)

def createfile(arr):
    for i in range(len(arr)):
       open(f'{os.getcwd()}/{arr[i].strip()}','x')

createfile(files) 
  """


""" for file in os.listdir():
    if file.endswith('.txt'):
        files2.append(file)
stripped = files2[3:] """
#converts elememts of list into string
""" for i in range(len(contents)):
    convertToString= str(contents[i])
    stringtxt.append(convertToString)
 """

files=['0-hbtn_status','1-hbtn_header','10-my_github','100-github_commits','2-post_email','3-error_code','4-hbtn_status','5-hbtn_header','6-post_email','7-error_code','8-json_api']
""" for i in range(1,6):
    files.append(i)  """
    

def createfile(arr):
    for i in range(len(arr)):
       open(f'{os.getcwd()}/{arr[i]}.py','x')

createfile(files)  