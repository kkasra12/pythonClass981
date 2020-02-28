def isFib(num):
    a,b=1,1
    while b<num:
        a,b=b,a+b
        if b==num:
            return True
    return False

if __name__ == '__main__':
    for i in [3,5,11,8,20,50,100,90]:
        print(isFib(i))
