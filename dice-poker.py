import random

is_playing = False
def roll():
    return print(random.randint(1, 6))



while True:
    print("Do you want to play a game of dice poker?")
    print("1) Yes")
    print("2) No")

    choice = input("Enter choice:")
    choice = choice.strip()

    if choice == "1":
        is_playing = True

    while is_playing:


        if choice == "1":
            roll()

