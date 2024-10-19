# A B C
# A B
# A

for i in range(3):
   a=65
   for j in range(3-i):
      print(chr(a),end='\t')
      a+=1
   print()  

# 1 2 3
# 4 5
# 6

# a=1
# for i in range(3):
#     for j in range(3-1):
#         print(a,end='\t')
#         a+=1
#     print()

#1 2 1
#1 2 1
#1 2 1

# a=2
# for i in range(3):
#  for j in range(3):
#     if j==0:
#         print(a-1,end='\t')
#     elif j==1:
#         print(a,end='\t')
#     else:
#         print(a-1,end='\t')
#  print()