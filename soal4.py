import random
c = 0
number = random.randint(1, 20)
while c < 5:
    n = int(input("Enter: "))
    c += 1
    if n > number:
        print("koochik tar hads bezan:")
    elif n < number:
        print("bozorgtar hads bezan:")
    else:
        print("right!")
        break
if n != number:
    print("u lost")
    print(f"the number was {number}")