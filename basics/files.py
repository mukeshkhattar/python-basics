
import os
print(os.listdir())

#Reading one line at a time has the nice quality that not all the file needs to fit in memory at one time --
# handy if you want to look at every line in a 10 gigabyte file without using 10 gigabytes of memory.
f=open('basics/small.txt','r')
for line in f:
  print(line)
f.close
# The f.readlines() method reads the whole file into memory and returns its contents as a list of its lines.
f=open('basics/small.txt','r')
lines=f.readlines()
for line in lines:
  print(line)
f.close

#The f.read() method reads the whole file into a single string, which can be a handy way to deal with the text all at once, such as with regular expressions we'll see later.

print('alt way:2')
f=open('basics/small.txt','r')
afile=f.read()
print(afile)


