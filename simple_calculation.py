#This is for simple calculations#
def add(*b):
    sum=b[0]
    print(sum)
    for i in range(1,len(b)):
        sum=sum+i
        print(i)
    return sum

def sub(*b):

    sub=2*b[0];
    for i in b:
        sub=sub-i;
    return sub

def mul(*b):
    mul=b[0]
    for i in b:
        mul=mul*i
    return mul

def div(*b):
    x = b[0] / b[1]
    for i in range(2,len(b)):
        x=x/b[i]
    return x



