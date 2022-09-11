# Lecture 09: Exception Handling


## Motivation

Our code can, and will, run into errors. Sometimes this is a consequence of incorrect coding, some times of improper input data, sometimes of some malfunction of the underlying infrastructure. Programming languages offer tools to handle these exceptions and to transfer control to another component of the codebase. Even basic solutions need to handle errors, so exception handling is also a part of the basic tools for a data scientist or analyst. 


## This lecture

We introduce `try` and `except`, and offer a few simple examples on how to '_catch_' these errors. By identifying exception types we show how to be selective on the treatment of the various types of errors. 


## Learning outcomes 

After completing [exception_handling.ipynb](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture09-exception-handling/exception_handling.ipynb) students should be able to :

- Test code chunks for potential errors
- Control how to handle these exceptions
- Identify exception (aka error) types
- Selecting actions based on the types of the exception occurred 


## Datasets used

None. 


## Lecture time

Ideal overall time: **10 mins**. 


## Homework

Define the following function:

```python
def divide(a, b):

    return a / b
```

The user needs to add both `a` and `b` as user input using the `input()` function.

```python
a = input()
b = input()
```

Define a complex `try` - `except` block which handles all false user input which otherwise crash the function. Make sure your code sends different instructions to the user depending on the nature of the error:

- when division with zero
- when using strings instead of numbers
- in case of other false input. 

