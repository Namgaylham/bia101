# obj: a calculator application made using
# variable and if statement

#steps
# get input from user
# do calculation based on the user input
# check what string did user typed
# if user use string 
# give output to the user

#print("* for multiplication")
#print('+ for addition')
#print('- for subtraction')
#print('/ for division')

#watusertyped = input("+")
#print('you typed: ', watusertyped)
#print('user input-type', type(watusertyped))

#if  watusertyped =="+":
   # print('doing addition')

   # print('doing more addition')
    
    #if  watusertyped =="-":
       # print('doing subtraction')
       # print('doing more subtraction')
        
        
        
        # Objective: a calculator application made using 
# variables and if statements

# STEPS
# 1. get input from user --> DONE

# 2. do calculation based on user input
# 2.1 check what string did user typed
# 2.2 if usser string == * then do multiplicatio and so on

# 3. give output to the user

print('* for multipliocation')
print('+ for addition')
print('- for subtraction')
print('/ for division')

whatUserTyped = input()

print('User typed:', whatUserTyped)
print('user input-type', type(whatUserTyped))

print('-------------------')
if whatUserTyped == "+":
    print('Doing Addition')
    if 'a' == 'b':
        print('a is not b')
    if 'b' == 'b':
        print('b is b')

print('doing more addition')

if whatUserTyped == "-":
    print('Doing Subtraction')
    print('doing more subtraction')