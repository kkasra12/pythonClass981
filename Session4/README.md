**QUESTION:** There is a list of points in Cartesian coordinates. Desired program should be able to count the number of rectangles that can be formed using those points. To simplify the question,a rectangle's edges are parallel with xor y coordinates. For instance:

**Input**
```
0,0
0,1
0,2
1,0
1,1
1,2
```
**output**
```
3
```
# Exception Handling

#### Some Common Exceptions
- **Exception** (this is what almost all the others are built off of)
- **AttributeError** - Raised when an attribute reference or assignment fails.
- **IOError** - Raised when an I/O operation (such as a `print` statement, the built-in `open()` function or a method of a file object) fails for an I/O-related reason, e.g.,
“*file not found*” or “*disk full*”.
- **ImportError** - Raised when an import statement fails to find the module definition or when a `from ... import` fails to find a name that is to be imported.
- **IndexError** - Raised when a sequence subscript is out of range.
- **KeyError** - Raised when a mapping (dictionary) key is not found in the set of existing keys.
- **KeyboardInterrupt** - Raised when the user hits the interrupt key (normally
Control-C or Delete).
- **NameError** - Raised when a local or global name is not found.
- **OSError** - Raised when a function returns a system-related error.
- **SyntaxError** - Raised when the parser encounters a syntax error
- **TypeError** - Raised when an operation or function is applied to an object of inappropriate type. The associated value is a string giving details about the type mismatch.
- **ValueError** - Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described by a more precise exception such as *IndexError*.
- **ZeroDivisionError** - Raised when the second argument of a division or modulo operation is zero.

#### try/except

```python
try:
  print(1/0)
except:
  print("Can not divide by zero :)")
```

*to be more specified...*

```python
try:
  print(1/0)
except ZeroDivisionError:
  print("Can not divide by zero :)")
```

**How to handle several exceptions?**

```python
numDicts={"zero":0,"one":1,
          'two':2,'three':3,
          'four':4,'five':5,
          'six':6,'seven':7,
          'eight':8,'nine':9}
try:
  num1,num2=input("please give me two numbers to divide them: ").split(" ")
  print(numDicts[num1]/numDicts[num2])
except ZeroDivisionError:
  print("Can not divide by zero :)")
except KeyError:
  print("I do not understand that number")
except:
  print("Oops!!! smth bad happened :[")
```

*or*

```python
numDicts={"zero":0,"one":1,
          'two':2,'three':3,
          'four':4,'five':5,
          'six':6,'seven':7,
          'eight':8,'nine':9}
try:
  num1,num2=input("please give me two numbers to divide them: ").split(" ")
  print(numDicts[num1]/numDicts[num2])
except (ZeroDivisionError, KeyError):
  print("Please recheck what you entered :|")
except:
  print("Oops!!! smth bad happened :[")
```

# Modules and Importing

```python
import math
print(math.sqrt(4))
print(math.cos(0))
print(math.pi)
```

**QUESTION:** How to find all functions in a module ?

#### Using from to import
```python
from math import sqrt
print(sqrt(4))
# print(math.sqrt(4))
# print(cos(60))
# print(math.cos(60))
# print(math.pi)
```

```python
from math import sqrt,cos
print(sqrt(4))
# print(math.sqrt(4))
print(cos(60))
# print(math.cos(60))
```

```python
from math import *
print(sqrt(4))
# print(math.sqrt(4))
print(cos(60))
# print(math.cos(60))
print(math.pi)
```

**How to change functions name?**

```python
import tkinter as tk
```

```python
from math import log as ln
print(ln(2.71828))
```

```python
from math import log as ln,e as EulerNumber
print(ln(EulerNumber))
```

*lets have some fun...*
```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>>
```

#### importing from non-global modules

Imagine there is a program which needs `func0` and `func1`. One simple architecture for this code can be like this:

```Python
# File name: run_me.py
def func0(a,b):
  pass

def func1():
  pass

input()
# your main code goes here
print()
```

*or* it is much **better** to use modules and `import`

```Python
# File name: utilities.py
def func0(a,b):
  pass

def func1():
  pass
```

```Python
# File name: run_me.py
from utilities import func0,func1
input()
# your main code goes here
print()
```

# if \_\_name__ == "\_\_main__":

think of the last example. It will be nice to have some test cases for `utilities.py`. Simply we can add some test lines at the end of `utilities.py`, but there is a problem.(!?)

To solve the problem, lets separate test cases which leads us to generate this file:
```Python
# File name: utilities_testCase.py
from utilities import func0,func1
print(func0("aTest","bTest"))
print(func0("aAnotherTest","bAnotherTest"))
print(func1("aTest","bTest"))
print(func1("aAnotherTest","bAnotherTest"))
```

**now lets make our environment more tidy by deleting `utilities_testCase.py`:**

```Python
# File name: utilities.py
def func0(a,b):
  pass

def func1():
  pass
if __name__ == '__main__':
  print(func0("aTest","bTest"))
  print(func0("aAnotherTest","bAnotherTest"))
  print(func1("aTest","bTest"))
  print(func1("aAnotherTest","bAnotherTest"))
```
*and also we have main file:*
```Python
# File name: run_me.py
from utilities import func0,func1
input()
# your main code goes here
print()
```

> NOTE: both files should be in the same folder.
