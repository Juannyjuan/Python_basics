# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 14:46:51 2023

I asked chatgpt to come up with some challenges based on the basics of Python
Here is my attempt to strengthen my fundamentals through these challenges

@author: Juan
"""

# Challenge 1: Calculator function
''' 
Create a simple calculator function that takes two numbers and an operator as input
and returns the result. The function should support addition, subtraction, multiplication,
and division.
'''

def calculate(num1, num2, operator):
    try:
        if operator == "+":
            result = num1+num2
        elif operator == "-":
            result = num1-num2
        elif operator == "*" or "x" or "X":
            result = num1*num2
        elif operator == "/":
            result = num1/num2
    except SyntaxError:
        print("check if inputed numbers are int/float & operator is str")
    except ZeroDivisionError:
        print("numbers cannot be divided by zero")
    return result

calculate(5,2,"*")


# Challenge 2: Check even or odd
'''
Write a function that takes an integer as input and prints whether it is even or odd.
'''

def odd_even_checker(integer):
    try:
        number = int(integer)
        remainder = number%2
        if remainder == 0:
            return "Integer is an even number."
        else:
            return "Integer is an odd number."
    except ValueError:
        print("Error: please enter a valid integer.")
    
odd_even_checker(5)


# Challenge 3: Temperature Converter
'''
Write a function that converts a temperature from Celsius to Fahrenheit. 
The formula is F = C * 9/5 + 32. Test your function with a few temperatures.
'''

def fahrenheit_converter(celsius):
    try:
        temp_c = float(celsius)
        temp_f = temp_c *(9/5) + 32
        return temp_f
    except ValueError:
        print("Error: please enter a valid number without the symbols")
        
fahrenheit_converter("15")
fahrenheit_converter(0)
fahrenheit_converter(36.5)


# Challenge 4: List Manipulation
'''
Create a list of your favorite fruits. 
Write a function that adds a new fruit to the list. 
Write another function that removes a fruit from the list. 
Print the updated list after each operation.
'''

favourite_fruits = ["Guava","Pomelo","Mango","Watermelon"]

def add_fruit(new_fruit):
    fruit = new_fruit.title()
    favourite_fruits.append(fruit)
    return favourite_fruits

def remove_fruit(old_fruit):
    fruit = old_fruit.title()
    favourite_fruits.remove(fruit)
    return favourite_fruits

add_fruit("peach")
remove_fruit("guava")


# Challenge 5: Factorial Calculator
'''
Write a function that calculates the factorial of a given number. 
The factorial of a non-negative integer n is the 
product of all positive integers less than or equal to n.
'''

def calculate_factorial(integer):
    try:
        number = int(integer)
        factorial_result = 1
        for i in range (number):
            factorial_result *= (i+1)
        return factorial_result

    except ValueError:
        print("Error: please input a valid integer")

calculate_factorial(4)


# Challenge 6: Print Patterns
'''
Write a Python program to print the following patterns using loops
I have written the code, print them out if you want to see the patterns
'''
## pattern 1
for i in range(6):
    print(i*"*")
## pattern 2
for i in range(6):
    print((5-i)*"*")


# Challenge 7: Simple Guessing Game
'''
Create a simple guessing game. Generate a random number between 1 and 10. 
Ask the user to guess the number. 
Provide feedback on whether the guess is too high, too low, or correct.
'''

import random

random_number = random.randint(1,10)
user_input = int(input("The random number has been generated, guess the number:  > "))

while user_input != random_number:
    if user_input > random_number:
        print("too high")
    elif user_input < random_number:
        print("too low")
    user_input = int(input("Try another number:  > "))
else:
    print("Correct! You got it!")


# Challenge 8: Dictionary Operations
'''
Create a dictionary representing a person. 
Include keys for name, age, city, and occupation. 
Write a function to update any of these values. Print the updated dictionary.
'''

person_info = {}
keys = ["name", "age", "city", "occupation"]
values = ["Dell", "23", "Singapore", "Unemployed"]
for i in range(4):
    person_info[keys[i]] = values[i]

def info_update(key, value):
    person_info[key] = value
    return person_info

info_update("occupation","Frisbee Player")


# Challenge 9: Fibonacci Sequence
'''
Write a function to generate the Fibonacci sequence up to a given number n. 
The Fibonacci sequence is a series of numbers where 
each number is the sum of the two preceding ones, usually starting with 0 and 1.
'''

def fibo_sequence(n):
    number = int(n)
    fibo_list = [0,1]
    while fibo_list[-1] < number:
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    return fibo_list[:-1]

fibo_sequence(50)


# Challenge 10: Reverse a String
'''
Write a function that takes a string as input and returns the reverse of the string. 
Test it with various words.
'''

def string_reversal(string):
    return string[::-1]

string_reversal("water")
string_reversal("reversal")
string_reversal("racecar")
