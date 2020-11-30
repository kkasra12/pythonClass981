# Unpacking lists

```python
>>> a,b=[1,3]
>>> a
1
>>> b
3
>>> print(a,b)
1 3
>>> a,b=[1,2,3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
>>> a,b,c=[1,2,3]
>>> print(a,b,c)
1 2 3
>>> a,*b=[1,2,3]
>>> print(a,b)
1 [2, 3]
>>> a,*b,c=[1,2,3,4,5,6]
>>> print(a,b,c)
1 [2, 3, 4, 5] 6
```

# defining functions

#### why we need to define new functions ?
1. Re-usability
2. Easier to understand
3. Recursive functions
4. Abstraction
5. Team work
6. Making iterators

```python
def <function_name>(<arguments>):
  #
  # function body
  #
  return <output>
```

**example:** Adder
```python
def adder(a,b):
  return a+b
```

**example:** XOR two lists
```python
def XOR(list0,list1):
  answer=[]
  for i,j in zip(list0,list1):
    answer.append(i^j)
  return answer
```

*or...*

```python
def XOR(list0,list1):
  return [i^j for i in zip(list0,list1)]
```

**example:** Absolute value
```python
def absoluteVal(x):
  if x<0:
    x*=-1
  return x
```

**example:** Fibonacci series

```python
def fib(n):
  if n==1 or n==2:
    return 1
  a=1
  b=1
  for i in range(n-2):
    b=a+b
    a=b-a
  return b
```
*or...*

```python
def fib(n):
  if n==1 or n==2:
    return 1
  a,b=1,1
  for i in range(n-2):
    a,b=b,a+b
  return b
```

# Variable scope

```python
def boo():
  m=3

def foo(n):
  m=1
  boo()
  print(n,m)
  n=10

m=2
n=0
foo(3)
print(n,m)
```

# Passing arguments

#### Define a default value for a specific variable
```python
def log(num,base=10):
  UPBOUND=1**5
  sum0=0
  k=1
  xn=num-1
  for i in range(1,UPBOUND):
    sum0+=k*xn/i
    k*=-1
    xn*=(num-1)
  sum1=0
  k=1
  xn=base-1
  for i in range(1,UPBOUND):
    sum1+=k*nx/i
    k*=-1
    xn*=base-1
  return sum0/sum1


print(log(20))
print(log(100))
print(log(64,2))
print(log(729,base=2))
```
#### Passing multiple arguments as a list

```python
def f(*numbers):
  k=1
  s=0
  for i in numbers:
    s+=k*i
    k*=-1
  return s


print(f(1,2,3)) # 1-2+3 = 2
print(f(4,5,8,9,10,4)) # 4-5+8-9+10-4 = 4
print(f(8,3,2)) # 8-3+2 = 7
```

**using asterisks while calling function**

```python
def curveGenerator(a,b,c,xStart,xEnd,step):
  ''' returns a list containing f(x) values which starts from xStart and end until xEnd
  WHERE:
    f(x) = ax^2+bx+c
  '''
  ans=[]
  x=xStart
  while x<=xEnd: # Line A
    ans.append(a*x**2+b*x+c)
    x+=step
  return ans

print(curveGenerator(*[1,0,0,-2,2,0.01]))
```
**QUESTION**:  why `for i in range(xStart,xEnd,step)` is not used instead of line A ???

#### Passing multiple arguments as a dictionary

```python
def add_to_db(**details):
  print(details)
  # do other stuffs

add_to_db(name='kasra',age=22,degree='Bachelor')
```

# Recursive functions

**example:** power

```python
def pow(base,power):
  if power==1:
    return base
  return base*pow(base,power-1)
```

**example:** again Fibonacci
```python
def fib(n):
  if n<=2:
    return 1
  return fib(n-1)+fib(n-2)
```

*or...*

```python
def fib(n):
    return ([1,1]+[fib(i) for i in range(2,n)]+[fib(n-1)+fib(n-2) for _ in [1] if n>=2])[n]
```

*or lets make it faster...*

```python
def fib(n,series=[1,1]):
  if len(series)>=n:
    return series
  series=fib(n-1,series)
  series.append(series[-1]+series[-2])
  return series
```
