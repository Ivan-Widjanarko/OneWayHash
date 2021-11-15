# import the library
import os       # for clearConsole()
import sys      # for sleepTime() and exit()
import time     # for timeSleep()
import hashlib  # for md5Function() and sha1Function()

def menu():

    """Display the hashing menu"""

    print("""
    Please choose the Hashing Methods below
    \t0. Exit
    \t1. MD5
    \t2. SHA-1
    """)
    userChoice = input("Your Choice : ") # user choice
    while (userChoice != '0') and (userChoice != '1') and (userChoice != '2'): # error handling
        print("""
        Wrong Input!!!
        Please Try Again
        """)
        userChoice = input("Your Choice : ") # user choice

    if userChoice =='0':    # choice 0 (exit)
        print("""
        Thank You for Using this Cryptography
        See You Again
        """)
        sleepTime()     # call sleepTime() function
        clearConsole()  # call clearConsole() function
        sys.exit()      # exit the program
    elif userChoice == '1': # choice 1 (MD5)
        sleepTime()     # call sleepTime() function
        clearConsole()  # call clearConsole() function
        md5Function()   # call md5Function() function
    elif userChoice == '2': # choice 2 (SHA-1)
        sleepTime()     # call sleepTime() function
        clearConsole()  # call celarConsole() function
        sha1Function()  # call sha1Function() function

def md5Function():

    """Hashing with MD5 Algorithm"""

    md5Input = input("Enter MD5 String: ")          # user input for hashing
    
    md5Result = hashlib.md5(md5Input.encode())      # encoding user input then sending to md5() function
    
    print("Hashing Successful")
    print("The MD5 Hashing Result is : ", end ="")
    print(md5Result.hexdigest())                    # printing the hashing result in hexadecimal value

    menu()                                          # display the menu again

def sha1Function():

    """Hashing with SHA-1 Algorithm"""

    sha1Input = input("Enter SHA-1 String: ")           # user input for hashing
    
    sha1Result = hashlib.sha1(sha1Input.encode())       # encoding user input then sending to sha1() function
    
    print("Hashing Successful")
    print("The SHA-1 Hashing Result is : ", end ="")    
    print(sha1Result.hexdigest())                       # printing the hashing result in hexadecimal value

    menu()                                              # display the menu again

def clearConsole():

    """Clear the console based on the OS"""

    command = 'clear'               # command for console clearing
    if os.name in ('nt', 'dos'):    # if the machine is running on Windows, then use cls
        command = 'cls'
    os.system(command)              # othen than Windows, use clear

def sleepTime():

    """delaying the process"""

    for remaining in range(3, 0, -1):   # 3 seconds delay
        sys.stdout.write("\r")                                              # carriage return
        sys.stdout.write("Please wait for{:2d} seconds.".format(remaining)) # delay countdown
        sys.stdout.flush()                                                  # flush the buffer
        time.sleep(1)                                                       # delay 1 second
    print("\nComplete!\n")                                                  # end of delay

print("Welcome to Cryptography")    # Title
menu()                              # call menu() function