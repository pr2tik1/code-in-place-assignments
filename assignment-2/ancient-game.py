import random

def main():
    stone=20
    count=0
    
    while stone>1 and stone<=20:
        #Player 1
        if stone!=0:
            print("There are "+str(stone)+" stones left")    
            p1=int(input("Player 1 would you like to remove 1 or 2 stones? "))
        else:
            break
        if p1==1 or p1==2:
            stone-=p1
        while p1<1 or p1>2:
            p1=int(input("Please enter 1 or 2: "))
            stone-=p1
        count+=1
        
        print() 

        #Player 2
        if stone!=0:
            print("There are "+str(stone)+" stones left")
            p2=int(input("Player 2 would you like to remove 1 or 2 stones? "))
        else:
            break        
        if p2==1 or p2==2:
            stone-=p2
        while p2<1 or p2>2:
            p2=int(input("Please enter 1 or 2: "))
            stone-=p2 
        count+=1
        print()
    
    if count%2==0:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
        
if __name__ == '__main__':
    main()