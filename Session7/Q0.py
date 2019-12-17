class iterator:
    def __init__(self):
        self.lst=[]
        self.n=0
    def add(self,lst):
        self.lst+=lst
    def next(self):
        if self.n==len(self.lst):
            return None
            self.n=0
        ans=self.lst[self.n]
        self.n+=1
        # return self.lst.pop(0)
        return ans

a=iterator()
b=iterator()

b.add([6,9,1])
print(a.add([3,4,5]))
print(b)
print(a.next())
print(a.next())
print(a.next())
print(a.next())
print(b.next())
print(b.next())
print(b.next())

# class iterator:
#     def __init__(self):
#         self.lst=[]
#     def next(self,lst=[])
#         self.lst+=lst
#         if lst==[]:
#             return self.lst.pop(0)
#         else:
#             return None
#
#
# a=iterator()
# b=iterbtor()
#
# b.next([6,9,1])
# a.next([3,4,5])
#
# a.next()
