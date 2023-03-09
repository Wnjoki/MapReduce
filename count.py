#!/usr/bin/env python
#mapper.py"""

import sys

data=[
    "2014-04-01 13:45:42,http://example.com/products.html,77.140.91.33,89",
    "2014-10-01 14:39:48,http://example.com/index.html,113.107.99.122,13",
    "2014-06-23 21:27:50,http://example.com/about.html,50.98.73.129,73",
    "2014-01-15 21:27:09,http://example.com/services.html,149.59.51.52,59",
    "2014-05-13 11:43:42,http://example.com/about.html,61.91.88.85,46",
    "2014-02-17 03:17:37,http://example.com/contact.html,68.78.59.117,98"
]

for line in data:
    
    line = line.strip()
 
    words = line.split()
   
    for word in words:
        
        print ('%s\t%s' % (word, 1))

        
#reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
for line in data: 
    line = line.strip()

    word, count = line.split('\t', 1)


    try:
        count = int(count)
    except ValueError:
        
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print ('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word


if current_word == word:
    print ('%s\t%s' % (current_word, current_count))