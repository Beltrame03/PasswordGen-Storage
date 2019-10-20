import random
import string

txt = open("password.txt", "a")

new = ''
print("Would you like to make a new password or input an existing password?")
print("Input new to make one and old to use a pre-existing one.")
print("Input 1 to quit the program")

while (new != '1'):

    new = input()
    new = new.upper()

    if new == 'NEW':
        def gen():
            global password
            password = ''
            print("How long would you like your password to be?")
            l = int(input())
            for i in range(l):
                char = random.choice(string.ascii_letters + string.digits)
                password = password + char
            txt.write('Password: ' + password + "\n" + "\n")
            return


        global name
        name = input("What is your username?")
        txt.write('Username: ' + name +'||')
        gen()
        break


    elif (new == 'OLD'):
        username = input("What is your username?")
        txt.write('Username: ' + username +'||')
        passname = input("What is your password?")
        txt.write('Password: ' + passname + "\n" + "\n")
        break


    else:
        print("What you inputted does not match one of our options.")
        print("Please input something that was specified.")
