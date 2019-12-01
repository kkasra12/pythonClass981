## First question

there is some numbers in first line
these numbers might be angles of a polygon
The question is to write a code to determine wheather those angles can form a polygon or not.

#### input0
> 90 45 45

#### output0
> YES

#### input1
> 90 80 100 90

#### output1
> YES

#### input2
> 90 80 80 70

#### output2
> NO

**TIP**: You can split input value using `str.split()` function
```python
>>> a='kasra eskandari test tmp'
>>> splitedVal=a.split(' ')
>>> print(splitedVal)
['kasra', 'eskandari', 'test', 'tmp']
```

**TIP**: The sum of a angles in a polygon is `180(n-2)`

## Second question

get an integer number `n` from user and draw two diamond with a diameter of `n` using astricks (or whatever character you like).

#### input0
> 5

#### output0
```
  *    *
 ***  ***
**********
 ***  ***
  *    *
```

## Third question

ask the user for a sentence and count the occurrence of each character.
print each character in seperate line and leave a single space between character and the number

#### input0
> hello my name is kasra

#### output0
```
h 1
e 2
l 2
o 1
  4
m 2
y 1
n 1
a 3
i 1
s 2
k 1
r 1
```
**TIP**: use logical `in` operator to check if a key is available in dictionary or not.
```python
>>> d={'a':0, 'b':2, 'f':65}
>>> if 'a' in d:
...     print("YES")
...
YES
>>> if 'c' in d:
...     print("YES")
... else:
...     print("NO")
...
NO
>>>
```
## Forth question (!!HARD!!)

Get a sequence of numbers from user ans store them in a list ( lets say `a` e.g. )
find the size of this set

`{(x,y,z) : x<y<z , a[x] < a[y] < a[z] }`

#### input0
> 1 2 2 3 4

#### output0
> 6
