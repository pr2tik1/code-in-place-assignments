"""
Asks the user for two numbers and prints the result
of the first number minus the second number.
"""

def main():
    print("This program subtracts one number from another.")
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    total=a-b
    print("The result is "+str(total))

if __name__ == '__main__':
    main()