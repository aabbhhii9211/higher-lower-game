from art import logo, vs
from game_data import data
import random
from replit import clear

#display art
print(logo)
account_b = random.choice(data)
score = 0

#format the account data into printable format
def format_data(account):
    '''takes the account data and return the printable format'''
    account_name = account["name"]
    account_dis = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_dis}, from {account_country}"

def check_answer(guess,a_follower,b_follower):
    '''Take the user guess and followers counts and return if they got it right or not.'''
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess == 'b'


game_should_countinue = True
#make repeted the code 
while game_should_countinue:

    #generate a random  account from game data

    #making the acounts at possing b become the next account possion a.
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    #ask user for guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    #clear the screen 
    clear()
    print(logo)

    #give user feedback on therir guess.
    #track score
    if is_correct:
        score += 1
        print(f"You are right! you're current score is: {score}.")
    else:
        game_should_countinue = False
        print(f"Sorry, you are wrong. Final score is {score}.")