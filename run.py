import gspread
from google.oauth2.service_account import Credentials



SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Quiz_Scores')



def get_user_name():
    """ 
    This takes the users name from them upon entry and will be
    used to save their highscore.
    This is lenient to be able to accept anything other 
    than an empty string.
    """
    print("Welcome to James' Quiz!\n")

    username = input("What is your name? ").capitalize()
    while username == "":
        print("Please enter a valid name.")
        username = input("What is your name? ").capitalize()
    if username != "":
        print(f"Let's get started {username}!")
    return username







def main_game():
    """
    This function will be the entire game, this will ask the
    user 10 questions and then tell them their final score.
    Then add their highscores to the Quiz_Scores Google spreadsheet
    and relay the highscore table back to them
    """
    username = get_user_name()

    score = 0

    print(f"Welcome {username}!")
    print("Question 1 \n")
    print("What is the capital of Australia?")
    userInput = input()
    if (userInput.lower() == "Canberra".lower()):
        print("That is correct!")
        print("-------------------------------")
        score +=1

    else:   
        print("Sorry, the correct answer is Canberra.")
        print("-------------------------------")

    print("Question 2 \n")
    print("Who won the Men's Euro 2020 competition?")
    userInput = input()
    if (userInput.lower() == "Portugal".lower()):
        print("That is correct!")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Portugal.")
        print("-------------------------------")

    print("Question 3 \n")
    print("What is the smallest planet in our solar system?")
    userInput = input()
    if (userInput.lower() == "Mercury".lower()):
        print("That is correct!")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Mercury.")
        print("-------------------------------")
    
    print("Question 4 \n")
    print("Name the first actor to play Dumbledore in the Harry Potter films.")
    userInput = input()
    if (userInput.lower() == "Richard Harris".lower()):
        print("That is correct!")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Richard Harris.")
        print("-------------------------------")
    
    print("Question 5 \n")
    print("What is the official language of Brazil?")
    userInput = input()
    if (userInput.lower() == "Portugese".lower()):
        print("That is correct!")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Portugese.")
        print("-------------------------------")
    
    print("Question 6 \n")
    print("What is the tallest man made structure on earth?")
    userInput = input()
    if (userInput.lower() == "Burj Khalifa".lower()):
        print("That is correct!")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Burj Khalifa.")
        print("-------------------------------")
    
    print("Question 7 \n")
    print("The first atomic bomb was dropped on which Japanese city?")
    userInput = input()
    if (userInput.lower() == "Hiroshima".lower()):
        print("That is correct!")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Hiroshima.")
        print("-------------------------------")
    
    print("Question 8 \n")
    print("What is the chemical symbol for iron?")
    userInput = input()
    if (userInput.lower() == "Fe".lower()):
        print("That is correct!")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Fe.")
        print("-------------------------------")
    
    print("Question 9 \n")
    print("What country has the most islands in the world?")
    userInput = input()
    if (userInput.lower() == "Sweden".lower()):
        print("That is correct!")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Sweden.")
        print("-------------------------------")
    
    print("Question 10 \n")
    print("What is the biggest mammal in the world?")
    userInput = input()
    if (userInput.lower() == "Blue whale".lower()):
        print("That is correct!")
        print("-------------------------------")
        score +=1

    else:   
        print("Sorry, the correct answer is Blue whale.")
        print("-------------------------------")
    
    
    print(f"Thanks for playing {username}, your final score was {score}")

    score_sheet = SHEET.worksheet("scores")
    score_sheet.append_row([username, score])

main_game()