---
layout: post
title:  Data Types
date:   2024-09-01
categories: types
---

# Java Types

Java numbers have signed two's complements representation. Exception is int and long as they both also support unsigned integers (since Java SE 2).  

| Type    | Bits |
|:--------|:-----|
| byte    | 8    |
| short   | 16   |
| int     | 32   |
| long    | 64   |
| float   | 32   |
| double  | 64   |
| boolean | n/a  |
| char    | 16   |


# Binary Number

A binary number is a number expressed in a base-2 notation. Only `1` and `0` symbols are used to encode the number.

# Two's complement Number Representation

Two complement number representation is achieved by applying **NOT** operation (negating) a binary number. Most systems use Two's complement number representation as it allows to unify addition and subtraction. 

# Signed and Unsigned Numbers

Unsigned binary numbers are positive numbers. For example a 8-Bit unsigned number have range of 0 - 2^8-1 (255). Signed binary numbers require arithmetic sign. The most significant bit represent the sign bit. The rest of the numbers represent the value.


# References

- [1] Primitive Data Types (Java) - <https://docs.oracle.com/javase%2Ftutorial%2F/java/nutsandbolts/datatypes.html> - 2024-09-01
- [2] Binary Number - <https://en.wikipedia.org/wiki/Binary_number> - 2024-09-02
- [3] Two's Complement - <https://en.wikipedia.org/wiki/Two's_complement> - 2024-09-02
