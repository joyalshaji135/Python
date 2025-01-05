matrix1=[]
matrix2=[]
n=int(input("Enter the size of matrix: "))
print("Enter the first element matrix ")
for i in range(n):
    row=[]
    for j in range(n):
        element=int(input("Enter the element: "))
        row.append(element)
    matrix1.append(row)
print("Enter the sec element matrix ")
for i in range(n):
    row=[]
    for j in range(n):
        element=int(input("Enter the element: "))
        row.append(element)
    matrix2.append(row)
    
result=[]
for i in range(len(matrix1)):
    result.append([])
    for j in range(len(matrix1[0])):
        sum=0
        for k in range(len(matrix2)):
            sum +=matrix1[i][k]*matrix2[k][j]
        result[i].append(sum)
print("matrix multi: ")
for i in result:
    print(i)
    