# # Iterative python program to reverse an array
 
# # Function to reverse A[] from start to end

# def reverselist(a,start,end):
#     while start<end:
#         a[start],a[end]=a[end],a[start] #SWAP METHOD
#         start+=1
#         end-=1

# # main
# a=[1,2,3,4,5,6]
# print(*a)
# reverselist(a,0,len(a)-1)
# print("Reversed list is")
# print(*a)

#- - - - - - - - - - - - - - - - - - - - - - - -

def reverselist(a):
    print(*a[::-1])

a=[1,2,3,4,5,6]
print(*a)
print("Reversed list is")
reverselist(a)
