num=[23,4,5,6,11,77,9]
odd_num=[]
even_num=[]
for i in num:
    if i%2==0:
        even_num.append(i)
    else:
        odd_num.append(i)
print(odd_num)
print(even_num)
odd=0
even=0
for i in num:
    if i%2==0:
        even +=1
    else:
        odd +=1
print("count of odd numbers: "+str(odd))
print("count of even numbers:"+str(even))