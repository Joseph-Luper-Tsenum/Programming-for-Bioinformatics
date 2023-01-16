Programming for Bioinformatics | BIOL 7200


Name: Joseph Luper Tsenum


Exercise 8

    

Starting this week we will be using real bioinformatics data and writing (simpler versions of) real world bioinformatics scripts. 
For this week, assume that the user gives you correct inputs all the time. Your script will be graded on the output produced and not how all the errors are handled.
Again, please do not use any modules other than sys. 
Instructions for submission
    • This assignment is due Monday, October 25, 2021, at 11:59pm. Late submissions will receive a 0.
    • The k-mer counter script must be named: <gtusername>_kmer_counter.py
    • The vertical column script should be named: <gtusername>_read_vertical.py
    • The three-way file join script must be named:  <gtusername>_three_way_join.py
    • All scripts should output their tab-separated results to STDOUT 
    • Please submit these three files on Canvas.
    1. K-mer counter in Python
Write a script that reads in a FASTA file and a value of k and calculates the number of times each k-mer is observed within the genome.  A k-mer is a sequence of length k; for example, k-mers of length 2 (k=2) for DNA are AA, AT, AG, AC, CC, CT, CG, CA, TT, TA, TG, TC, GG, GC, GT, and GA
You should only report k-mers with non-zero occurrences.  The output should be printed on the standard output in two, tab-separated columns.  The first column should contain the k-mer sequence and the second column should be the number of times it occurs within the input sequence.  Do not print any extra lines.  The k-mers should be printed alphabetically (i.e., sorted based on their sequence and not on their occurrence).
For the test dataset, you are given a FASTA file (NC_000913.fasta).  This is the genome for E. coli K-12 substr.  We are also providing you with an output file for this genome. If your script can reproduce this output file correctly, it should work fine on other datasets too.

A k-mer is a sequence of length k.  If you are given a sequence AGCTTTTCA and asked to find all possible k-mers with k=5, the solution would be:
AGCTT	1
CTTTT	1
GCTTT	1
TTTCA	1
TTTTC	1

Your script should take two positional arguments (k-mer size and FASTA file), do NOT use getopts or any other modules, and be named <gtusername>_kmer_counter.py

<gtusername>_kmer_counter.py <k> <input FASTA>

    




SCRIPT


##########


#!/usr/bin/env python3


##########


import sys
b = int(sys.argv[1])
a = sys.argv[2]


##########


#Placing sequences in a string
table = ''
filename = 'NC_000913.fasta' #change to 'a'
with open(filename,"r") as fh:
for line in fh.readlines():
	if not line.startswith('>'):
	line = line.rstrip()
	table += line


##########


#How to do k-mer count
counts = {}
kmers = []
num_kmers = len(table)-b+1


##########


# How to loop over k-mer start positions
for i in range(num_kmers):


##########


# How to slice the string to get the k-mer
kmer = table[i:i+b]


##########


# Adding the k-mer to the dictionary if the k-mer is not there
if kmer not in counts:
counts[kmer] = 0


##########


# How to increment the count for this k-mer
counts[kmer] += 1
for kmer in sorted(counts.keys()):
print(kmer,counts[kmer])
