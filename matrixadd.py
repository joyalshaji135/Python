"""WAP to add two matrix"""
matrix1=[]
matrix2=[]
n=int(input("Enter the size of matrix: "))
print("Enter the element of the first matrix: ")
for i in range(n):
    row=[]
    for j in range(n):
        element=int(input("Enter elements "))
        row.append(element)
    matrix1.append(row)
print("Enter the sec matrix")    
for i in range(n):
    row=[]
    for j in range(n):
        element=int(input("Enter elements "))
        row.append(element)
    matrix2.append(row)
result=[]
for i in range(n):
    row=[]
    for j in range(n):
        row.append(matrix1[i][j]+matrix2[i][j])
    result.append(row)
print("Result of matrix addition is ")
for i in result:
    print(i)
        