import random

message = input("Roll the dice? (y/n): ").lower().strip()

if message == "y":
    x = random.randint(1,6)
    y = random.randint(1,6)
    print(f"({x}, {y})")
elif message == "n":
    print("Thanks for playing!")

else:
    print("invalid choice!")