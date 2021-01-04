#Name: Adam Petty
#File: all.py
#Collects frequency analysis data from individual
#files and creates a frequency analysis data for all files.

import os, itertools


all_length = 0
gram1 = {}
gram2 = {}
gram3 = {}
gram4 = {}

g1_total = 0
g2_total = 0
g3_total = 0
g4_total = 0

cwd = os.getcwd()
os.walk(cwd)

for a, b, c in os.walk(cwd):
    os.chdir(a)
    if os.path.exists("data.txt"):
        with open ("data.txt", 'r') as f:
        
            for line in itertools.islice(f, 1, 2):
                i = line.index(': ')
                length = int(line[i + 2 : -1])
                all_length += length
        
            for line in itertools.islice(f, 2, None):
                
                j = line.index(':')
                k = line.index(',')
                gram = line[:j]
                freq = line[j + 2: k]
            
                if len(gram) == 4:	
                    if gram not in gram4.keys():
                        gram4[gram] = int(freq)
                        g4_total += int(freq)
                    else:
                        gram4[gram] += int(freq)
                        g4_total += int(freq)
                    
                elif len(gram) == 3:	
                    if gram not in gram3.keys():
                        gram3[gram] = int(freq)
                        g3_total += int(freq)
                    else:
                        gram3[gram] += int(freq)
                        g3_total += int(freq)
                        
                elif len(gram) == 2:	
                    if gram not in gram2.keys():
                        gram2[gram] = int(freq)
                        g2_total += int(freq)
                    else:
                        gram2[gram] += int(freq)
                        g2_total += int(freq)
            
                elif len(gram) == 1:
                    if gram not in gram1.keys():
                        gram1[gram] = int(freq)
                        g1_total += int(freq)
                    else: 
                        gram1[gram] += int(freq)
                        g1_total += int(freq)

                else: print "Invalid n-gram size:", gram
    
        f.close()	


print "length:", all_length

for k in sorted(gram1.keys(), key=lambda q:int(gram1[q]), reverse = True):
    print "%s: %s, %s" % (k, gram1[k], (float(gram1[k]) / float(g1_total)))
                
limit = 0
for k in sorted(gram2.keys(), key=lambda q:int(gram2[q]), reverse = True):
        print "%s: %s, %s" % (k, gram2[k], (float(gram2[k]) / float(g2_total)))
        limit += 1
        if limit == 40: break

limit = 0
for k in sorted(gram3.keys(), key=lambda q:int(gram3[q]), reverse = True):
    print "%s: %s, %s" % (k, gram3[k], (float(gram3[k]) / float(g3_total)))
    limit += 1
    if limit == 40: break

limit = 0
for k in sorted(gram4.keys(), key=lambda q:int(gram4[q]), reverse = True):
	print "%s: %s, %s" % (k, gram4[k], (float(gram4[k]) / float(g4_total)))
	limit += 1
	if limit == 40: break
