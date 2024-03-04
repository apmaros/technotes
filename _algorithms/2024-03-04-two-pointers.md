---
layout: post
title:  "Two Pointers"
date:   2024-03-04
categories: pointers
tags: array string
---


# Two pointers

Two-pointers is a common technique in solving string and array-related problems. It 
consists of 2 pointers. It can be low and high, where low (also can be left, or right)
is tracking the beginning of the array and high is tracking the end of the array. It has 
a condition that decides whether we move the low or the high pointer.

An example I enjoyed solving and demonstrating this problem is Leetcode problem [11. 
Container with most water](https://leetcode.
com/problems/container-with-most-water/description/).

{% highlight python %}
def maxArea(self, height: List[int]) -> int:        
    maxvol = 0
    l = 0
    r = len(height) - 1
    
    while l < r:
        area = r - l
        lh = height[l]
        rh = height[r]

        volume = area * (min(lh, rh))
        maxvol = max(volume, maxvol)

        if lh > rh:
            r -= 1
        else:
            l += 1
    
    return maxvol
{% endhighlight %}
