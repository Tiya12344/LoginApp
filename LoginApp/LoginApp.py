my_list = ["Liam", 11 , "Milton Keynes" , "01234567891"]
Name = str(input("What is your name?"))
age = int(input("What is your age? "))
Place = str(input("Which city do you live in? "))
PhoneNumber = str(input("What is your phone number? "))

if Name == my_list[0] and age == my_list[1]:
    print("You are now logged in!")
else:
    print("invalid credentials")