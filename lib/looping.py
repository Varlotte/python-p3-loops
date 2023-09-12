#!/usr/bin/env python3

def happy_new_year():
    i=10
    while i >= 1:
        print (i)
        i-=1
    print ("Happy New Year!")
        


def square_integers(int_list):
    squaring = [number * number for number in int_list]
    return squaring
    

def fizzbuzz():
    for i in range(1,101):
        if (i % 15 == 0):
            print ("FizzBuzz")
        elif (i %3 ==0):
            print ("Fizz")
        elif (i %5 == 0):
            print ("Buzz")
        else:
            print (i)

    
