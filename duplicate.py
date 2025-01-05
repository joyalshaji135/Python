"""duplicates from a list of integers"""
num=[2,3,4,5,6,7,8,9,9,2,22,44,5,10,22,2,4,8,10,1,11,22]
seen=set()
duplicate=set()
for i in num:
    if i in seen:
        duplicate.add(i)
    else:
        seen.add(i)
print("Duplicate: ",list(duplicate))