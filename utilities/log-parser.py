#https://medium.com/devops-challenge/apache-log-parser-using-python-8080fbc41dda
'''
find top 10 offending IP addresses in apache_logs to detect dos
'''
import re
from collections import Counter
# Open file
f = open('/Users/mukeshkhattar/github_public_repos/examples/Common Data Formats/apache_logs/apache_logs', 'r')
# Feed the file text into findall(); it returns a list of all the found strings
ip_list = re.findall(r'[\d]+\.[\d]+\.[\d]+\.[\d]', f.read())

#create a dict with key:value pairs(ip:count) using Counter class. this dic stores count indesc order
ip_list_by_count=Counter(ip_list)

#Get the top 10 ips. This returms a list of tuples(ip:count)
my_top_10_ip=ip_list_by_count.most_common(10)

#print the top 10
for tuple in my_top_10_ip:
  print('ip:',tuple[0], 'count:', tuple[1])


'''
output:
ip: 32.0.1700.1 count: 2238
ip: 66.249.73.1 count: 538
ip: 33.0.1750.9 count: 467
ip: 46.105.14.5 count: 364
ip: 130.237.218.8 count: 357
ip: 75.97.9.5 count: 273
ip: 207.241.237.2 count: 117
ip: 50.16.19.1 count: 113
ip: 68.180.224.2 count: 106
ip: 209.85.238.1 count: 102
'''



