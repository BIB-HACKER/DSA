def reverse(x): 
  ret = 0
  while (x>0):
    ret = ret * 10 + x % 10
    # 5
    # 54
    # 543
    # 5432
    # 54321
    x //= 10

  return ret

# int beautifulDays(int i, int j, int k) 
# {
#     int ans =0;
#     for(int a = i; a <= j; a++)
#     {
#         int diff = abs(i-reverse(i));
#         if(diff % k == 0)
#            ans++; 
#      }
#     return ans;
# }

num=12345
print(reverse(num))