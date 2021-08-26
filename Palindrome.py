"""
The task you have to perform is “The Next Palindrome.” This task consists of a total of 15 points to evaluate your performance.

Problem Statement:-
A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:

676, 616, mom, 100001.

You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number.
Your first input should be the number of test cases and then take all the cases as input from the user.



Input:
3

451

10

2133

Output:
Next palindrome for 451 is 454

Next palindrome for 10 is 11

Next palindrome for 2311 is 2222
"""

try:
    tc = int(input("Enter the number of test cases you want:- "))
    for i in range(tc):
        n = int(input("Enter the number:- "))
        while True:
            n = n + 1
            t = str(n)
            if t == t[::-1]:
                print(f"The next palindrome for is {t}")
                break
            else:
                continue

except Exception as f:
    print(f"{f} Please try to input numbers not alphabet")