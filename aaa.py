import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#


def matchingStrings(strings,queries):
   z = strings
   y = queries
   b =len(queries)
   a= len(strings)
   '''
   a = int(input())
   for h in range(0,a):
       x=input()
       z.append(x)
   b = int(input())
   for k in range(0,b):
       y.append(input())
    #l = len(strings)
    #m = len(queries)
'''
   c=list() 
   
   for i in range(0,b):
      count = 0
      for j in range(0,a):
         cha = y[i]
         if z[j] == cha:
            count += 1
      c.append(count)
   return c

'''
c=list()
strings  = list()
queries = list()
db=cr(strings,queries)
print(db)
'''
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    resp = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, resp)))
    fptr.write('\n')

    fptr.close()
