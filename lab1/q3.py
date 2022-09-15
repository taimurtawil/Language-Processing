import sys
infile = open(sys.argv[1], 'r')
source = infile.read()
outfile = open(sys.argv[2], 'w')
i = 1
for line in source:
    outfile.write("i   "+line)
    i+=1
outfile.close() 
