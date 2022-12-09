import random
print("Guessing game")
print("Hello!")
Name=input("Enter Your name:")
print("\nWelcome, "+Name)
co=int(input("How many times you want to play"))
score=0
for i in range(co):
    print(f"Chance number",i+1)
    a=int(input("Enter the Lower boundry:" ))
    b=int(input("Enter the upper boundry: "))
    c=random.randint(a,b)
    quess=None
    no_guess=0
    limit=3
    while no_guess<limit:
        guess=int(input(f"enter a number between {a} and {b}:"))
        no_guess+=1
        if guess==c:
            print("Congrat's")
            score+=1
            break
        elif c > guess:
            print("your guess was too small")
        elif c < guess:
            print("your guess was too high")
    else:
        print("Better luck for next time!")
print(f"Your total score is",score, "out of",co)