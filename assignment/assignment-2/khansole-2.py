"""
TODO: Write a description here
"""

import random

def main():
    ran1=random.randint(10,99)
    ran2=random.randint(10,99)
    total=ran1+ran2
    count=0

    while count<3:
        print("What is "+str(ran1)+" + "+str(ran2)+"?")
        ans=int(input("Your answer: "))
        if ans!=total:
            print("Incorrect. The expected answer is "+str(total))
            count=0
        else:
            count+=1
            print("Correct! You've gotten "+str(count)+" correct in a row")
    print("Congratulations! You mastered addition.")        

              


if __name__ == '__main__':
    main()