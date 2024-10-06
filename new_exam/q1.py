# 1.
data=['hello','welcome','hai']

longest_word = ''
max_length = 0

for i in data:
    if len(i) > max_length:
        max_length = len(i)
        longest_word =i

print(f"The longest word is: {longest_word}")

# 11.A      
#    B A
#    C B A

a=65
for i in range(3):
    for j in range(i+1):
        print(chr(a-j),end='\t')
    print()    
    a+=1


Data = ['helo', 'welcome', 'hai']

smallest_word = Data[0]
min_length = len(smallest_word)

for word in Data:
    if len(word) < min_length:
        min_length = len(word)
        smallest_word = word

print(f"The smallest word is: {smallest_word}")

# 4.
n=[1,2,3,4,5,1,2,] 
l=[]
for i in n:
    if i not in l:
        l.append(i)
print(n)



