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


'''
search('r'pattern,text) : serach pattern in test, 'r' flag = raw string. which passes through backslashes without change which is very handy for regular expressions
importance of rflag
 in particular, \b matches empty string specifically at the start and end of a word.
 re expects the string \b, however normal string interpretation '\b' is converted to the ASCII backspace character,
 so you need to either explicitly escape the backslash ('\\b'), or tell python it is a raw string (r'\b').
'''
re.findall('\b', 'testb') # without r flag , the backslash gets consumed by the python string interpreter and '\b' is converted to the ASCII backspace character. re module gets backspace.
#[]
re.findall('\\b', 'test')  # backslash is explicitly escaped and is passed through to re module
#['', '']
re.findall(r'\b', 'test') # often this syntax is easier
#['', '']

'''
Search for pattern 'iii' in string 'piiig'.
On success, result.group() is resulted text.
# result[0] - the whole string
# result[1] - first group
# result[2] - second group and so on
'''
result = re.search(r'iii', 'piiig') # found, result.group() == "iii"
result = re.search(r'igs', 'piiig') # not found, result == None
if result != None:
  result[0]

'''
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")
r"\bain"
r"ain\b"
'''
result = re.search(r'\bain', 'it is  aining asas') # found,'ain
result[0]

#if r flag is not used, \b is treated as a backspace
result = re.search('\bain', 'it is  aining') # not found

## . = any single char but \n, so ... means 3 chars must result
result = re.search(r'..g', 'p1kgx') # found, result.group() == "1kg"

## \d = digit char,
# \w = alphanumeric and _ [a-zA-Z0-9_]
# In example below, 3 digits and 3 chars must result
result = re.search(r'\d\d\d', 'p123g') # found, result.group() == "123"
result = re.search(r'\w\w\w', '@@ab_1d!!') # found, result.group() == "ab1"
type(result)
result[0]


''' Repeatition
Things get more interesting when you use + and * to specify repetition in the pattern

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

## ^ = results the start of string, so this fails:
result = re.search(r'^b\w+', 'foobar') # not found, result == None
## but without the ^ it succeeds:
result = re.search(r'b\w+', 'foobar') # found, result.group() == "bar"

## ? = 0 or 1 occurance
result = re.search(r'ssa?', 'ssa') # found, result.group() == "ssa"
result = re.search(r'ssa?', 'sdf') # not found
result = re.search(r'ssa?', 'ssdf') # found, result.group() == "ss"

#escape a special char e.g. \.
# @ does not need to be escaped. However if escaped , it does not make a difference and the result is the same
#square brackets
'''
Square brackets can be used to indicate a set of chars, so [abc] resultes 'a' or 'b' or 'c'.
The codes \w, \s etc. work inside square brackets too.
In sets, +, *, ., |, (), $,{} has no special meaning, so
    [+] means: return a match for any '+' character in the string
    dot (.) just means a literal dot.
 For the emails problem, the square brackets are an easy way to add '.' and '-' to the set of chars which can appear around the @ with the pattern r'[\w.-]+@[\w.-]+'
\=
'''
result = re.search(r'[\w.-]+\@1[2-9]+', 'x@1122') # not found
result = re.search(r'[\w.-]+\@1[2-9]+', 'x@122') # found: x@122
result = re.search(r'[\w.-]+\@[\w-]+\.[\w]+', 'mukesh_khattar.k@swd-edc.com') # found: mukesh_khattar.k@swd-edc.com


# Inside a set, ^ in a set means exclude. In a normal use (r'^str' ) means starting with
# example - [^arn]	Returns a match for any character EXCEPT a, r, and n
result = re.search(r'[^arn]', 'rit is  aining')
result[0] # i

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

#  '-'   need to be escaped in set. + and . lose its special meaning when used isnide a set

pattern = '[\w\-+.]+\.[a-zA-Z]+'
result=re.search(pattern, 'a_b-c+d.wdwd.com')
result[0]

# the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case.
pattern = '([1]?[0-9]):([0-5][0-9])( ?)[AaPp][Mm]'
result = re.search(pattern, '2:29 PM')
result[0]
result[1]
result[2]
result[3]
result[4] # error

# OR condition use | . eg. first char needs to be upper char or digit AND two or more chars AND surrounded by ()
pattern = '\(([A-Z]|[0-9])[\w]+\)'
result = re.search(pattern, "wdwd(1aM)wdw") # True
result = re.search(pattern, "wdwd(AM)wdw") # True
result = re.search(pattern, "wdwd(aswd)wdw") # False




# ^- start of string , $ - end of string
#the text passed qualifies as a top-level web address, meaning that it contains alphanumeric characters (which includes
# letters, numbers, and underscores), as well as periods, dashes, and a plus sign,
# followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", et
pattern = '^([\w\-+\.]+)\/([a-zA-Z]+)$'
result = re.search(pattern, "web-addres.com/homepage") # True
result[0]

'''
group Extraction
Group result e.g. for email address (username_pattern)@(host_pattern)
The "group" feature of a regular expression allows you to pick out parts of the resulting text.
'''
str = 'purple alice-b@google.com monkey dishwasher'
result = re.search(r'([\w.-]+)@([\w.-]+)', str)
result[0] ## 'alice-b@google.com' (the whole result)
#extract groups, eq:
result[1] #'alice-b' (the username, group 1)
# eq:
result[2] ## 'google.com' (the host, group 2)



# pattern to find ln, fn where fn should include
# '-' does not need to be escaped if it is first or last char in set
name = 'last-name, firstname  M.'
result = re.search(r'^([\w\s-]+), ([\w\s\.]+)$', name)
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

 # exactly 5 digits, and sometimes, but not always, followed by a dash with 4 more digits.
 # The zip code needs to be preceded by at least one space, and cannot be at the start of the text.
#pattern = '(\w)+(\s)+[0-9][0-9][0-9][0-9][0-9](([-][0-9][0-9][0-9][0-9])|(\s))'
pattern = '(\w)+(\s)+[0-9]{5}(([-][0-9]{4})|(\s))'
result = re.search(pattern, "a 21212-0991 wdw") # True
result[0]
result = re.search(pattern, "a 21212  wdw") # True
result[0]
result = re.search(pattern, "a 2122  wdw") # False
if result:
  result[0]


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
  tuple
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
## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher
#method:1
## \1 is group(1), \2 group(2) in the replacement
result=re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str)
result
str
#method:2
print (re.sub(r'@[\w\.-]+', r'@yo-yo-dyne.com', str))

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
x = re.sub("\s", "9",txt,2)
x # 'The9rain9in Spain'
