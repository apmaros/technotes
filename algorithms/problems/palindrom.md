# Palindrom

## Valid Palindrom
**Decsription**

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

**Solution**

Two pointer problem. Use pointer for the beginning and the end of the string.

```Python
def is_palindrome(self, s: str) -> bool:
    i = 0
    j = len(s) - 1
    
    while i < j:
        si = s[i]
        sj = s[j]

        if not si.isalpha() and (not si.isnumeric()):
            i += 1
            continue
        if not sj.isalpha() and (not sj.isnumeric()):
            j -= 1
            continue
        
        if si.lower() == sj.lower():
            i += 1
            j -= 1
        else:
            return False
    
    return True
```

## Palindrome Permutation
Given a string `s`, return `true` if a permutation of the string could form a palindrome.

```python
freq = set()

for ch in list(s):
    if ch not in freq:
        freq.add(ch)
    else:
        freq.remove(ch)
    
return len(freq) < 2
```