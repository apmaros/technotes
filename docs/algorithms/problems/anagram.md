# Anagram

**Definition**

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Solution**

```python
def is_anagram(self, s: str, t: str) -> bool:        
    freq = {}

    for c in s:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1
    
    for c in t:
        if c not in freq:
            return False
        else:
            freq[c] -= 1
        
        if freq[c] == 0:
            freq.pop(c)
    
    return not freq
```