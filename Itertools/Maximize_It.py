'''
You are given a function . You are also given  lists. The  list consists of  elements.

You have to pick one element from each list so that the value from the equation below is maximized:

%

 denotes the element picked from the  list . Find the maximized value  obtained.

 denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

Input Format

The first line contains  space separated integers K and M.
The next K lines each contains an integer Ni, denoting the number of elements in the ith list, followed by Ni space separated integers denoting the elements in the list.

Constraints





Output Format

Output a single integer denoting the value Smax .

Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
Sample Output

206
Explanation

Picking 5 from the 1st list, 9 from the 2nd list and 10 from the 3rd list gives the maximum S value equal to(5**2+9**2+10**2) %1000 = 206.'''

#code
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
lists=[list(map(int,input().split()))[1:] for _ in range(n)]
possible_sums={0}
for lst in lists:
    new_set=set()
    for num in lst:
        for s in possible_sums:
            new_set.add((s + num**2)%m)
    possible_sums=new_set

print(max(possible_sums))
