# Lesson 6: Strings

We look at how Python stores and manipulates textual data using string variables and functions.

## A String is a Sequence

Video: Strings - Part 1

### <https://www.youtube.com/watch?v=dr98iM4app8>

A string is a *sequence* of characters. You can access the characters one at a time with the bracket operator. 

```py
fruit = 'banana'
letter = fruit[1]
```

The expression in brackets is called an *index*. The index indicates which character in the sequence you want (hence the name). 

But you might not get what you expect: 

```py
>>> print(letter)
a
```

For most people, the first letter of "banana" is "b", not "a". But in Python, the index is an offset from the beginning of the string, and the offset of the first letter is zero.

```py
>>> letter = fruit[0]
>>> print(letter)
b
```

So "b" is the 0th letter ("zero-th") of banana, "a" is the 1th letter ("one-th"), and "n" is the 2th ("two-th") letter. 

![Alt text](17100e28-string.png)
String Indexes 

You can use any expression, including variables and operators, as an index, but the value of the index has to be an integer. Otherwise you get:

```py
>>> letter = fruit[1.5]
TypeError: string indices must be integers
```

