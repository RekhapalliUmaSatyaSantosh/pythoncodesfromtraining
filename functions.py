##def add(a,b):
##    '''Hello this is python class'''
##    c=a+b
##    d=a*b
##    e=a/b
##    f=a//b
##    g=a**b
##    h=a%b
##    print(f'add={c},minus={d},mult={e},div={f},floor={g},mod={h}'
##print(add(10,20))
##a=add(10,20)
##print(a)
##a=add
##print(a(10,20))
##print(a.__doc__)

##def add(a,b):
##    print(a+b
##    print(a
##print(add(10,20))

##def isprime(n):
##    for i in range(2,n):
##        if n%i==0:
##            print(False
##    print(True
##print(isprime(23))

##a=[[1,2,3],
##   [1,2,3]]
##b=[[1,2,3],
##   [1,2,3]]
##def validate(m1,m2):
##    if len(m1)!=len(m2):
##        print(False
##    for i in range(len(m1)):
##        if not (len(m1[i]) == len(m2[i]) and len(m1[i]) == len(m1[0])):
##            print(False
##    print(True
##print(validate(a,b))

##def validate(r,c):
##    res=[]
##    for _ in range(r):
##        a=input('Enter a matrix values=').split(',')
##        if c != len(a):
##            print('Not valid'
##        x=[]
##        for i in a:
##            x.append(int(i))
##        res.append(x)
##    print(res
##print(validate(2,2))

##r=int(input('enter rows='))
##c=int(input('enter columns='))
##res=[]
##for _ in range(r):
##    a=input('Enter a matrix values=').split(',')
##    if c != len(a):
##        print('Not valid')
##    x=[]
##    for i in a:
##        x.append(int(i))
##    res.append(x)
##print(res)

##l=['12','3456','789012']
##for i in l:
##    if len(i)%2==0:
##        print('even length=',i)
##    else:
##        print('Not in even length=',i)

##def isprime(n):
##    if n==1:
##        print(False
##    else:
##        for i in range(2,n):
##            if n%i==0:
##                print(False
##                break
##        print(True
##print(isprime(1))

##def isprime(n):
##    if n==1:
##        print(False
##    for i in range(2,n):
##        if n%i==0:
##            print(False
##    print(True
##n=4
##c=1
##for i in range(n):
##    c2=0
##    l=[]
##    while c2<=i:
##        if not isprime(c):
##            l.append(c)
##            c2+=1
##        c+=1
##    if i%2==0:
##        print(*l)
##    else:
##        print(*l[::-1])

##def num(*n):
##    for i in n:
##        if not isinstance(i,int):
##            print('Not a int'
##    print(n
##a=num(10,20,40,50,'hello')
##print(a)
##
##b=num(10,20,30)
##print(b)

##def val(**n):
##    for i in n.items():
##        print(i)
##val(name='satya',phno=1246808532,email='yourname@gmail.com',age=22)

# def cal(oper,*n):
#     r=0
#     for i in n:
#         if oper=='+':
#             r+=i
#             print(r)
#         elif oper=='-':
#             r-=i
#             print(r)
#         elif oper=='*':
#             r*=i
#             print(r)
#         elif oper=='/':
#             r/=i
#             print(r)
#         elif oper=='//':
#             r//=i
#             print(r)
#         elif oper=='%':
#             r%=i
#             print(r)
            
# print(cal('+',10,20,30,40))

# def info(name,wishes='Good morning'):
#     print('Hi',name,wishes)
# info('satya')
# info('satya','Good Evening')

def fact(n):
    if n<=1:
       return 1
    else:
       return n*fact(n-1)
print(fact(5))
