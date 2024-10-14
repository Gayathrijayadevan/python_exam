# A
# B A
# C B A

a=65
for i in range(3):
    for j in range(i+1):
        print(chr(a-j),end='\t')
    print()    
    a+1

# A B C
# C B A
# A B C

a = 65

for i in range(3):
    for j in range(3):
        if i % 2 == 0:
            print(chr(a + j), end=' ')
        else:
            print(chr(a + 2 - j), end=' ')
    print() 

# 1 A A
# B 1 B
# C C 1    

a = 65

for i in range(3):
    for j in range(3):
        if j == 0:
            print(chr(a + i), end=' ')
        elif j == 1:
            if i == 0:
                print('A', end=' ')
            elif i == 1:
                print('1', end=' ')
            else:
                print(chr(a + i), end=' ')
        else:
            if i == 0:
                print('A', end=' ')
            elif i == 1:
                print(chr(a + i), end=' ')
            else:
                print('1', end=' ')
    print()
