# Question0
write a function which gets a nested list and a number. This function should search the number in the list and returns its place as sequence of indexes, also this function should returns the lists structure.

 **input** is a list and a number\
 **output** must be sequence of indexes pointing to that number and the structure of nested lists.

#### sampleCode
```python
def listShape(lst,n):
  # blub blub blub
  pass

nestedList=[
  [
    [
      [1,2],
      [3,4],
      [5,6]
    ],
    [7,8],
    [9,10,11],
    [12],
    [13,14,15]
  ],
  [
    [16],
    [17,18],
    [19,20,21],
    [
      [22],
      [
        [23,24],
        [25,26,27],
      ],
      [28]
    ],
    [29]
  ],
  [30],
]
print(nestedList,15)
```
#### Output
```python
[0,4,2],
[
  3,
  [5,5,1],
  [
    [3,2,3,1,3],
    [1,2,3,3,1],
    [0]
  ],
  [
    [
      [2,2,2],
      [0,0],
      [0,0,0],
      [0],
      [0,0,0]
    ],
    [
      [0],
      [0,0],
      [0,0,0],
      [1,2,1],
      [0]
    ]
  ],
  [
    [
      [
        [0,0],
        [0,0],
        [0,0]
      ],
    ],
    [
      [
        [0],
        [2,3],
        [0]
      ],
    ]
  ],
  [
    [
      [
        [
          [0,0],
          [0,0,0]
        ],
      ],
    ]
  ],
]
```

# Question1
Implement a function which it can calculate the reverse of another function.\
we know `y=f(x)` where `y` value and `f` function are available. Finding `x` is the goal.

**input**
- first input is a function
- second one is `y` value
- third and forth values are the ranges which contains the answer(generally, the whole function range or any sub-range of that)

**output** is `x` which `y==f(x)` is **True** value.

#### sampleCode
```python
def f_inv(f,y,startRange,endRange):
  # blub blub blub
  pass


g=lambda x: 2*x**2+x
print(f_inv(g,g(4,5),0,5))
```
#### output
```
4.5
```
or any number near to `4.5`
