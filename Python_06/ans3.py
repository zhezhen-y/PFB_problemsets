#!/usr/bin/env python3
#Open and print the reverse complement of each sequence in Python_06.seq.txt. Each line is the following format: seqName\tsequence\n. Make sure to print the output in fasta format including the sequence name and a note in the description that this is the reverse complement. Print to STDOUT and capture the output into a file with a command line redirect '>'.

with open('Python_06.seq.test.txt','r') as fo:
  for line in fo:
    line = line.rstrip()
    name,seq = line.split()
    replace_A = seq.replace('A', 't')
    replace_T = replace_A.replace('T', 'a')
    replace_G = replace_T.replace('G', 'c')
    replace_C = replace_G.replace('C', 'g')
    seq_comp = replace_C.upper()
    seq_comp_rev = seq_comp[::-1]
    print(name,'the reverse complement:',seq_comp_rev)
