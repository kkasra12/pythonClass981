# `os` Module

- os.name
****
- os.environ
- os.getenv()
- os.putenv()
****
- os.chdir()
- os.getcwd()
****
- os.mkdir()
- os.rmdir()
****
- os.remove()
- os.rename()
****
- os.walk()
```python
for root, dirs, files in os.walk(path):
    print(root)
```
- os.path
 - basename
 - dirname
 - exists
 - isdir and isfile
 - join
 - split

# `random` Module
- choice \
 **Question:** Roll a dice :)
- choices\
 **Question:** How to generate a 8 digit random password?
- randint\
 **Question:** Roll another dice :))
- random\
 **Question:** keep rolling dices :)))
- shuffle\
 **Question:** feel free to roll a simple dice :))))

# `time` Module
- time
- sleep

# `pickle` Module
- dump
- load

```python
from pickle import dump

myList=[1,2]
# some codes to populate myList
# now lets save it to use later

f=open("myList",'wb')
dump(myList,f)
f.close()
```

```python
from pickle import load
f=open("myList",'rb')
myList=load(f)
print(myList)
```
# More Modules to Read
- csv
- datetime
- urllib2
- hashlib
- json
- smtplib

# How to Install New Modules


first of all check if you have pip or not
```bash
$ pip3
pip 19.3.1 from /usr/local/lib/python3.6/dist-packages/pip (python 3.6)
```
> use `pip` if you have windows

## Install pip
to install pip, if you already don't have it:\
**In UNIX machines:**
```bash
$ sudo apt install python3-pip
```
or use any other package manager up to your distribution

**In Windows**
```bash
python -m pip install pip
```
*or:*

1. Download (get-pip.py)[https://bootstrap.pypa.io/get-pip.py] to a folder on your computer.
2. Run that file using python:
```bash
$ python get-pip.py
```
3. FINISH

## How to Use It
```bash
$ pip3 search <package-name>
$ pip3 install <package-name> --user
$ pip3 list
$ pip3 install <package-name> --upgrade
```
