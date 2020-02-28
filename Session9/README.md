# Question0

implement a bidirectional linked list :)

![](Linkedlist.png)
**API**

| function/variable | description     |
| :-: |:-
data|the data stored in this node
next| points to the next node      |
previous|points to previous node
add|adds a node to specific index|
delete|deletes current node
root| returns the lists root
len| -
str| -
eq| -

![](Linkedlist_insert_middle.png)

![](Linkedlist_deletion.png)

# Question1

You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.

Your objective is to determine the length of the loop.

in the following example the tail's size is 3 and the loop size is 11.
```python
nodes=[node() for i in range(14)]
for node, next_node in enumerate(nodes,nodes[1:]):
  node.next=next_node
nodes[13].next=nodes[11]
```

> Use the `next` attribute to get the following node\
> `node.next`

> Note: do NOT mutate the nodes!


# Question2

A [perfect power](https://en.wikipedia.org/wiki/Perfect_power) is a classification of positive integers:

> In mathematics, a perfect power is a positive integer that can be expressed as an integer power of another positive integer. More formally, `n` is a perfect power if there exist natural numbers `m > 1`, and `k > 1` such that `m**k = n`.

Your task is to check wheter a given integer is a perfect power. If it is a perfect power, return a pair `m` and `k` with `mk = n` as a proof. Otherwise return `None`.

> Note: For a perfect power, there might be several pairs. For example 81 = 3^4 = 9^2, so (3,4) and (9,2) are valid solutions. However, the tests take care of this, so if a number is a perfect power, return any pair that proves it.

```
Examples
isPP(4) => [2,2]
isPP(9) => [3,2]
isPP(5) => None
```
