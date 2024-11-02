# largest among the numbers in a list 

# l=[1,15,3,10,5,11]
# n=l[0]
# for i in l:
#     if i>n:
#         n=i
# print("largest number is:",n)      

# reverse of a string

# a = 'welcome'
# s = ''
# i = len(a) - 1  

# while i >= 0:
#     s += a[i]  
#     i -= 1  

# print(s)

# largest word in the list 

a=['haii','hello','welcome','nicetomeetyou']

largest_word=''
n=0
for i in a:
    if len(i)>n:
        n=len(i)
        largest_word=i
print("largest word is:",largest_word)        

