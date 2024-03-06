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

# Sliding Window

A sliding window is a bubset of 2 pointers problem. By a window we can understand a subarray with a left pointer at the start and a right pointer at the end of the window. Typically, it is used in problems with a validation criteria for a subarray with some metrics, e.g. sum, unique elements, frequency.

For example, a subarray is valid when it has a sum less or equal to 5. Find longest valid subarray.

{% highlight python %}
def sliding_window(nums, target):
    left = curr_sum = max_len = 0

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum > target:
            left += 1
            curr_sum -= nums[left]

        max_len = max(max_len, right - left + 1)

    return max_len
{% endhighlight %}
