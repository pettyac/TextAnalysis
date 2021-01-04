# Name: Adam Petty
# File: books.py
# This file creates a list of book numbers from gutenberg.org
# in English and non audio book format. (a - z) & #.


import os, urllib, time
import random


url = 'https://gutenberg.org/browse/titles/'
masterlist = []


'''
goes to the above url and searches each page of books
sorted by title, a-z and #, and collects page source info
'''
'''
for i in range(ord('a'), ord('z') + 1):
    os.chdir('/home/adam/CISS451/gutenberg')
    time.sleep(random.randrange(3,8))
    f = urllib.urlopen(url + chr(i))
    s = f.read()
    os.chdir('/home/adam/CISS451/gutenberg/books')
    file("%s.txt" % chr(i), "w").write(s)
'''


'''
loops through a - z and extracts book numbers from page source
that are in English and non audio book and excludes duplicates
'''
os.chdir('/home/adam/CISS451/gutenberg/books')

for i in range(ord('a'), ord('z') + 1):
    xs = []
    books = {}
    ebooks = "/ebooks/"         # where to find the book ID
    audio = "Audio Book"        # filters out audio books
    y = 1
    
    with open("%s.txt" % chr(i), 'r') as f:
    
        for line in f:
            if '(English)' in line:
                xs.append(str(line))

        for x in xs:
            if ebooks in x and audio not in x:
                j = x.index('books/')
                j += 6
                k = x.index('">', j)
                if x[j:k] not in books.values():
                    books[y] = x[j:k]
                    masterlist.append(x[j:k])
                    y += 1

    with open ("books(%s).txt" % chr(i), 'w') as g:
        for key, val in books.items():
            g.write("%s %s'\n'" % (key, val))	

'''
dont forget about '#'
'''
with open("#.txt", 'r') as f:
    y = 1
    for line in f:
            if '(English)' in line:
                xs.append(str(line))

    for x in xs:
        if ebooks in x and audio not in x:
            j = x.index('books/')
            j += 6
            k = x.index('">', j)
            if x[j:k] not in books.values():
                books[y] = x[j:k]
                masterlist.append(x[j:k])
                y += 1
    
with open ("books(#).txt", 'w') as g:
    for key, val in books.items():
        g.write("%s %s'\n'" % (key, val))	

'''
writes the full list as a file
'''
with open ("masterlist.txt", 'w') as h:
    for item in masterlist:
        h.write("%s '\n'" % item)
