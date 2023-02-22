# Given an array of size 'num' another number 'num2'. also given a size 's' (integer value) of the subset. the task is to find if ther number 'num2' if present in every non-overlapping subset of size 's' in the given array. if its present in every subset print 1 otherwise 0.

num=int(input("->"))
arr=[13 ,24 ,20, 2, 10, 20, 3, 20, 5 ,55, 20, 13]
for i in range(num):
    arr.append(int(input("enter value =")))
s=int(input("->"))
num2=int(input('->'))

flag = 0
for i in range(0,num,s): # 13 24 10 2 10 20 3 20 5 55 20 13
    
    for j in range(i,i+s):
        if arr[j]==num2:
            flag=1
    
    if flag==1:
        continue 
    else:
        flag=0
        break

print(flag)


