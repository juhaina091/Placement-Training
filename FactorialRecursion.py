'''Write a program to find the factorial of a number using recursion.

Input Format

Read a number n from the console

Constraints

NA

Output Format

Print the factorial of the number n

Sample Input 0

6
Sample Output 0

720
Sample Input 1

9
Sample Output 1

362880'''
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n=int(input())
print(fact(n))
