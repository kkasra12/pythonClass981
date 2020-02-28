class FibMaker:
    def __init__(self):
        self.series={1,1}
        self.lastNum0=1
        self.lastNum1=1

    def isFib(self,num):
        if num in self.series:
            return True
        if num<self.lastNum1:
            return False
        a,b=self.lastNum0,self.lastNum1
        while b<num:
            a,b=b,a+b
            self.series.add(b)
            if b==num:
                self.lastNum0=a
                self.lastNum1=b
                return True
        self.lastNum0=a
        self.lastNum1=b
        return False

if __name__ == '__main__':
    f=FibMaker()
    for i in [3,5,11,8,20,50,100,90]:
        print(f.isFib(i))
