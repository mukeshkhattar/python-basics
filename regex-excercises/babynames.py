#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  #open file and read it onto a string
  names=[]
  f=open(filename,'r')
  file_contents=f.read()
  #find year Popularity in 2006
  year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', file_contents)
  if not year_match:
    # We didn't find a year, so we'll exit with an error message.
    sys.stderr.write('Couldn\'t find the year!\n')
    sys.exit(1)
  year = year_match.group(1)
  names.append(year)

  #solution # 1
  #the following will create a list of tuples, with each tuple as (rank, name1, name2)
  male_list = re.findall(r'td>(\d*\d)</td><td>(\w+)</td><td>\w+</td>', file_contents)
  female_list = re.findall(r'td>(\d*\d)</td><td>\w+</td><td>(\w+)</td>', file_contents)
  alist=male_list+female_list
  # sort method 1
  # alist.sort(key=lambda atuple:atuple[1])
  blist=[x[1]+ ' '+ x[0] for x in alist]
  # sort method 2
  blist.sort(key=lambda item:item.split()[0])
  # insert the year item
  names=names+blist
  print(names)
  print(len(names))
  print('end of solution1')

  #solution # 2 - More efficient
  names = []
  names.append(year)
  tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', file_contents)
  names_to_rank =  {}
  for rank, boyname, girlname in tuples:
    if boyname not in names_to_rank:
      names_to_rank[boyname] = rank
    if girlname not in names_to_rank:
      names_to_rank[girlname] = rank
  sorted_names = sorted(names_to_rank.keys())
  for name in sorted_names:
    names.append(name + " " + names_to_rank[name])
  print(names)
  print('end of solution2')




def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

if __name__ == '__main__':
  extract_names('regex_excercise/baby2006.html')
