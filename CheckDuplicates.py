'''Given an integer array nums, print "true" if any value appears at least twice in the array, and print "false" if every element is distinct.

Read n, the number of values in the first line, followed by the n numbers in the next line.

Input Format

4 1 2 3 1

Constraints

NA

Output Format

true

Sample Input 0

4
1 2 3 1
Sample Output 0

true
Sample Input 1

4
1 2 3 4
Sample Output 1

false'''
n=int(input())
arr=input().split()
if len(arr)==len(set(arr)):
    print('false')
else:
    print('true')
