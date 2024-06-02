#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
write_data = int(input("Do you want to write then type 1 or type 2 for reading past passwords"))

if(write_data == 1):    
    myDatabase = open(r"Password_Database.txt", 'a')

    st_website = input("Website you want to Sign_up in - \n")
    st_emailId = input("Your Email Id used for this website - \n")
    nr_letters = int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91


    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    password = ""

    # range goes from (begining{included} to ending{excluded runs till ending-1})
    # random.shuffle() helps to shuffle position of list members
    # read more about random.choice()
    for num in range(1, nr_letters+1):
        i = random.randint(0,51)
        password = password + letters[i]

    for num in range(1, nr_symbols+1):
        i = random.randint(0,8)
        password = password + symbols[i]

    for num in range(1, nr_numbers+1):
        i = random.randint(0,9)
        password = password + numbers[i]

    password = list(password)
    random.shuffle(password)


    ans = ""

    for num in password:
        ans += num

    print(ans)

    lineToWrite = st_website + "    " + st_emailId + "    " + ans  + "\n"

    myDatabase.write(lineToWrite)

    myDatabase.close()

elif(write_data == 2):
    with open(r"Password_Database.txt", 'r') as myDatabase:
        for line in myDatabase:
            print(line.strip())

else:
    print("Invalid Input")
