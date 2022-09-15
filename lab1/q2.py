import sys
infile = open(sys.argv[1], 'r')
source = infile.read()
outfile = open(sys.argv[2], 'w')
outfile.write(source)
outfile.close() 
