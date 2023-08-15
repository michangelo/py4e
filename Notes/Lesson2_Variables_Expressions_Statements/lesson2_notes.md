# Lesson 2: Variables, Expressions, and Statements

## Values and Types

<https://www.youtube.com/watch?v=7KHdV6FSpo8>

A **value** is one of the basic things a program works with, like a letter or a number. The values we have seen so far are 1, 2, and "Hello, World!"

These values belong to different **types**: 2 is an integer, and "Hello, World!" is a string, so called because it contains a "string" of letters. You (and the interpreter) can identify strings because they are enclosed in quotation marks.

The `print` statement also works for integers. We use the `python` command to start the interpreter.

``` py
python
>>> print(4)
4
```

If you are not sure what type a value has, the interpreter can tell you.

```py
>>> type('Hello, World!')
<class 'str'>
>>> type(17)
<class 'int'>
```

Not surprisingly, strings belong to the type `str` and integers belong to the type `int`. Less obviously, numbers with a decimal point belong to a type called `float`, because these numbers are represented in a format called *floating* point.

``` py 
>>> type(3.2)
<class 'float'>
```

What about values like "17" and "3.2"? They look like numbers, but they are in quotation marks like strings.

``` py
>>> type('17')
<class 'str'>
>>> type('3.2')
<class 'str'>
```

They're strings.

When you type a large integer, you might be tempted to use commas between groups of three digits, as in 1,000,000. This is not a legal integer in Python, but it is legal:

``` py
>>> print(1,000,000)
1 0 0
```

Well, that's not what we expected at all! Python interprets 1,000,000 as a comma-separated sequence of integers, which it prints with spaces between.

This is the first example we have seen of a semantic error: the code runs without producing an error message, but it doesn't do the "right" thing.

## Variables

One of the most powerful features of a programming language is the ability to manipulate variables. A variable is a name that refers to a value.

An *assignment statement* creates new variables and gives them values:

``` py
>>> message = 'And now for something completely different'
>>> n = 17
>>> pi = 3.1415926535897931
```

This example makes three assignments. The first assigns a string to a new variable named `message`; the second assigns the integer 17 to n; the third assigns the (approximate) value of $\pi$ to `pi`.

To display the value of a variable, you can use a print statement:

``` py
>>> print(n)
17
>>> print(pi)
3.141592653589793
```

The type of a variable is the type of the value it refers to.

``` py
>>> type(message)
<class 'str'>
>>> type(n)
<class 'int'>
>>> type(pi)
<class 'float'>
```

## Variable Names and Keywords

Programmers generally choose names for their variables that are meaningful and document what the variable is used for.

