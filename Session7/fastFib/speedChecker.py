from time import time
from random import randint,gauss
from fastFib import FibMaker
from regularFib import  isFib
from collections import Counter
try:
    from matplotlib import pyplot as plt
    drawGraph=True
except:
    print('''You dont have matplotlib!!So I cant show any graph...
try installing it using:
    $pip install matplotlib''')
    drawGraph=False
# This is a Fibonacci series chose your constant wiser...
# 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393
#
TEST_SIZE=int(1e7)
START_RANGE=int(1.21e5)
END_RANGE=int(1.22e5)
print('generating numbers...')
# numbers=[randint(START_RANGE,END_RANGE) for _ in range(TEST_SIZE)]
numbers=[int(gauss((START_RANGE+END_RANGE)/2,(END_RANGE-START_RANGE)/12)) for _ in range(TEST_SIZE)]
print('numbers generated...')
print(f'''\tbiggest number generated: {max(numbers)}
\tsmallest number generated:{min(numbers)}''')
if drawGraph:
    numbersDest=Counter(numbers)
    ############this is not good(why?):
    #x=[i[0] for i in numbersDest.items()]
    #y=[i[1] for i in numbersDest.items()]
    ############this is much faster
    x=[]
    y=[]
    for i in numbersDest:
        x.append(i)
        y.append(numbersDest[i])
    print("numbers counted...\nmaking the graph...")
    plt.bar(x,y)
    plt.show()
ansfastFib=[]
ansreguFib=[]
print('...')
fastFib=FibMaker()
now=time()
for i in numbers:
    ansfastFib.append(fastFib.isFib(i))
fastFibTime=time()-now
print(f"time elapsed for fast fib is {fastFibTime}")

now=time()
for i in numbers:
    ansreguFib.append(isFib(i))
reguFibTime=time()-now
print(f"time elapsed for fast fib is {reguFibTime}")

if all([i==j for i,j in zip(ansfastFib,ansreguFib)]):
    print("\tNOTE: all answers match")
else:
    print("\tNOTE: all answers does NOT match")

ansDest=Counter(ansfastFib)

# plt.bar(['True','False'],[ansDest[True],ansDest[False]],yerr=["sallaaam","rrrr"])
print(f"number of mathed items: {ansDest[True]}\nnumber of unmathed items: {ansDest[False]}")
# plt.show()

fig, ax = plt.subplots()
y=[ansDest[True],ansDest[False]]
ax.bar(['True','False'],y)
for index,data in enumerate(y):
    plt.text(index, 10, s=f"{data}")
plt.tight_layout()
plt.show()
