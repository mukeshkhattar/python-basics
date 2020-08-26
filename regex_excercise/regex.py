# https://developers.google.com/edu/python/regular-expressions


import re

## Search for pattern 'iii' in string 'piiig'.
## All of the pattern must match, but it may appear anywhere.
## On success, match.group() is matched text.
'''
search('r'pattern,text) : serach pattern in test, 'r' flag = raw string. which passes through backslashes without change which is very handy for regular expressions
match = re.search(r'iii', 'piiig') # found, match.group() == "iii"
'''
# match = re.search(r'iii', 'piiig') # found, match.group() == "iii"
match = re.search(r'igs', 'piiig') # not found, match == None

## . = any single char but \n, so ... means 3 chars must match
match = re.search(r'..g', 'p1kgx') # found, match.group() == "1kg"

## \d = digit char, \w = word char (includes numbers too),
# In example below, 3 digits and 3 chars must match
match = re.search(r'\d\d\d', 'p123g') # found, match.group() == "123"
match = re.search(r'\w\w\w', '@@ab1d!!') # found, match.group() == "ab1"

''' Repeatition
hings get more interesting when you use + and * to specify repetition in the pattern

+ -- 1 or more occurrences of the pattern to its left, e.g. 'i+' = one or more i's
* -- 0 or more occurrences of the pattern to its left
? -- match 0 or 1 occurrences of the pattern to its left
Leftmost & Largest
'''
## i+ = one or more i's, as many as possible.
match = re.search(r'pi+', 'piiig') # found, match.group() == "piii"

## Finds the first/leftmost solution, and within it drives the +
## as far as possible (aka 'leftmost and largest').
## In this example, note that it does not get to the second set of i's.
match = re.search(r'i+', 'piigiiii') # found, match.group() == "ii"

## \s* = zero or more whitespace chars
## Here look for 3 digits, possibly separated by whitespace.
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx') # found, match.group() == "1 2   3"
match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx') # found, match.group() == "12  3"
match = re.search(r'\d\s*\d\s*\d', 'xx123xx') # found, match.group() == "123"

## ^ = matches the start of string, so this fails:
match = re.search(r'^b\w+', 'foobar') # not found, match == None
## but without the ^ it succeeds:
match = re.search(r'b\w+', 'foobar') # found, match.group() == "bar"

## ? = 0 or 1 occurance
match = re.search(r'ssa?', 'ssa') # found, match.group() == "ssa"
match = re.search(r'ssa?', 'sdf') # not found
match = re.search(r'ssa?', 'ssdf') # found, match.group() == "ss"

#escape a special char e.g. \. \@
#square brackets
'''
Square brackets can be used to indicate a set of chars, so [abc] matches 'a' or 'b' or 'c'.
The codes \w, \s etc. work inside square brackets too
 dot (.) just means a literal dot.
 For the emails problem, the square brackets are an easy way to add '.' and '-' to the set of chars which can appear around the @ with the pattern r'[\w.-]+@[\w.-]+'
\=
'''
match = re.search(r'[\w._-]+\@1[2-9]+', 'x@1122') # not found
match = re.search(r'[\w._-]+\@1[2-9]+', 'x@122') # found: x@122
match = re.search(r'[\w._-]+\@[\w_-]+\.[\w]+', 'mukesh_khattar.k@swd-edc.com') # found: mukesh_khattar.k@swd-edc.com

#[a-zA-Z] - one char of a-z or A_Z
# ^ ; start of string
match = re.search(r'^[a-zA-Z][\w._-]+\@[\w_-]+\.[\w]+', 'mukesh_khattar.k@swd-edc.com') # found: mukesh_khattar.k@swd-edc.com
match = re.search(r'^[a-zA-Z][\w._-]+\@[\w_-]+\.[\w]+', '1mukesh_khattar.k@swd-edc.com') # not found


'''
group Extraction
Group match e.g. for email address (username_pattern)@(host_pattern)
The "group" feature of a regular expression allows you to pick out parts of the matching text.
'''
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w.-]+)@([\w.-]+)', str)
if match:
  print (match.group())   ## 'alice-b@google.com' (the whole match)
  print (match.group(1))  ## 'alice-b' (the username, group 1)
  print (match.group(2))  ## 'google.com' (the host, group 2)

'''
findall() is probably the single most powerful function in the re module.
Above we used re.search() to find the first match for a pattern.
 findall() finds *all* the matches and returns them as a list of strings, with each string representing one match.
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
  match = re.search(r'^[a-zA-Z][\w._-]+\@[\w_-]+\.[\w]+', '1mukesh_khattar.k@swd-edc.com')
  if match:
    print ('found:', match.group()) ## 'found word:cat'
  else:
    print ('did not find')
