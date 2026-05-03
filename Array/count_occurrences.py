"""
Problem Statement:

You are given two lists of integers:
N = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
M = [10, 111, 1, 4, 5, 67, 2]

For each element in list M, determine how many times it appears in list N.

Your task is to return the result as a dictionary where:
- Keys are elements from list M
- Values are the count of occurrences of those elements in list N

Example:
10 appears 1 time in N → 10: 1  
111 appears 0 times in N → 111: 0  
1 appears 1 time in N → 1: 1  

Final Output:
{10: 1, 111: 0, 1: 1, 4: 0, 5: 4, 67: 0, 2: 2}

Constraints:
1 ≤ len(N), len(M) ≤ 10^8  
1 ≤ N[i], M[i] ≤ 10

Note:
- The solution should be efficient for large inputs.
"""

N = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
M = [10, 111, 1, 4, 5, 67, 2]