Variable names can be arbitrarily long. They can contain both letters and numbers, but they cannot start with a number. It is legal to use uppercase letters, but it is a good idea to begin variable names with a lowercase letter (you'll see why later).

The underscore character ( _ ) can appear in a name. It is often used in names with multiple words, such as `my_name` or `airspeed_of_unladen_swallow`. Variable names can start with an underscore character, but we generally avoid doing this unless we are writing library code for others to use.

If you give a variable an illegal name, you get a syntax error:

``` py
>>> 76trombones = 'big parade'
SyntaxError: invalid syntax
>>> more@ = 1000000
SyntaxError: invalid syntax
>>> class = 'Advanced Theoretical Zymurgy'
SyntaxError: invalid syntax
```

`76trombones` is illegal because it begins with a number. `more@` is illegal because it contains an illegal character, @. But what's wrong with `class`?

It turns out that `class` is one of Python's *keywords*. The interpreter uses keywords to recognize the structure of the program, and they cannot be used as variable names.

Python reserves 35 keywords:

``` py
and     continue  finally  is        raise
as      def       for      lambda    return
assert  del       from     None      True
async   elif      global   nonlocal  try
await   else      if       not       while
break   except    import   or        with
class   False     in       pass      yield
```

You might want to keep this list handy. If the interpreter complains about one of your variable names and you don't know why, see if it is on this list.

## Statements

A *statement* is a unit of code that the Python interpreter can execute. We have seen two kinds of statements: print being an expression statement and assignment.

When you type a statement in interactive mode, the interpreter executes it and displays the result, if there is one.

A script usually contains a sequence of statements. If there is more than one statement, the results appear one at a time as the statements execute.

For example, the script

``` py
print(1)
x = 2
print(x)
```

produces the output

``` py
1
2
```

The assignment statement produces no output.

## Operators and Operands

**Operators** are special symbols that represent computations like addition and multiplication. The values the operator is applied to are called *operands*.

The operators `+` `-` `*` `/`, and `**` perform addition, subtraction, multiplication, division, and exponentiation, as in the following examples:

``` py
20+32
hour-1
hour*60+minute
minute/60
5**2
(5+9)*(15-7)
```

There has been a change in the division operator between Python 2.x and Python 3.x. In Python 3.x, the result of this division is a floating point result:

``` py
>>> minute = 59
>>> minute/60
0.9833333333333333
```

The division operator in Python 2.0 would divide two integers and truncate the result to an integer:

``` py
>>> minute = 59
>>> minute/60
0
```

To obtain the same answer in Python 3.0 use floored `//` integer division. 

``` py
>>> minute = 59
>>> minute//60
0
```

In Python 3.0 integer division functions much more as you would expect if you entered the expression on a calculator.

## Expressions

Video: Variables, Expressions and Statements - Part 2

<https://www.youtube.com/watch?v=kefrGMAglGs>

An *expression* is a combination of values, variables, and operators. A value all by itself is considered an expression, and so is a variable, so the following are all legal expressions (assuming that the variable `x` has been assigned a value):

``` py
17
x
x + 17
```

If you type an expression in interactive mode, the interpreter evaluates it and displays the result:

``` py
>>> 1 + 1
2
```

But in a script, an expression all by itself doesn't do anything! This is a common source of confusion for beginners.

## Exercise 1

Type the following statements in the Python interpreter to see what they do:

``` py
5
x = 5
x + 1
```

## Order of Operations

When more than one operator appears in an expression, the order of evaluation depends on the *rules of precedence*. For mathematical operators, Python follows mathematical convention. The acronym *PEMDAS* is a useful way to remember the rules:

- *Parentheses* have the highest precedence and can be used to force an expression to evaluate in the order you want. Since expressions in parentheses are evaluated first, `2 * (3-1)` is 4, and `(1+1)**(5-2)` is 8. You can also use parentheses to make an expression easier to read, as in `(minute * 100) / 60`, even if it doesn't change the result.

- *Exponentiation* has the next highest precedence, so `2**1+1` is 3, not 4, and `3*1**3` is 3, not 27.

- *Multiplication and Division* have the same precedence, which is higher than Addition and Subtraction, which also have the same precedence. So `2*3-1` is 5, not 4, and `6+4/2` is 8, not 5.

- *Operators* with the same precedence are evaluated from left to right. So the expression `5-3-1` is 1, not 3, because the `5-3` happens first and then `1` is subtracted from 2.

When in doubt, always put parentheses in your expressions to make sure the computations are performed in the order you intend.

## The Modulus Operator

The *modulus operator* works on integers and yields the remainder when the first operand is divided by the second. In Python, the modulus operator is a percent sign (`%`). The syntax is the same as for other operators:

``` py
>>> quotient = 7 // 3
>>> print(quotient)
2
>>> remainder = 7 % 3
>>> print(remainder)
1
```

So 7 divided by 3 is 2 with 1 left over.

The modulus operator turns out to be surprisingly useful. For example, you can check whether one number is divisible by another: if `x % y` is zero, then `x` is divisible by `y`.

You can also extract the right-most digit or digits from a number. For example, `x % 10` yields the right-most digit of `x` (in base 10). Similarly, `x % 100` yields the last two digits.

## String Operations 

The `+` operator works with strings, but it is not addition in the mathematical sense. Instead it performs *concatenation*, which means joining the strings by linking them end to end. For example:

``` py
>>> first = 10
>>> second = 15
>>> print(first+second)
25
>>> first = '100'
>>> second = '150'
>>> print(first + second)
100150
```

The `*` operator also works with strings by multiplying the content of a string by an integer. For example:

``` py 
>>> first = 'Test '
>>> second = 3
>>> print(first * second)
Test Test Test
```

## Asking the User for Input

Sometimes we would like to take the value for a variable from the user via their keyboard. Python provides a built-in function called `input` that gets input from the keyboard^[In Python 2.0, this function was named `raw_input`.]. When this function is called, the program stops and waits for the user to type something. When the user presses `Return` or `Enter`, the program resumes and `input` returns what the user typed as a string.

``` py
>>> inp = input()
Some silly stuff
>>> print(inp)
Some silly stuff
```

Before getting input from the user, it is a good idea to print a prompt telling the user what to input. You can pass a string to `input` to be displayed to the user before pausing for input:

``` py
>>> name = input('What is your name?\n')
What is your name?
Chuck
>>> print(name)
Chuck
```

The sequence \n at the end of the prompt represents a *newline*, which is a special character that causes a line break. That's why the user's input appears below the prompt.

If you expect the user to type an integer, you can try to convert the return value to `int` using the `int()` function:

``` py
>>> prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
>>> speed = input(prompt)
What...is the airspeed velocity of an unladen swallow?
17
>>> int(speed)
17
>>> int(speed) + 5
22
```

But if the user types something other than a string of digits, you get an error:

``` py
>>> speed = input(prompt)
What...is the airspeed velocity of an unladen swallow?
What do you mean, an African or a European swallow?
>>> int(speed)
ValueError: invalid literal for int() with base 10:
```

We will see how to handle this kind of error later.

## Comments

As programs get bigger and more complicated, they get more difficult to read. Formal languages are dense, and it is often difficult to look at a piece of code and figure out what it is doing, or why.

For this reason, it is a good idea to add notes to your programs to explain in natural language what the program is doing. These notes are called *comments*, and in Python they start with the `#` symbol:

``` py
# compute the percentage of the hour that has elapsed
percentage = (minute * 100) / 60
```

In this case, the comment appears on a line by itself. You can also put comments at the end of a line:

``` py 
percentage = (minute * 100) / 60     # percentage of an hour
```

Everything from the `#` to the end of the line is ignored; it has no effect on the program.

Comments are most useful when they document non-obvious features of the code. It is reasonable to assume that the reader can figure out *what* the code does; it is much more useful to explain *why*.

This comment is redundant with the code and useless:

``` py
v = 5     # assign 5 to v
```

This comment contains useful information that is not in the code:

``` py
v = 5     # velocity in meters/second.
```

Good variable names can reduce the need for comments, but long names can make complex expressions hard to read, so there is a trade-off.

## Choosing Mnemonic Variable Names

As long as you follow the simple rules of variable naming, and avoid reserved words, you have a lot of choice when you name your variables. In the beginning, this choice can be confusing both when you read a program and when you write your own programs. For example, the following three programs are identical in terms of what they accomplish, but very different when you read them and try to understand them.

``` py 
a = 35.0
b = 12.50
c = a * b
print(c)
```

``` py
hours = 35.0
rate = 12.50
pay = hours * rate
print(pay)
```

``` py
x1q3z9ahd = 35.0
x1q3z9afd = 12.50
x1q3p9afd = x1q3z9ahd * x1q3z9afd
print(x1q3p9afd)
```

The Python interpreter sees all three of these programs as *exactly the same* but humans see and understand these programs quite differently. Humans will most quickly understand the intent of the second program because the programmer has chosen variable names that reflect their intent regarding what data will be stored in each variable.

We call these wisely chosen variable names "mnemonic variable names". The word mnemonic^[See https://en.wikipedia.org/wiki/Mnemonic for an extended description of the word "mnemonic".] means "memory aid". We choose mnemonic variable names to help us remember why we created the variable in the first place.

While this all sounds great, and it is a very good idea to use mnemonic variable names, mnemonic variable names can get in the way of a beginning programmer's ability to parse and understand code. This is because beginning programmers have not yet memorized the reserved words (there are only 35 of them) and sometimes variables with names that are too descriptive start to look like part of the language and not just well-chosen variable names.

Take a quick look at the following Python sample code which loops through some data. We will cover loops soon, but for now try to just puzzle through what this means:

``` py
for word in words:
    print(word)
```

What is happening here? Which of the tokens (for, word, in, etc.) are reserved words and which are just variable names? Does Python understand at a fundamental level the notion of words? Beginning programmers have trouble separating what parts of the code must be the same as this example and what parts of the code are simply choices made by the programmer.

The following code is equivalent to the above code:

``` py
for slice in pizza:
    print(slice)
```

It is easier for the beginning programmer to look at this code and know which parts are reserved words defined by Python and which parts are simply variable names chosen by the programmer. It is pretty clear that Python has no fundamental understanding of pizza and slices and the fact that a pizza consists of a set of one or more slices.

But if our program is truly about reading data and looking for words in the data, `pizza` and `slice` are very un-mnemonic variable names. Choosing them as variable names distracts from the meaning of the program.

After a pretty short period of time, you will know the most common reserved words and you will start to see the reserved words jumping out at you:

``` py
for word in words:
    print(word)
```

The parts of the code that are defined by Python (`for`, `in`, `print`, and `:`) are in bold and the programmer-chosen variables (`word` and `words`) are not in bold. Many text editors are aware of Python syntax and will color reserved words differently to give you clues to keep your variables and reserved words separate. After a while you will begin to read Python and quickly determine what is a variable and what is a reserved word.

## Debugging

At this point, the syntax error you are most likely to make is an illegal variable name, like `class` and `yield`, which are keywords, or `odd~job` and `US$`, which contain illegal characters.

If you put a space in a variable name, Python thinks it is two operands without an operator:

``` py
>>> bad name = 5
SyntaxError: invalid syntax
```

``` py
>>> month = 09
  File "<stdin>", line 1
    month = 09
             ^
SyntaxError: invalid token
```

For syntax errors, the error messages don't help much. The most common messages are `SyntaxError: invalid syntax` and `SyntaxError: invalid token`, neither of which is very informative.

The runtime error you are most likely to make is a "use before def;" that is, trying to use a variable before you have assigned a value. This can happen if you spell a variable name wrong:

``` py
>>> principal = 327.68
>>> interest = principle * rate
NameError: name 'principle' is not defined
```

Variables names are case sensitive, so `LaTeX` is not the same as latex.

At this point, the most likely cause of a semantic error is the order of operations. For example, to evaluate $1/2\pi$, you might be tempted to write

``` py
>>> 1.0 / 2.0 * pi
```

But the division happens first, so you would get $\pi / 2$, which is not the same thing! There is no way for Python to know what you meant to write, so in this case you don't get an error message; you just get the wrong answer.

## Glossary 

**assignment**: A statement that assigns a value to a variable.

**concatenate**: To join two operands end to end.

**comment**: Information in a program that is meant for other programmers (or anyone reading the source code) and has no effect on the execution of the program.

**evaluate**: To simplify an expression by performing the operations in order to yield a single value.

**expression**: A combination of variables, operators, and values that represents a single result value.

**floating point**: A type that represents numbers with fractional parts.

**integer**: A type that represents whole numbers.

**keyword**: A reserved word that is used by the compiler to parse a program; you cannot use keywords like if, def, and while as variable names.

**mnemonic**: A memory aid. We often give variables mnemonic names to help us remember what is stored in the variable.

**modulus operator**: An operator, denoted with a percent sign (%), that works on integers and yields the remainder when one number is divided by another.

**operand**: One of the values on which an operator operates.

**operator**: A special symbol that represents a simple computation like addition, multiplication, or string concatenation.

**rules of precedence**: The set of rules governing the order in which expressions involving multiple operators and operands are evaluated.

**statement**: A section of code that represents a command or action. So far, the statements we have seen are assignments and print expression statement.

**string**: A type that represents sequences of characters.

**type**: A category of values. The types we have seen so far are integers (type int), floating-point numbers (type float), and strings (type str).

**value**: One of the basic units of data, like a number or string, that a program manipulates.

**variable**: A name that refers to a value.

# Exercises

## [Graded Assignment] Exercise 2  
Accept and complete the assignment in the Github Classroom.Write a program that uses input to prompt a user for their name and then welcomes them.

``` py 
   """Returns a string greeting the input name from the prompt "enter your name".
    
    Parameters
    ----------
    none: a prompt is given asking for your name

    Returns
    -------
    Hello ___; followed by the name given at the input prompt
    """

    in_name = input("Enter your name: ")
    print("Hello ",name)

# exercise_2_2()
```

## [Graded Assignment] Exercise 3  
Accept and complete the assignment in the Github Classroom.Write a program to prompt the user for hours and rate per hour to compute gross pay.

``` py
    """ Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
    Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
    Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
    You should use input to read a string and float() to convert the string to a number. 
    Do not worry about error checking the user input - assume the user types numbers properly.
    
    Parameters
    ----------
    45, 10.50
    You should use input to read a string and float() to convert the string to a number.

    Returns
    -------
    498.75
    """

    hrs = float(input("Enter Hours: "))  
    rate = float(input("Enter Rate: "))

    if hrs <= 40.0:
        hrs = hrs 
        rate = rate 
    elif hrs > 40.0:
        hrs = hrs
        rate = rate * 1.5
    
    print(hrs*rate)
    
# exercise_3_1()
```

We won't worry about making sure our pay has exactly two digits after the decimal place for now. If you want, you can play with the built-in Python round function to properly round the resulting pay to two decimal places.

<https://www.youtube.com/watch?v=DVmspDooG2c>

## Exercise 4
Assume that we execute the following assignment statements:

``` py
width = 17
height = 12.0
```

For each of the following expressions, write the value of the expression and the type (of the value of the expression).

`width//2`
== 8 

`width/2.0` == 8.5

`height/3` == 4.0

`1 + 2 * 5` == 11

Use the Python interpreter to check your answers.

## Exercise 5
Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

```py 
def exercise_celsius_to_fahrenheit(): 
    # prompt user for celsius temperature
    var1 = float(input("Enter celsius temperature: "))

    # convert celsius to fahrenheit == celsius*(9/5) + 32 
    var2 = var1*(9/5)+32

    # print prompt with fahrenheit
    print("The temperature in Fahrenheit is: ",var2)

# exercise_celsius_to_fahrenheit()
```


