"""+ve num -ve num count find"""
list=[2,1,-3,-5,4,-10,5]
pos=0
neg=0
for i in list:
    if(i>0):
        pos +=1
    else:
        neg +=1
        
print("number of positive numbers: ",pos)
print("number of negative nummber: ",neg)

