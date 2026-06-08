##x=[[1,2,3],
##   [4,5,6],
##   [7,8,9]]
##y=[[1,2,3],
##   [4,5],
##   [7,8,9]]
##r=[]
##for i in range(len(x)):
##    r.append([])
##    if len(x[i])==len(y[i]):
##        for j in range(len(x[i])):
##            k=x[i][j]+y[i][j]
##            r[i].append(k)
##    else:
##        print('Not equal')
##        del r
##        break

# n=eval(input())
# d={}
# if isinstance(n,(list,tuple,set,dict)):
#     for i in n:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1
# else:
#     for i in str(n):
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1
# print(d)

a,b=0,1
for i in range(1,11): 
    print(a,end=' ')
    a,b=b,a+b
