---
layout: post
title:  "Backtracking"
date:   2024-01-30
categories: backtracking
tags: backtracking
---
This is my solution of leetcode `39. Combination Sum`.

It follows general backtracking algorithm:

- add new candidate to list
- check for condition
- backtrack left candidate

{% highlight python %}

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def backtrack(remaining, starti, comb):
        # satisfy condition
        if remaining == 0:
            result.append(list(comb))
        # base case condition - must be within target
        if remaining < 0:
            return
        
        for i in range(starti, len(candidates)):
            # extend the combination
            candidate = candidates[i]
            comb.append(candidate)
            # check for sum
            backtrack(remaining - candidate, i, comb)
            # backtrack left item
            comb.pop()
    
    backtrack(target, 0, [])

    return result

{% endhighlight %}
