import random
c=[]
a='BOY'

b=list(a)
for i in range(4):#probability  of boy is 4
    random.shuffle(b)
    c.append(''.join(b))
#print(c)
d=set(c)
print(list(d))
    

    
    
