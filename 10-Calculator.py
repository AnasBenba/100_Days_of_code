#Calculator
from calculator_art import logo
import sys
import os

def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def mul(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2


operations = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': div
}

def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls') # For Windows
    else:
        os.system('clear') # For Linux and macOS

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for key in operations:
    print(key)
  should_continue = True
  
  while should_continue:
    operatin_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    
    function = operations[operatin_symbol]
    
    answer = function(num1, num2)
    print(f"{num1} {operatin_symbol} {num2} = {answer}")
    decide = input(f"Type 'y' to continue calculating with {answer}, or type 'c' to start new calculation or 'n' to exit.: ")
    if decide == 'y':
      num1 = answer
      clear_console()
    elif decide == 'c':
      should_continue = False
      clear_console()
      calculator()
    else:
        should_continue = False

calculator()