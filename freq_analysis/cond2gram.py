#Name: Adam Petty
#File: cond2gram.py
#searches text files for passed letter and finds
#all digrams starting with that letter


import sys, os, string

x = sys.argv[1]
y = sys.argv[2]
all_length = 0
digrams = {}

cwd = os.getcwd()
os.walk(cwd)

for a, b, c in os.walk(cwd):
	os.chdir(a)
	i = str(a)[29:]
	
	if os.path.exists("%s.txt.gz" % i):
		os.system('gunzip %s.txt.gz' % i)
		with open("%s.txt" % i, 'r') as f:
			s = f.read()
			f.close()
			os.system('gzip %s.txt' % i)
			
			for j, c in enumerate(s):
				if c == x:
					dgram = s[j : j + 2]
					if dgram not in digrams.keys():
						digrams[dgram] = 1;
						all_length += 1
					else:
						digrams[dgram] += 1;
						all_length += 1

print "total count:", all_length

for k in sorted(digrams.keys(), key=lambda q:int(digrams[q]), reverse = True):
	print "%s: %s, %s" % (k, digrams[k], (float(digrams[k]) / float(all_length)))
							


