# Name: Adam Petty
# File: gutenberg.py
# this file reads each book downloaded by download.py
# and removes spacing and punctuation. This file also
# calls freq.cpp to perform frequency analysis on the
# cleaned up text


import os, string

def cleanup(cs):
    cs = cs.lower()
    xs = []
    for c in cs:
        if c in string.ascii_lowercase:
            xs.append(c)
    return ''.join(xs)


cwd = os.getcwd()
os.walk(cwd)

#for all files in cwd
for x in os.walk(cwd): 
    os.chdir(x[0])
    book = str(x[0])
    i = book[19:]       #i = book number
    cs = ''
    
    if os.path.exists('%s.txt.gz' % i):
        os.system('gunzip %s.txt.gz' % i)
        print "[%s/46394]...reading book %s" % (cnt, i)
        
        
        with open("%s.txt" % i, 'r') as f:
            
            for line in f:
                cs += line
        
        #comment out if already cleaned up
        cs = cleanup(cs)
        f.close()
    
        with open("%s.txt" % i, 'w') as g:
                for j in cs:
                    g.write(j)
        
        os.system('/mnt/hdd/gutenberg/./a.out %s.txt > data.txt' % i)
        os.system('gzip %s.txt' % i)
