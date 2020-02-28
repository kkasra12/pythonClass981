class stack:
    def __init__(self):
        self.values=[]
    def push(self,value):
        self.values.append(value)


    def pop(self):
        if len(self.values)==0:
            return None
        else:
            return self.values.pop(-1)

    def lastItem(self):
        if len(self.values)==0:
            return None
        else:
            return self.values[-1]
    def isEmpty(self):
        if len(self.values)==0:
            return True
        else:
            return False
    def __len__(self):
        return len(self.values)
    def __str__(self):
        return f"[ {' '.join(self.values)} ]"
    def __eq__(self,other):
        if type(other)==type(self):
            return self.values==other.values
        raise Exception("other type is not stack")

if __name__ == '__main__':
    s=stack()
    s.push(1)
    s.push(4)
    s.push(6)
    s.push("kasra")
    s.push("hellllo")
    print(s.pop())
    print(s.lastItem())
    print(s.pop())
    print(s.pop())
    print(s.lastItem())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.lastItem())
    print(s.pop())
    print(s.pop())
    
