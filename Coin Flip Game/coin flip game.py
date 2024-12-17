import random

heads_or_tails = random.randint(0, 1)
# print(heads_or_tails)

coin_flip = input('Pick an option. Type "heads" for Heads and type "tails" for Tail\n')
# print(coin_flip)

if heads_or_tails == 0:
    print("Heads")
    if coin_flip == "heads":
        print("You won!")
    elif coin_flip == "tails":
        print("You lost!")
    else:
        print("Invalid option!")
elif heads_or_tails == 1:
    print("Tails")
    if coin_flip == "tails":
        print("You won!")
    elif coin_flip == "heads":
        print("You lost!")
    else:
        print("Invalid option!")
else:
    print("Invalid Option!")
