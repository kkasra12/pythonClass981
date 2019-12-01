# second Session

# if - elif - else

the overall syntax is:
```python
if <condition0>:
    # some code goes here using proper indentation
elif <condition1>:
    # some other code goes here
    # these codes will execute if ( ~condition0 & condition1 )
elif <condition2>:
    # some other code goes here
    # these codes will execute if ( ~condition0 & ~condition1 & condition2 )
else:
    # some other code goes here
    # these codes will execute if all conditions was not true
```

## forLoop

overall syntax is
```python
for <var> in <iterable>:
    loop-body
# for example:
for i in [1,2,3,4]:
    print(2*i)
```
OUTPUT:
```1
2
3
4
```
### question: print 0 to 100 ???
```python
for i in range(0,100):
    print(i)
```

### question: print Fibonacci
ask a user for a number and print Fibonacci series up to that number
Fibonacci series is:
>  a[n]=a[n-1]+a[n-2]
>
>  1,1,2,3,5,8,13,...

```python
n=int(input())
fib=[1,1]
for i in range(2,n):
    fib=fib+[fib[i-1]+fib[i-2]]
    print(fib[i],end=" ")
print()
```

## break - continue - for else
think of a given list as `lst` print 1/x for each x in lst if x!=0 and ignore all members after a `None` member

> what is None?
>
> None is a data that points to nothing :)

``python
lst=[1,3,4,6,8,0,None,4,5,5,3]
ans=[]
for i in lst:
    if i==0:
        continue
    if i==None:
        break
    ans.append(1/i)
else:
    print("this list has no None items")
print(ans)
```

## while - loop

### question: ask for numbers from users and sum them up until user types STOP

```python
sum=0
while True:
    n=input()
    if n=="STOP":
        break
    sum+=int(n)
print(sum)
```

### question: ask a number from user and write the each in seperate line
> idea
>
> 256=25*10+6
>
> 25=2*10+5
>
> 2=0*10+2

```python
lst=[]
n=int(input())
while n>0:
    lst.append(n%10)
    n//=10.
print(lst[::-1])
```

OR

```python
n=input()
for i in n:
 print(i)
```

LATER you can say:

```python
print("\n".join([i for i in input()]))
```

## Dictionary

dictionaries contains a ***key*** and a ***value***
> TIP: ***key*** must be **hashable**
the most usable function of the dictianries is update:

look at this cammands executed in REPL
```python
>>> numbers={1:"one",2:"two",3:"three"}
>>> print(numbers[1])
one
>>> print(numbers[1])[1P])3])
three
>>> details={"name":"kasra","age":22,"[K"height":1.8,200:500}
>>> details['name']
'kasra'
>>> details.get("name")
'kasra'
>>> details.get("namee")
>>> details.items()
dict_items([('name', 'kasra'), ('age', 22), ('height', 1.8), (200, 500)])
>>> details.pop("name")
'kasra'
>>> details
{'age': 22, 'height': 1.8, 200: 500}
>>> details.setdefault('age',0)
22
>>> details
{'age': 22, 'height': 1.8, 200: 500}
>>> details.setdefault('age',0)
22
>>> details.setdefault('name','kasraaaaaa')
'kasraaaaaa'
>>> details
{'age': 22, 'height': 1.8, 200: 500, 'name': 'kasraaaaaa'}
>>> details.update({"name":"kasra","test":"testVal"})

>>> details
{'age': 22, 'height': 1.8, 200: 500, 'name': 'kasra', 'test': 'testVal'}
```
