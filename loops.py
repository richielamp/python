#fruits = ["apple", "bananas", "cherry"]
#for i in fruits:
#    print(i + " pie")

#for num in range (1,100):
#    if num % 3 == 0:
#        print(num)

#import time
#choice =int(input("What number would you choose? "))

#def function(choice):
#    for num in range (1,choice):
#        if num % 3 == 0 and num % 5 == 0:
#            print("fizzbuzz")
#        elif num % 3 == 0:
#            print("fizz")
#        elif num % 5 == 0:
#            print("buzz")
#        else:
#            print(num)

#print("about to run the program, please wait a while")
#time.sleep(10)
#function(choice)

name = input("What is your name? \n")

def greeting(name): #it doesnt really matter what you call your function
    print(f"Hello {name}")

greeting(name)

ip = input("What is your IP address? \n")

def nmap(ip):
    print(f"Attacking {name}'s IP addresss {ip}")

nmap(ip)