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
print(os.getcwd())
files=['101-square','102-square','100-singly_linked_list','103-magic_class']
def createfile(arr):
    for i in range(len(arr)):
        open(f'{os.getcwd()}/{arr[i]}.py','x')
createfile(files)