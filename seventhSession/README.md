# CLASS


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


- `__lt__(self, other)`

- `__le__(self, other)`

- `__eq__(self, other)`

- `__ne__(self, other)`

- `__gt__(self, other)`

- `__ge__(self, other)`
