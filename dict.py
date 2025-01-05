dict1={1:'Abc',2:'cde',3:'efg'}
dict2={'age1':21,'age2':22,'age':32}

dict1.update(dict2)
print(dict1)  #merge

#update dict
dict1.update({1:'abcdefg'})
print(dict1)
dict2.update({'age1':25})
print(dict2)

#add an element to dict
dict1[5]="adhi"
print(dict1)

#remove
dict1.pop(5)
print(dict1)

#delete
del dict1[3]
print(dict1)

#get value and key of particular item)
for i in dict1:
    print(i,dict1[i])