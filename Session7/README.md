# Class (part1)


Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

**What is a class?**

Objects are an encapsulation of variables and functions into a single entity

```python
class human:
  name=None
```

## Instantiating
```python
class human:
  name=None

person0=human()
person0.name='kasra'
```
## Adding Functions:
```Python
class human:
  name=None
  def sayHello(self):
    print(f"hello ma friend :)\nMy name is {self.name} I am very polit \U0001F60C\n")

person0=human()
person0.name='kasra'
person0.sayHello()
```

## \_\_init__ function
```Python
class human:
  name=None
  def __init__(self):
    print("i am new born!!")
  def sayHello(self):
    print(f"hello ma friend :)\nMy name is {self.name} I am very polit \U0001F60C\n")

person0=human()
print("name changed!")
person0.name='kasra'
person0.sayHello()
```

**Question:** write a function to change the `name`

**init function can have arguments...**

```Python
class human:
  name=None
  def __init__(self,name):
    print("i am new born!!")
    self.name=name
  def sayHello(self):
    print(f"hello ma friend :)\nMy name is {self.name} I am very polit \U0001F60C\n")

person0=human('kasra')
person0.sayHello()
```

**Try to make several objects from one function and see the variables namespace**

**Question:** Create a class, in which it has this functionallities:
- this class can be Instantiate by a list
- make a method , whenever the method is called it should return next object

**Question** think a pile of numbers that we should check whether they are in the Fibonacci series or not.(**fisrt** most of numbers are duplicated, **second** make it *fast*)

## Magic Functions or Dunder Functions

[docs for special functions](https://docs.python.org/3/reference/datamodel.html#special-method-names)

- `__lt__(self, other)`

- `__le__(self, other)`

- `__eq__(self, other)`

- `__ne__(self, other)`

- `__gt__(self, other)`

- `__ge__(self, other)`

****


- `__getitem__(self, key)`

- `__setitem__(self, key, value)`

- `__contains__(self, item)`

****

- `__add__(self, other)`  ==> `+`

- `__sub__(self, other)` ==> `-`

- `__mul__(self, other)` ==> `*`

- `__matmul__(self, other)` ==> `@ `

> [ptyhonDoc](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations) says `The @ (at) operator is intended to be used for matrix multiplication. No builtin Python types implement this operator.`

- `__truediv__(self, other)` ==> `/`

- `__floordiv__(self, other)` ==> `//`

- `__mod__(self, other)` ==> `%`

- `__pow__(self, other[, modulo])` ==> `**`

- `__lshift__(self, other)` ==> `<<`

- `__rshift__(self, other)` ==> `>>`

- `__and__(self, other)` ==> `&`

- `__xor__(self, other)¶` ==> `^`

- `__or__(self, other)` ==> `|`

- `__radd__(self, other)`
- `__rsub__(self, other)`
- `__rmul__(self, other)`
- `__rmatmul__(self, other)`
- `__rtruediv__(self, other)`
- `__rfloordiv__(self, other)`
- `__rmod__(self, other)`
- `__rpow__(self, other)`
- `__rlshift__(self, other)`
- `__rrshift__(self, other)`
- `__rand__(self, other)`
- `__rxor__(self, other)`
- `__ror__(self, other)¶`

- `__iadd__(self, other)` ==> `+=`
- `__isub__(self, other)` ==> `-=`
- `__imul__(self, other)` ==> `*= `
- `__imatmul__(self, other)` ==> `@=`
- `__itruediv__(self, other)` ==> `/=`
- `__ifloordiv__(self, other)` ==> `//=`
- `__imod__(self, other)` ==> `%=`
- `__ipow__(self, other[, modulo])` ==> `**=`
- `__ilshift__(self, other)` ==> `<<=`
- `__irshift__(self, other)` ==> `>>=`
- `__iand__(self, other)` ==> `&=`
- `__ixor__(self, other)` ==> `^=`
- `__ior__(self, other)` ==> `|=`

****

- `__str__(self)`

- `__len__(self)`
