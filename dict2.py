"""wap to chech if a.A key is already present in a dict"""
def check_dict():
    n=int(input("Enter the number of items: "))
    dictionary={}
    for _ in range(n):
        key=input("Enter key: ")
        value=input("Enter value: ")
        dictionary[key]=value
    print(dictionary)
    #key is already present in dict
    key=input("Enter key to check: ")
    if key in dictionary:
        print(f"key '{key}' is present in the dict")
    else:
        print(f"key '{key}' is not present in the dict")
    #check if value presenet in dictionary
    value=input("Enter value to check: ")
    if value in dictionary.values():
        print(f"value '{value}' is present in the dict")
    else:
        print(f"value '{value}' is not present in the dict")
    #An item present in a dict
    key=input("Enter key to check: ")
    value=input("Enter value to check: ")
    if dictionary.get(key)==value:
        print(f"item '{key}','{value}' is present in the dict")
    else:
        print(f"item '{key}','{value}' is not present in the dict")
        
        

check_dict()