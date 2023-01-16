Programming for Bioinformatics | BIOL 7200


Name: Joseph Luper Tsenum


Exercise 8




3. Three-way file join
You are given three files:
    a) knownGene.txt
    b) kgXref.txt
    c) InfectiousDisease-GeneSets.txt
The first two files have been downloaded from ftp://hgdownload.cse.ucsc.edu/goldenPath/hg19/database and are described in the sql files (knownGene.sql and kgXref.sql) located in the same ftp location. The third file is the result of manual curation by one of your collaborators.
While the full description of the first two files can be found in the above-noted sql files, here is the information you need to answer this question:
    a) The knownGene.txt file is a tab-separated file that has multiple columns, but you are only interested in columns 1 (UCSC id), 2 (chromosome), 4 (transcription start position) and 5 (transcription stop position).
    b) The kgXref.txt file is also tab-separated, and the columns we are interested in are 1 (UCSC id) and 5 (gene name).  Entries with missing information are represented as blanks within this file.  Try pasting the file in Excel to see how it is formatted.
Your task is to find the genomic coordinates for the genes listed in the InfectiousDisease-GeneSets.txt file.  The output should be printed on the standard output in four, tab-separated columns and will look like this (tab-separated fields)
Gene	Chr	Start	Stop
ACTB	chr7	5566778	5570232
ACTG1	chr17	79476996	79479892
ADCY3	chr2	25042038	25142055
ADCY9	chr16	4012649	4166186
The output should be sorted alphabetically by gene name.
Your script should take three positional arguments, do NOT use getopts, and be named <gtusername>_three_way_join.py

<gtusername>_three_way_join.py  knownGene.txt  kgXref.txt  InfectiousDisease-GeneSets.txt

Some of the assumptions you will have to make:
    1) UCSC id is the unique identifier for knownGene.txt and acts as a connector between knownGene.txt and kgXref.txt
    2) A gene can have multiple transcripts listed in kgXref.txt and hence multiple UCSC ids associated with it.  If this happens, pick the FIRST set of coordinates for the gene.  This is a simplifying assumption, and this is what we will be using for testing your code.
    3) Genes can be absent from the kgXref table; this is ok.  The inconsistency is due to discordance in the update dates of the table and GeneSets file, but there shouldn’t be a lot of these cases.

Sample output files for your reference:
    1) q1-3mer.out.txt – This is a sample output produced from the input file (NC000913.fasta) and a k-mer size of 3
    2) q1-4mer.out.txt – This is a sample output produced from the input file (NC000913.fasta) and a k-mer size of 4
    3) q3-geneSetCoordinates.txt – this is the final expected output file for provided input file.




SCRIPT


##########


#!/usr/bin/env python3


##########


#Open all files
import sys
file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]


##########


#Open knownGene.txt
knownGene = {}
col1 = []
row1=[]
 with open(file1,"r") as fh1:
   for line in fh1:
row1 = line.strip().split("\t")
chromosome = row1[1]
start = row1[3]
stop = row1[4]
ucsc_id = row1[0]
col1 = [chromosome,start,stop]
knownGene[ucsc_id] = col1
Xref = {}


##########


#Open kgXref.txt
    with open(file2,"r") as fh2:
      for line in fh2:
row2 = line.strip().split("\t")
ucsc = row2[0]
gene_name = row2[4]
Xref[gene_name] = ucsc
col3 = []


##########


#Open InfectiousDisease-GeneSets.txt
   with open(file3,"r") as fh3:
     for line in fh3:
line = line.rstrip()
col3.append(line)


##########


#To ensure that the title doesn't show
col3 = col3[1:]
   for x in Xref.keys():
      if x in col3:
ucsc_id = Xref[x] 
print(f'{x} \t {knownGene[ucsc_id][0]} \t {knownGene[ucsc_id][1]} \t
{knownGene[ucsc_id][2]}')



