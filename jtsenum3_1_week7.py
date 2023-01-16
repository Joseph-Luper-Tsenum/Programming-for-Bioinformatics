Programming for Bioinformatics | BIOL 7200


Name: Joseph Luper Tsenum


Exercise 7


Question 1-13


1. Using a while loop, print whether a number is even or odd while counting from 0 to 49 by


#!/bin/env python3

a = 0
	while a < 50:
		if a % 2 == 0:
print ("the number is even.")
	else:
print ("the number is odd")
a += 3


2. Using a loop, print the first 10 numbers of the Fibonacci sequence (1, 1, 2, 3, 5, 8, 13, 21, 34,
55, ...)


#include<stdio.h>
int fibo(int num);
void main()
{
    int num,c=0,i;

    printf("Enter number: ");
    scanf("%d", &num);

    printf("Fibonacci Series:\n");

    for(i=1;i<=num;i++)
    {
        printf("%d\n", fibo(c));
        c++;
    }
}
int fibo(int num)
{
    if(num==0)
    {
        return 0;
    }

    else if(num==1)
    {
        return 1;
    }

    //fibonacci = 1 1 2 3 5 8
    // where n = (n-1) + (n-2)
    else
    {
        return (fibo(num-1)+fibo(num-2));
    }
}

#After entering 10 and running the command, it outputted the following Fibonacci sequence

0
1
1
2
3
5
8
13
21
34


3. Use a while loop to print the factorial of a number


#include <stdio.h>

int main()  
{  
    long int num, count = 1, fact = 1;  
  
    printf("Enter a number to find factorial\n");  
    scanf("%d", &num);  
  
    while(count <= num)  
    {  
        fact = fact * count; // fact *= count;  
        count++;  
    }  
  
    printf("Factorial of %d is %d\n", num, fact);  
  
    return 0;  
} 

#After entering 5 and executing the command, the factorial of 5 outputted 120


4. Find all the numbers between 2000 and 3000 that are divisible by 7 but not by 5

#!/bin/env python3


for i in range (2000,3001):
	if i % 7 == 0:
	if i % 5 != 0:
print (i)


5. Using a while loop and input(), check if an entered string matches “secretpassword”. Once
the match is found, exit the loop.


#!/bin/env python3

a = input("type a string that is 14 characters long: ")
i = str("secretpassword")
	while a == i:
print ("string matched")
break
	else:
print ("string does not match")


6. Write a loop that generates a triangle of text, i.e.
*
**
***
****
*****
****
***
**
*


#!/bin/env python3

#How many rows would you like the triangle to have?
x = int(input("what value would you like the peak of the triangle to be:"))
	for i in range(0,x): #tracks number of lines you have
	for j in range(0,i+1):
print("*",end = "")
print("\r")

	for a in range(x,0,-1):
	for b in range(0,a-1):
print("*",end ="")
print("\r")


7. Swapping values:
a. Create two numeric variables: a = 10 and b = 30
b. Swap their values by using a temporary variable
c. Swap their values without using any intermediate variable


#!/bin/env python3

a = 10
b = 30
#swaps with temp variable
temp = b
b = a
a = temp
print("a is now",a)
print("b is now",b)

#swapping without intermediate variable
a,b = b,a
print("a is now",a)
print("b is now",b)


8. Use input to take a series of numbers from the user (one number at a time); stop if the user
enters 0 and return the sum, average, maximum and minimum of the numbers received.


#!/bin/env python3

while num > a :
b.append(num)
num = int(input("input one integer value: "))

else:
	c = max(b) d = min(b) e = sum(b)
	avg = sum(b)/len(b)
print("The sum of the numbers entered is: " + str(e)) 
print("The maximum number entered is: " + str(c)) 
print("The minimum number entered is: " + str(d)) 
print("The average of the numbers entered is: " +str(avg))


Logic problems

9. Given two numeric values (say a and b), return their sum unless they are equal (i.e., a+b). If
they are equal, return their sum plus the square of the two numbers (i.e., a+b+a*a+b*b).


#!/bin/env python3

a = 5
b = 5
sum = a + b

if a == b:
	c = a**a
	d = b**b
	x = c + d + sum
print ("the square of the two number is plus the sum is:" + str(x))
	else:
print("The sum of the two numbers is: " + str(sum))


10. The police in your city aggressively ticket speeders, unless it happens to be their birthday.
There is an unofficial policy to subtract 5mph from your speed, which can be the difference
between a ticket and no ticket, on your birthday. Fines for speeding are small if within 1-15
mph over and large if > 15mph over. Return the expected fine (“none”, “small”, “large”)
depending on your speed and whether it is your birthday.


#!/bin/env python3

speed = int(input("What is the speed you the car is traveling at?"))
birthday = input("Is today your birthday? True/False")
speed_limit = int(input("What is the speed limit?"))

while birthday:
speed = speed - 5
speeding = speed_limit + 15 #if you're 1-15mph over case
	if speed == speed_limit:
print("none")
	elif speed in range(speed_limit,speeding):
print("small")
	elif speed > speeding:
print ("large")
	break
	else:
		speeding = speed_limit + 15 #if you're 1-15mph over case
		if speed == speed_limit:
print("none")
	elif speed in range(speed_limit,speeding):
print("small")
	elif speed > speeding:
print ("large")


String manipulation

11. Given two strings, one of length 4 (string1) and one of any length (string2), return string2 in
the middle of string1.
a. string1 = “****”
b. string2 = “Bold move, Cotton”
c. output: **Bold move, Cotton**

#!/bin/env python3

def insert_string2_middle(string1):
	return str[:2] + string1 + str[2:]

print(insert_string2_middle('[[]]', 'Python'))


12. Given a string of any length, return the first half of the string (For strings of odd length,
return the “half + 1” part of the string)


#!/bin/env python3

x = "absolutee"
y = len(x)
z = int(y/2)
	if y % 2 == 0:
print (x[0:z])
	else:
print(x[0:z+1])


13. Given a string and a logical value, return the reversed string if TRUE and return the string as
is if FALSE.

#!/bin/env python3

x = True
y = "abc"
z ="abc"[::-1]
	if x == True:
print(z)
	else:
print(y)



