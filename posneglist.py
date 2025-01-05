num=[1,-2,-3,4,5,6,-7]
pos=[]
neg=[]
for i in num:
    if i>0:
        pos.append(i)
    else:
        neg.append(i)
        
print(pos)
print(neg)