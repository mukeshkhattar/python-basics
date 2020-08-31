# https://developers.google.com/edu/python/regular-expressions
import re

## Search for pattern 'iii' in string 'piiig'.
## All of the pattern must result, but it may appear anywhere.
## On success, result.group() is resulted text.
'''
search('r'pattern,text) : serach pattern in test, 'r' flag = raw string. which passes through backslashes without change which is very handy for regular expressions
result = re.search(r'iii', 'piiig') # found, result.group() == "iii"
'''
# result = re.search(r'iii', 'piiig') # found, result.group() == "iii"
result = re.search(r'igs', 'piiig') # not found, result == None

## . = any single char but \n, so ... means 3 chars must result
result = re.search(r'..g', 'p1kgx') # found, result.group() == "1kg"

## \d = digit char, \w = word char (includes numbers too),
# In example below, 3 digits and 3 chars must result
result = re.search(r'\d\d\d', 'p123g') # found, result.group() == "123"
result = re.search(r'\w\w\w', '@@ab1d!!') # found, result.group() == "ab1"

''' Repeatition
hings get more interesting when you use + and * to specify repetition in the pattern

+ -- 1 or more occurrences of the pattern to its left, e.g. 'i+' = one or more i's
* -- 0 or more occurrences of the pattern to its left
? -- result 0 or 1 occurrences of the pattern to its left
Leftmost & Largest
'''
## i+ = one or more i's, as many as possible.
result = re.search(r'pi+', 'piiig') # found, result.group() == "piii"

## Finds the first/leftmost solution, and within it drives the +
## as far as possible (aka 'leftmost and largest').
## In this example, note that it does not get to the second set of i's.
result = re.search(r'i+', 'piigiiii') # found, result.group() == "ii"

## \s* = zero or more whitespace chars
## Here look for 3 digits, possibly separated by whitespace.
result = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx') # found, result.group() == "1 2   3"
result = re.search(r'\d\s*\d\s*\d', 'xx12  3xx') # found, result.group() == "12  3"
result = re.search(r'\d\s*\d\s*\d', 'xx123xx') # found, result.group() == "123"

## ^ = resultes the start of string, so this fails:
result = re.search(r'^b\w+', 'foobar') # not found, result == None
## but without the ^ it succeeds:
result = re.search(r'b\w+', 'foobar') # found, result.group() == "bar"

## ? = 0 or 1 occurance
result = re.search(r'ssa?', 'ssa') # found, result.group() == "ssa"
result = re.search(r'ssa?', 'sdf') # not found
result = re.search(r'ssa?', 'ssdf') # found, result.group() == "ss"

#escape a special char e.g. \. \@
#square brackets
'''
Square brackets can be used to indicate a set of chars, so [abc] resultes 'a' or 'b' or 'c'.
The codes \w, \s etc. work inside square brackets too
 dot (.) just means a literal dot.
 For the emails problem, the square brackets are an easy way to add '.' and '-' to the set of chars which can appear around the @ with the pattern r'[\w.-]+@[\w.-]+'
\=
'''
result = re.search(r'[\w._-]+\@1[2-9]+', 'x@1122') # not found
result = re.search(r'[\w._-]+\@1[2-9]+', 'x@122') # found: x@122
result = re.search(r'[\w._-]+\@[\w_-]+\.[\w]+', 'mukesh_khattar.k@swd-edc.com') # found: mukesh_khattar.k@swd-edc.com

# escape [] if it is patterns e.g. if we need '[process id]' in the line below
line ='sqxwc wecwec[12121] xwcwecc'
result=re.search(r'\[\d+\]',line)
# print the result using one of the following
result.group(0) # '[12121]'
result[0] # '12121'

#in abobe if just process_id is needed
line ='sqxwc wecwec[12121] xwcwecc'
result=re.search(r'\[(\d+)\]',line)
result[0] # '[12121]'
result[1] # '12121'

#[a-zA-Z] - one char of a-z or A_Z
# ^ ; start of string
result = re.search(r'^[a-zA-Z][\w._-]+\@[\w_-]+\.[\w]+', 'mukesh_khattar.k@swd-edc.com') # found: mukesh_khattar.k@swd-edc.com
result = re.search(r'^[a-zA-Z][\w._-]+\@[\w_-]+\.[\w]+', '1mukesh_khattar.k@swd-edc.com') # not found


'''
group Extraction
Group result e.g. for email address (username_pattern)@(host_pattern)
The "group" feature of a regular expression allows you to pick out parts of the resulting text.
'''
str = 'purple alice-b@google.com monkey dishwasher'
result = re.search(r'([\w.-]+)@([\w.-]+)', str)
if result:
  print (result.group())   ## 'alice-b@google.com' (the whole result)
  print (result.group(1))  ## 'alice-b' (the username, group 1)
  print (result.group(2))  ## 'google.com' (the host, group 2)

'''
findall() is probably the single most powerful function in the re module.
Above we used re.search() to find the first result for a pattern.
 findall() finds *all* the resultes and returns them as a list of strings, with each string representing one result.
'''
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
  # do something with each found email string
  print (email)

# findall and groups
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print (tuples)  ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
  print (tuple[0])  ## username
  print (tuple[1])  ## host

'''
findall()  with files
example below extracts IP addresses from apache file
'''
# Open file
f = open('/Users/mukeshkhattar/github_public_repos/examples/Common Data Formats/apache_logs/apache_logs', 'r')
# Feed the file text into findall(); it returns a list of all the found strings
strings = re.findall(r'[\d]+\.[\d]+\.[\d]+\.[\d]', f.read())
print(strings)

#subtir=tution
# this code updates emailaddresses with domain name
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## re.sub(pat, replacement, str) -- returns new string with all replacements,
## \1 is group(1), \2 group(2) in the replacement
print (re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str))
## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher




# Driver code
if __name__ == '__main__':
  result = re.search(r'^[a-zA-Z][\w._-]+\@[\w_-]+\.[\w]+', '1mukesh_khattar.k@swd-edc.com')
  if result:
    print ('found:', result.group()) ## 'found word:cat'
  else:
    print ('did not find')
