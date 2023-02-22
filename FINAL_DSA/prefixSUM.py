arr=[3, 4, 1, 7, 9, 1]
pre=[]
pre[0]=arr[0]
print(pre)
for i in range(1,len(arr)):
    pre[i]=pre[i-1]+arr[i]

print(pre)

# from itertools import accumulate
 
# def cumulativeSum(lst):
#     print (list(accumulate(lst)))
 
# # Driver program
# if __name__ == "__main__":
#     lst = [3, 4, 1, 7, 9, 1]
#     cumulativeSum(lst)