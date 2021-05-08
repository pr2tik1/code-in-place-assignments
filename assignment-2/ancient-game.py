import random

def main():
    stone=20
    count=0
    
    while stone>0 and stone<=20:
        
        print("There are "+str(stone)+" stones left")
        amount=int(input("Player 1 would you like to remove 1 or 2 stones? "))
        if amount==1 or amount==2:
            stone-=amount
        while amount<1 or amount>2:
            amount=int(input("Please enter 1 or 2: "))
            stone-=amount
        x=1
        count+=x    
        print("   ") 
        print("There are "+str(stone)+" stones left")
        amount=int(input("Player 2 would you like to remove 1 or 2 stones? "))
        if amount==1 or amount==2:
            stone-=amount
        while amount<1 or amount>2:
            amount=int(input("Please enter 1 or 2: "))
            stone-=amount 
        y=1
        count+=y
        print("   ")
    if count/2==0:
        print("Player ")        
    print("Game over")
 
        
if __name__ == '__main__':
    main()