Programming for Bioinformatics | BIOL 7200


Name: Joseph Luper Tsenum


Exercise 7


Question 14-21


List manipulation
14. Give an integer, n, return a list containing the first n numbers of the Fibonacci sequence.


#!/bin/env python3

num = int(input("give an integer input: "))
a = 0
b = 1
count = 0

	while count < num:
print (b)
c = a + b #assigning a new value to make swapping a & b easier
a = b
b = c
count += 1


15. Given two lists, return TRUE if the sums of each list are equal, else return FALSE.


#!/bin/env python3

a = [1,2,3,4,5]
b = [1,3,5,4,2]
c = sum(a)
d = sum(b)

	if c == d:
print ("true")
	else:
print("false")


16. Given a list of integers and two numeric inputs (A and B), return the sum and product of
the integers at positions A and B in the list.


#!/bin/env python3

a = [2,3,4,5,6,7,0]
b = [1,3,6,2,7,8,9]
A = int(input("chose an index position for list a"))
B = int(input("chose an index position for list b"))
x = a[A]
y = b[B]

	sum = y+x
	product = y*x
print("the sum of the values is: ", sum)
print("the product of the values is: ", product)


17. Given two lists of numbers, return a list containing the median number from each list
(Assume the lists will always be an odd length)
Dictionary manipulation


#!/bin/env python3

import statistics
a = [1,2,3,4,5]
b = [1,2,3,4,5]
x = statistics.median(a)
y = statistics.median(b)

print("The median of list a and b is: ", x,"and", y)


18. Given an integer, n, write a program that generates a dictionary that contains as keys the
1:n and values equal to n*n. For example:
Input: 4
Output: {1:1, 2:4, 3:9, 4:16}
Multiple dimensions
Create a 3 x 5 matrix of numbers (of your choice) to use for these exercises.


#!/bin/env python3
n=int(input("Input a number "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d) 


19. Write a program that computes the mean of each column and the mean of means


#!/bin/env python3

a = [[1,2,3,4,5],
[6,7,8,9,0],
[2,4,6,8,7]]
total = 0
	for i in zip(*a):
print(sum(i)/len(i))
total = total +sum(i)/len(i)

print ("The total mean is:", (total/5))


20. Write a program that computes that pairwise difference and returns the average difference.
For example: if position (1,1)=10 and (1,2)=7, the pairwise distance is 3.


#!/usr/bin/env python3

a = [[1,2,3,4,5],
[6,7,8,9,0],
[2,4,6,8,7]]
total = 0

for i in range(3):
for j in range(5):
for x in range(3):
for y in range(5):
	value = a[i][j]
	difference = value - a[x][y]
	total += difference
	average = total/15
print("The average pairwise difference is:", average)


21. Write a program that reverses the order of numbers in each row

#!/bin/env python3

a = [[1,2,3,4,5],
[6,7,8,9,0],
[2,4,6,8,7]]
print(a)

	for i in range(3):
		start = 0
		end = 4
	while start < end:
a[i][start], a[i][end] = a[i][end], a[i][start]
start += 1
end -= 1



