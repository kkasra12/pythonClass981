class FibMaker:
    def __init__(self):
        self.series=[]
    def isFib(self,num):
        if num in self.series:
            return True
        a,b=1,1
        n=2
        while b<num:
            a,b=b,a+b
            n+=1
            if n>len(self.series)+2: # if b not in self.series:
                self.series.append(b)
            if b==num:
                return True
        return False

f=FibMaker()
for i in [3,5,11,8,20,50,100,90]:
    print(f.isFib(i))
