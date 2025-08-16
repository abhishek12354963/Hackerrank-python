'''You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Example
Set([1,3,4]) is a strict superset of set([1,3]).
Set([1,3,4]) is not a strict superset of set([1,3,4]).
Set([1,3,4]) is not a strict superset of set([1,3,5]).

Input Format

The first line contains the space separated elements of set A.
The second line contains integer n, the number of other sets.
The next n lines contains the space separated elements of the other sets.

Constraints

Output Format

Print True if set A is a strict superset of all other N sets. Otherwise, print False.

Sample Input 0

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
Sample Output 0

False
Explanation 0

Set A is the strict superset of the set([1,2,3,4,5]) but not of the set([100,11,12]) because 100 is not in set A.
Hence, the output is False.'''

#code

#method 1 
# Enter your code here. Read input from STDIN. Print output to STDOUT
A=set(map(int,input().split()))
n=int(input())
val=True
for _ in range(n):
    l1=set(map(int,input().split()))
    if len(l1.difference(A))==0:
        val=True
    else:
        val=False
        break
print(val)

#method 2# Check Strict Superset
A = set(map(int, input().split()))
n = int(input())
ok = True
for _ in range(n):
    S = set(map(int, input().split()))
    if not (A > S):      # strict superset
        ok = False
        # no break to consume all input if needed
print(ok)

#method 3 using issuperset(if not A.issuperset(S) is used)
A = set(map(int, input().split()))
n = int(input())
ok = True
for _ in range(n):
    S = set(map(int, input().split()))
    if not A.issuperset(S):   # check superset
        ok = False
print(ok)

#method 4 using intersection
A = set(map(int, input().split()))
n = int(input())
ok = True
for _ in range(n):
    S = set(map(int, input().split()))
    if A.intersection(S) != S:   # if all S elements not in A
        ok = False
print(ok)

#method 5 using difference
A = set(map(int, input().split()))
n = int(input())
ok = True
for _ in range(n):
    S = set(map(int, input().split()))
    if len(S.difference(A)) != 0:   # if S has elements outside A
        ok = False
print(ok)

