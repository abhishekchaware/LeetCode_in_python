'''
Docstring for Leetcode.Container_With_Most_Water_11

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) 
and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
'''
height = [1,8,6,2,5,4,8,3,7]

def maxArea(height: list[int]) -> int:
    lenn =len(height)
    maxsumm = 0
    l=0
    r=lenn-1
    while l < r:
        diff = r-l
        mn = min(height[l],height[r])
        summ = mn * diff
        maxsumm = max(summ,maxsumm)
        
        if mn ==height[l]:
            l +=1
        else:
            r -=1
    return maxsumm

print(maxArea(height))