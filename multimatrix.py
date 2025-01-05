"""multiplay matrix"""
matrix1=[]
matrix2=[]
n=int(input("Enter the size of martix: "))
print("Enter the elements first matrix")
for i in range(n):
    row=[]
    for j in range(n):
        element=int(input("Enter the elements: "))
        row.append(element)
    matrix1.append(row)
print("Enter the sec matrix")
for i in range(n):
    row=[]
    for j in range(n):
        element=int(input("Enter the elements: "))
        row.append(element)
    matrix2.append(row)
result=[]
for i in range(len(matrix1)):
    result.append([])
    
    for j in range(len(matrix2[0])):
        sum=0
        for k in range(len(matrix2)):
            sum +=matrix1[i][k]*matrix2[k][j]
        result[i].append(sum)
print("Multi matrix result")
for i in result:
    print(i)
        