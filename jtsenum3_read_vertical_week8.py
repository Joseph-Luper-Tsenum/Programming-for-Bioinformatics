Programming for Bioinformatics | BIOL 7200


Name: Joseph Luper Tsenum


Exercise 8



2. Read a file vertically
On Canvas, you will find a file: knownGene.txt. You can read the first (second, third and so on..) row of this file using a normal for loop. But can you read just the first column? What about the nth column? This can be done easily using: “cut -f <n> file_name” in bash. But can you do this in python by reading the file?
Your task for this question is to write a script that takes in one argument k: a column number and print just that column on stdout (your terminal screen). 
For k=1, print column 1, for k=2, print column 2. If the column number does not exist in the file, then tell the user that “k” value is exceeding the file size. There is no column 0, so throw the same error for k=0.
<gtusername>_read_vertical.py <k> <knownGene.txt>
Want to learn more? Look what List Comprehension is in Python. See if you can use that in this question. Using list comprehension is not necessary for this question.





SCRIPT


#!/usr/bin/env python3

import sys
filename = sys.argv[2]
a = sys.argv[1]


##########


k = a-1
column =[]


##########

if a > 11:
    print("Error the column value exceeds the columns present.")
    sys.exit(0)


##########


elif a <= 0:
    print(f"There is no {a} column.")
    sys.exit(0)


##########


with open(filename,"r") as fh:
 for line in fh:
    row = line.strip().split("\t")
    column.append(row[k])
print(column)

