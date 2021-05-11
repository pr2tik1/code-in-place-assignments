"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random 

def main():
    ran1=random.randint(10,99)
    ran2=random.randint(10,99)
    total=ran1+ran2
    print("What is "+str(ran1)+" + "+str(ran2)+"?")
    ans=int(input("Your answer:"))
    if ans!=total:
        print("Incorrect."+"The expected answer is"+str(total))
    else:
        print("Correct!")    


if __name__ == '__main__':
    main()