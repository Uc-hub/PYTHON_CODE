print("Choose the correct number between 1 and 10 to hit the jackpot: ")
number = int(input())
if number < 5:
    print("You have one more chance")
    print("hint: guess higher")
    number = int(input())
    if number == 5:
        print("JACKPOT!!!!!, YOU WON")
    else:
        print("YOU LOOSE")
        print("GAME OVER")
elif number > 5:
    print("hint: guess lower")
    number = int(input())
    if number == 5:
        print("JACKPOT!!!!!, YOU WON")
    else:
        print("YOU LOOSE")
        print("GAME OVER")
else:
    print("JACKPOT!!!, YOU GOT IT IN YOUR FIRST TRIAL")
    print("Enter your mobile number to get your reward")
    mobileNumber = int(input())
    print("GET OUT YOU TOO LIKE FREE THING")