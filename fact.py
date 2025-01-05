def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
num=int(input("Enter the number"))
if num<0:
    print("Fect is not  defined in neg numbers")
else:
    print(f"The fact of {num} is {fact(num)}")
  