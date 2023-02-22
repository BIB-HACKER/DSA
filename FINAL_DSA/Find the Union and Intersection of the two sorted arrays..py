class Solution:
    def doUnion(self,a,n,b,m):
        # l=[]
        # for i in range(n):
        #     l.append(a[i])
        # for i in range(m):
        #     l.append(a[i])
        # uni=[]
        # c=0
        # for i in range(len(l)):
        #     if l[i] not in uni:
        #         uni.append(l[i])
        #         c+=1
        # return c
        
        # cou=0
        # for i in range(n):
        #     if a.count(a[i])==1:
        #         cou+=1
        # for j in range(m):
        #     if b[j] not in a: 
        #         cou+=1
        # return cou
        
        union_set = set(a).union(set(b))

        return len(union_set)

if __name__=='__main__':
    n=int(input("->"))
    m=int(input("->"))
    a=[1, 2 ,3, 4, 5]
    b=[1, 2, 3]
    ob=Solution()
    print(ob.doUnion(a,n,b,m))

