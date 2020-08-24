import sys
from collections import Counter
# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def print_words(filename):
  words_list=[]
  f=open(filename,'rU')
  for line in f:
    line_words=line.split()
    line_words=[ x.lower() for x in line_words ]
    words_list+=line_words
  words_count_map=Counter(words_list)
  unique_word_list=list(words_count_map.keys())
  unique_word_list_sorted=sorted(unique_word_list)
  for word in unique_word_list_sorted:
    print(word,words_count_map[word])

if __name__ == '__main__':
  print_words('small.txt')
