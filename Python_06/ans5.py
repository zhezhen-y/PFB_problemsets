#!/usr/bin/env python3
#You are going to generate a couple of gene list that are saved in files, add their contents to sets, and compare them.
#Open each of the three files and add the geneIDs to a Set. One Set per file.

gene_set = set()
with open("alpaca_all_genes.tsv", 'r') as fo:
  for line in fo:
    line = line.rstrip()
    gene_set.add(line)
gene_set.remove('Gene stable ID')
print(len(gene_set))
