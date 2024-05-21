#Data types
#1 strings (str)
#print(type("hello world"))
#print("hello world"[4]) #[] is called subscripting and is usually used to fish out a content is a line of code

#2 Integers (int)
#3 Float is any number that has a decimal point in it.
#4 Boolean

#conditional statements
#fnum = input("What is the first number? ")
#snum = input("What is the second number? ")

#if fnum > snum:
#    print("The first number is larger!")
#elif snum > fnum:
#    print("The second number is larger!")    
#else:
#    print("The numbers are the same!")

#try outs
score = input("What is your test score? ")
score = int(score)

if score >= 90:
    age = int(input("What is your age? "))
    if age < 25:
        print("Your grade is A+")
    else:
        print("Your grade is A")    
elif score >= 80:
    age = int(input("What is your age? "))
    if age < 25:
        print("Your grade is B+")
    else:
        print("Your grade is B")
elif score >= 70:
    print("Your grade is C")
elif score >= 60:
    print("Your grade is D")        
else:
    print("Next time study hard, YOU FAILED!!!!")