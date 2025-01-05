def calculator():
    print("1.Add ")
    print("2.Sub")
    print("3.Mul ")
    print("4.Div ")
    print("5.Exit")
    while True:
        choice=int(input("Enter your choice 1 to 5 "))
        if choice==5:
            print("Exiting the calculator")
            break
        if choice in [1,2,3,4]:
            num1=float(input("Enter the first number "))
            num2=float(input("Enter the sec number "))
            if choice==1:
                result=num1+num2
            elif choice==2:
                result=num1-num2
            elif choice==3:
                result=num1*num2
            elif choice==4:
                if num2!=0:
                    result=num1/num2
                else:
                    result="error div by zero "
            
            print(result)
                
        else:
            print("please enter number between 1 to 5 ")
            
calculator()



            
    