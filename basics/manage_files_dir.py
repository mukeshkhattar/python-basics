import os
from datetime import datetime


#delete file
#os.remove("file.txt") # FileNotFoundError if not exists

#rename a file
#os.rename('old','new') # FileNotFoundError if not exists

# check if a file exists
x = os.path.exists('file') # True / False
print(x)
y = os.path.isfile('basics/myfile.txt') #True
y

# file size in bytes
print(os.path.getsize('basics/myfile.txt'))

#last modified
atimestamp=os.path.getmtime('basics/myfile.txt')
print(atimestamp) # seconds since 1970
adatetime=datetime.fromtimestamp(atimestamp)
print(adatetime) # 2020-08-29 10:07:47.449870


#find the abs path
y = os.path.abspath('basics/myfile.txt')
print(y) # /Users/mukeshkhattar/github_public_repos/python-samples/basics/myfile.txt

#current working dir
y = os.getcwd()

print(y)

#mkdir and chdir rmdir
#os.mkdir('test')
#os.chdir('test') # cwd is test now
#os.rmdir('test') # works only if dir is empty , cwd is parent of test now
alist = os.listdir() # returns a list of all files and directories in given di
print(alist)
#If an item returned by listdir is a file or a dir
os.path.isdir('x')
os.path.isfile('x')


#last modified
atimestamp=os.path.getmtime('basics/myfile.txt')
adatetime=datetime.fromtimestamp(atimestamp)
type(adatetime)
"timestamp - {} datetime {} date-{} time-{}".format(atimestamp,adatetime,adatetime.strftime('%m-%d-%y'),adatetime.strftime('%H-%M-%S'))
