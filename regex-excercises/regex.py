# https://developers.google.com/edu/python/regular-expressions
# https://docs.python.org/3/howto/regex.html
'''
Check out the following links for more information:

https://docs.python.org/3/howto/regex.html
https://docs.python.org/3/library/re.html
https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy
Shout out to https://regex101.com, which will explain each stage of a regex.
https://regexcrossword.com/
'''
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

'''
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")
r"\bain"
r"ain\b"
'''

# [^arn]	Returns a match for any character EXCEPT a, r, and n

# 	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any '+' character in the string

## . = any single char but \n, so ... means 3 chars must result
result = re.search(r'..g', 'p1kgx') # found, result.group() == "1kg"

## \d = digit char, \w = word char (includes numbers too),
# \w = [a-zA-Z0-9_]
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

# if pattern needs to include literals  '-' and '.' , these need to be escaped. '+' loses its special meaning when used isnide a set

pattern = '[\w_+\-\.]+\.[a-zA-Z]+'
result=re.search(pattern, 'a_b-c+d.wdwd.com')
result[0]

# the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case.
pattern = '([1]?[0-9]):([0-5][0-9])( ?)[AaPp][Mm]'
result = re.search(pattern, '2:29 PM')

# OR condition use | . eg. first char needs to be upper char or digit AND two or more chars AND surrounded by ()
pattern = '\(([A-Z]|[0-9])[\w]+\)'
result = re.search(pattern, "wdwd(1aM)wdw") # True
result = re.search(pattern, "wdwd(AM)wdw") # True
result = re.search(pattern, "wdwd(aswd)wdw") # False
 # exactly 5 digits, and sometimes, but not always, followed by a dash with 4 more digits.
 # The zip code needs to be preceded by at least one space, and cannot be at the start of the text.
pattern = '(\w)+(\s)+[0-9][0-9][0-9][0-9][0-9](([-][0-9][0-9][0-9][0-9])|(\s))'
result = re.search(pattern, "a 21212-0991 wdw") # True
# eq below
result[0]
result.group()
result.group(0)

# ^- start of string , $ - end of string
#the text passed qualifies as a top-level web address, meaning that it contains alphanumeric characters (which includes
# letters, numbers, and underscores), as well as periods, dashes, and a plus sign,
# followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", et
pattern = '^([\w_\-+\.]+)\.([a-zA-Z]+)$'
result = re.search(pattern, "web-addres.com/homepage") # True
result[0]

'''
group Extraction
Group result e.g. for email address (username_pattern)@(host_pattern)
The "group" feature of a regular expression allows you to pick out parts of the resulting text.
'''
str = 'purple alice-b@google.com monkey dishwasher'
result = re.search(r'([\w.-]+)@([\w.-]+)', str)
# return tuple of all group values
result.groups() # ('alice-b', 'google.com')
#eq below
result.group(0) ## 'alice-b@google.com' (the whole result)
result.group() ## 'alice-b@google.com' (the whole result)
result[0] ## 'alice-b@google.com' (the whole result)
#extract groups, eq:
result.group(1)# 'alice-b' (the username, group 1)
result[1]
# eq:
result.group(2) ## 'google.com' (the host, group 2)
result[2]


# pattern to find ln, fn where fn should include
# '-' does not need to be escaped if it is first or last char in set
name = 'last-name, firstname  M.'
result = re.search(r'^(\w*), (\w*\s*\w*\.?)$', name)
result = re.search(r'^([\w\s\.-]+), ([\w\s\.]+)$', name)
result[0]
result[1]
result[2]


# exact specified number of instances
zip='here it is 12121'
result = re.search(r'\d{5}', zip)
result[0] # '12121'
zip='as 1212 ss'
result = re.search(r'\d{5}', zip)
result[0] # None



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


# The split() function returns a list where the string has been split at each match:
#split at each whitespace:
txt = "The rain in Spain"
x = re.split("\s", txt)
x # ['The', 'rain', 'in', 'Spain']

#split with maxsplit parameter
#split at first  whitespace occurance

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
x # ['The', 'rain in Spain']

# substitute function
# replace whitespace with 9
txt = "The rain in Spain"
x = re.sub("\s", "9", txt) # 'The9rain9in9Spain'
x


# You can control the number of replacements by specifying the count parameter:
txt = "The rain in Spain"
x = re.sub("\s", "9",txt,2) # 'The9rain9in9Spain'
x # 'The9rain9in Spain'

# Driver code
if __name__ == '__main__':
  result = re.search(r'^[a-zA-Z][\w._-]+\@[\w_-]+\.[\w]+', '1mukesh_khattar.k@swd-edc.com')
  if result:
    print ('found:', result.group()) ## 'found word:cat'
  else:
    print ('did not find')
