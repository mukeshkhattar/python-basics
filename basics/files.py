
import os
print(os.listdir())

#Reading one line at a time has the nice quality that not all the file needs to fit in memory at one time --
# handy if you want to look at every line in a 10 gigabyte file without using 10 gigabytes of memory.
# The special mode 'rU' is the "Universal" option for text files where it's smart about converting different line-endings so they always come through as a simple '\n'
f=open('basics/small.txt','rU')
for line in f:
  print(line)
f.close
# The f.readlines() method reads the whole file into memory and returns its contents as a list of its lines.
f=open('basics/small.txt','rU')
lines=f.readlines()
for line in lines:
  print(line)
f.close

#The f.read() method reads the whole file into a single string, which can be a handy way to deal with the text all at once, such as with regular expressions we'll see later.

print('alt way:2')
f=open('basics/small.txt','rU')
afile=f.read()
print(afile)

#write mode: creates if no file exists, overwrites an existing file
f=open('basics/myfile.txt','w')
acontent1='my line1\n'
acontent2='my line2\n'
f.write(acontent1)
f.write(acontent2)
f.close
'''
creates a file with this content:
my line1
my line2
'''

#append
f=open('basics/myfile.txt','a')
acontent3='my line3\n'
acontent4='my line4\n'
f.write(acontent3)
f.write(acontent4)
f.close

'''
creates a file with this content:
my line1
my line2
my line3
my line4
'''

