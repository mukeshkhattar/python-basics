'''
Modes:
'r' : default
'w' : write, overwritten , creates if does exist
'r+' : read-write mode, read head is at the begining, write head is at the end (same as in append)
'a' : append
'''

# write method returns the number of chars added
#write mode: creates if no file exists, overwrites an existing file
with open('basics/myfile.txt','r+') as file:
  x=file.write('last line added')
  print('number of chars added:',x) # 15
  print(file.readline())
  print(file.readline())
  print(file.read()) # does not dispaly the last line added above though until it is saved


with open('basics/myfile.txt','r') as file:
  print(file.read())



#Reading one line at a time has the nice quality that not all the file needs to fit in memory at one time --
# handy if you want to look at every line in a 10 gigabyte file without using 10 gigabytes of memory.
# The special mode 'r' is the "Universal" option for text files where it's smart about converting different line-endings so they always come through as a simple '\n'
f=open('basics/small.txt','r')
for line in f:
  print(line.strip()) # strips /n that is added by print
f.close

#large files should be processed line by line instead of reading the whole file in memory
# if you use With clause, you do not have to call close(). Python will close it for you:
with open('basics/small.txt','r') as file:
  for line in file:
    print(line.strip())



# The f.readlines() method reads the whole file into memory and returns its contents as a list of its lines.

with open('basics/small.txt','r') as file:
  lines=file.readlines() #list

print('sorted file:')
lines.sort()
for line in lines:
  print(line)

#alternatively
print('alt method- readline():')
f=open('basics/small.txt','r')
print(f.readline())
print(f.read())


#The f.read() method reads the whole file into a single string, which can be a handy way to deal with the text all at once, such as with regular expressions
print('alt way:2')
f=open('basics/small.txt','r')
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

'''
if certain lines of a file need updates, follow this approach:
read the file in a list of lines and clsoe the file
upadte the lines in list as needed
open the file in write mode and write the list
'''
