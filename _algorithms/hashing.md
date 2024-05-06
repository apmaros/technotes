---
layout: post
title:  "Hashing"
date:   2024-05-06
categories: algo
tags: hash
---

- What is Hash and how it differs from an array
- Hashing function
    - how it works
    - what makes a good hashing function
- Implement Hash and describe its API

## Hash Function
A function that deterministically converts a input into integer that is smaller than a constant predefined size.

## Hash Map

An un-orderd collection of key value pairs. With operations of adding, removing and lookup are 0(n).

## Disadvantages

**Size** - Hash maps are larger than arrays because they need to allocate an array for each key due to collisions.

**Speed** - Calculating hash function can make hash map make less efficient than array for small collections.

## Collisions

A hash map has a finite number of fields in the array where values can be stored. The number is defined by the largest integer that hash function can convert input to. A collision occurs when different inputs convert to the same integer. This is possible due to limited number of fields in the array where the value can be store. The smaller number, the higher chance of collision is.

Unhandled collisions would lead to data loss, where a string would convert to the same integer as another string and would overwrite existing value. One way of addressing collisions is using method called **chaining**.

### Chaining

Hash function determines a filed in an array where the value is to be stored. Instead of storing the value directly, the value is appended to a linked list. This mean that each field in the array can contain multiple values. Upon access, or update of the value, first the hash function determines the array field where the value is stored. Then, the linked list is traversed to find the specific value.

It is important part of every hash map to minimize collisions as they are slowing down the read and write to hash map.

{% highlight python %}
# Set
empty = {}
basket = {'apple', 'orange'}

## Membership Testing
'orange' in basket
# >>> True
'potato' in basket
# >>> False

shopping_list = ['apple', 'butter', 'coffee']

# comprehension
to_buy = {x for x in shopping_list if x not in basket}
# >> {'coffee', 'butter'}
{% endhighlight %}
