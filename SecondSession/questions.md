# QUESTION0
Bob's space button is broken and is misbihaving which inserts several space characters instead of one. Write a program to help him for this problem.

**input** is a string containing several consecutive spaces. 

**output** Replace this spaces with one single space. Also omit any extra space at the end or start of the string.

#### input0
>  Hello   my    name    is   Bob.

#### output0
> Hello my name is Bob.

# Question1
Bob wants to know all file extensions used in his computer, hence he has prepared a list containing all of files in his computer. Now help him to find all extensions and print them out.

**input** is a file names (each name in a single line)

**output** print all extensions:
- extensions must not be duplicated
- sort them in alphabetic order
- seperate each item with `--`

#### input0
> tmp.txt
>
> download.jpeg
>
> project.DB.first.exe

#### output0
> txt -- jpeg -- exe

# Question2
recently, Bob has studied about ([Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance).
now he invented new distance named Bob distance which works like this:
- check whether two strings has same length or not. answer `-1` if they are not same lenght
- find two strings differences
- sum all indexes which are different (indexes starts from 1)

*input* is two strings

*output* is a single number showing Bob distance

#### input0
1000111011
1000011110

#### output0
15

>10+5

# Question3
Bob could send an essay about his *'Bob distance'* to ISI.
now he wants to update his coding by changing the indexes:
 **number the index as increasing power of two and sum this new numbers**
 
#### input0
kasraaaa
jasrraae

#### output0
145

<table>
  <tr>
    <td>k</td><td>a</td><td>s</td><td>r</td><td>a</td><td>a</td><td>a</td><td>a</td>
  </tr>
  <tr>
    <td>j</td><td>a</td><td>s</td><td>r</td><td>r</td><td>a</td><td>a</td><td>e</td>
  </tr>
  <tr>
  <td><b>1</b></td><td>2</td><td>4</td><td>8</td><td><b>16</b></td><td>32</td><td>64</td><td><b>128</b></td>

  </tr>
</table>
`1+16+128=145`
