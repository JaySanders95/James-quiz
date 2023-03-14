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

scores = SHEET.worksheet('scores')

def get_user_name():
    """ 
    This takes the users name from them upon entry and will be
    used to save their highscore.
    """
    print("Welcome to James' Quiz!\n")
    print("When playing the game,\n")
    print("Please enter 't' for true\n")
    print("and 'f' for false.\n")
    name = input("What is your name? ").capitalize()
    while name == "":
        print("----------------------------")
        print("You havent entered a name\n")
        print("Please enter a valid name.\n")
        name = input("What is your name? ").capitalize()
        if name != "":
            
            print(f"Welcome {name}!")
    username = name



get_user_name()