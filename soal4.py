import random
c=0
number=random.randint(1,20)
print(number)
while c<=5:
    n=int(input("Enter:"))
    if n>number:
        c+=1
        if c==6:
            print("u lost") 
            print(f"the number was {number}")
        else:

            print("koochik tar hads bezan:")
    elif n<number:
        c+=1
        if c==6:
            print("u lost") 
            print(f"the number was {number}")
        else:

            print("bozorgtar tar hads bezan:")
    else:
        print("right!")
        break
    