dict = {'Mon':1,'Tue':9,'Wed':3,'Thu':7}

print("The given dictionary : ",dict)

check_key = input("Enter Key to check: ")

check_value = input("Enter Value: ")

if check_key in dict:

    print(check_key,"is Present.")

    dict.pop(check_key)

    dict[check_key]=check_value

else:

    print(check_key, " is not Present.")

    dict[check_key]=check_value

    print("Updated dictionary : ",dict)