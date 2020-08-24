import sys
from collections import Counter

### most top 20 most common words sorted so the most common word is first
def print_top(filename):
  words_list=[]
  f=open(filename,'rU')
  for line in f:
    line_words=line.split()
    line_words=[ x.lower() for x in line_words ]
    words_list+=line_words
  words_count_map=Counter(words_list)
  words_count_map_top_20=words_count_map.most_common(20) # it is a list
  words_count_map_top_20.sort(reverse=True, key=lambda atuple:atuple[1])
  print(words_count_map_top_20)
  for atuple in words_count_map_top_20:
    print(atuple[0],atuple[1])


if __name__ == '__main__':
  print_top('apache_logs')
