'''
Given two lists return a new one with the common values
'''
a = [1, 2, 2, 4]
b = [1,2,4]

c = []
for i in a:
    if i in b:
        c.append(i)
        
print(c)
