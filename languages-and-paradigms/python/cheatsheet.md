# Cheat Sheet

All the interesting things you can do with Python

## Get a hash value of a string

```Python
import hashlib
s = 'foo'
r = hashlib.md5(s.encode('utf8')).digest()[0]
```

## String methods

### Find

Return the lowest index in the string where substring sub is found within the slice `s[start:end]`.

```Python
"foobarbaz".find("bar")
```

### Is Alpha-Numeric

Return True if all characters in the string are alphanumeric and there is at least one character

```Python
'1a'.isalnum()
#> True
'$£'.isalnum()
#> False
```

#### Is Alphabetical

Return True if all characters in the string are alphabetic and there is at least one character

```Python
'A'.isalpha()
#> True
'1'.isalpha()
#> False
```

#### Is Digit

```Python
'10'.isdigit()
#> True
'010'.isdigit()
#> True
'0f'.isdigit()
#> False
```

#### Lower

```Python
'FOO'.lower()
#> foo
```

#### Upper

```Python
'foo'.upper()
#> FOOO
```

#### Split

```Python
'1,2,3'.split(',')
#> ['1', '2', '3']
```

#### Join

```Python
",".join(["1", "2", "3"])
#> 1,2,3
```

## References

[1] String Methods - <https://docs.python.org/3/library/stdtypes.html#string-methods>