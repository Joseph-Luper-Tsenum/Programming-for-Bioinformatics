Programming for Bioinformatics | BIOL 7200


Name: Joseph Luper Tsenum


Exercise 7


Question 22-24


Advanced string and list problems

22. Given a string made up of { and }, write a script that determines if all the opened curly
braces have a paired closing brace. Ensure the pairing component, {{}{}} have all curly
braces in pairs whereas }}{{{} do not have them in pairs. A simple counting of opening and
closing curly braces will return pairing for both cases which will be incorrect! Use the
following test cases to see if your code works properly:
Case
(a)
(b)
(c)
Input
{{{}}}
{{}{}}
{{{}}{}}
Paired?
Yes
Yes
Yes
Case
(d)
(e)
(f)
Input
}}{{
{}}{
{{}}}{
Paired?
No
No
No


#!/bin/env python3

x = input("Input a series of curly braces {} to test if they are paired: ")
y = []
for i in x:
	if i == "{":
	y.append(i)
		elif i == "}":
	if (len(y) > 0):
	y.pop()
		else:
print("ERROR!")

	if len(y) == 0:
print ("VALID!")
		else:
print ("ERROR!")


23. Detect if an input string is an English palindrome or not. I.e., words or sequence that reads
the same backwards as forwards. E.g., madam or Anna


#!/bin/env python3

x = input("input a string to see if it is palindromidc: ")

	if x == x[::-1]:
print("The string is palindromic!")
	else:
print("The string is not palindromic!")


24. Detect if an input string is a biological palindrome or not. Biological palindromes are self-
complimentary sequences. E.g., AACAGTTTATAAACTGTT (AACAGTTTA and its reverse
compliment TAAACTGTT) or ACACTGT


#!/bin/env python3

DNA = input("Input the DNA sequence you want to test: ")
dna_dict = {'A':'T','T':'A','G':'C','C':'G'}
start = 0
end = len(DNA)-1
flag = False

	while start < end:
	if DNA[start] == dna_dict[DNA[end]]:
flag = True
	else:
flag = False
start += 1
end -= 1
	if flag == True:
print ("This sequence is a biological palindrome.")
	else:
print("This sequence is not a biological palindrome.")




