import string
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


# Get player username
def get_user_name():
    """
    This takes the users name from them upon entry and will be
    used to save their highscore.
    This is lenient to be able to accept anything other
    than an empty string.
    """
    while True:
        user_input = input("Enter a username: \n")

        if user_input.isalnum():
            return user_input
        else:
            print("Invalid input. Please enter a username with only letters and numbers")


try:
    username = get_user_name()
    print("Welcome ", username)
except ValueError as ve:
    print(str(ve))


# General Knowledge Quiz
def general_knowledge():
    """
    This function will be the general knowledge quiz, this will ask the
    user 10 questions and then tell them their final score.
    Then add their highscores to the Quiz_Scores Google spreadsheet
    and relay the highscore table back to them
    """
    def valid_input(user_input):
        """
        Checks if the input is a string and allows a whitespace to be entered, 
        but does not allow just a whitespace to be entered.
        """
        has_letters = any(char in string.ascii_letters for char in user_input)
        has_valid_chars = all(char in string.ascii_letters + ' ' for char in user_input)
        return has_letters and has_valid_chars

    def get_valid_input(question):
        while True:
            user_input = input(question)
            if valid_input(user_input):
                return user_input
            else:
                print("Invalid input. Please use letters only.")

    print(f"Welcome to the General Knowledge Quiz {username}!\n")
    print("if you do not know the answer press 'enter' to pass")
    score = 0

    questions = [
        "What is the capital of Australia?  ",
        "Who won the Men's Euro 2020 competition?  ",
        "What is the smallest planet in our solar system?  ",
        "What sport is played using Tees, clubs and holes?  ",
        "What is the official language of Brazil?  ",
        "What is the tallest man made structure in the world?  ",
        "The first atomic bomb was dropped on which Japanese city?  ",
        "What is the chemical symbol for iron?  ",
        "What country has the most islands in the world?  ",
        "What is the biggest mammal in the world?  "
    ]

    answers = [
        "Canberra",
        "Portugal",
        "Mercury",
        "Golf",
        "Portuguese",
        "Burj Khalifa",
        "Hiroshima",
        "Fe",
        "Sweden",
        "Blue whale"
    ]

    for i in range(10):
        print(f"Question{i + 1}\n")
        user_input = get_valid_input(questions[i])

        if user_input.lower() == answers[i].lower():
            print("That is correct!")
            print("-------------------------------")
            score += 1
        else:
            print(f"Sorry, the correct answer is {answers[i]}")
            print("-------------------------------")

    # Prints users name, score then recent highscores
    print(f"Thanks for playing {username}, your final score was {score}")
    score_sheet = SHEET.worksheet("general")
    score_sheet.append_row([username, score])
    print("-----------------------------")
    print("----------Recent scores------")
    print("-----------------------------\n")
    highscores = score_sheet.get_all_values()
    for row in highscores:
        print(row[0] + ':  ' + row[1])
    print("-----------------------------")
    print("-----------------------------")
    print("-----------------------------\n")
    play_again()


# Football Quiz
def football_quiz():
    """
    This function will be the football quiz, this will ask the
    user 10 questions and then tell them their final score.
    Then add their highscores to the Quiz_Scores Google spreadsheet
    and relay the highscore table back to them
    """
    print("Welcome to the Football Quiz!\n")
    print("if you do not know the enter press type 'pass' to pass")
    score = 0

    def valid_input(user_input):
        """
        Checks if the input is a string and allows a whitespace to be entered, but
        does not allow just a whitespace to be entered.
        """
        has_letters = any(char in string.ascii_letters for char in user_input)
        has_valid_chars = all(char in string.ascii_letters + ' ' for char in user_input)
        return has_letters and has_valid_chars

    def get_valid_input(question):
        # Returns error to user if invalid input is entered
        while True:
            user_input = input(question)
            if valid_input(user_input):
                return user_input
            else:
                print("Invalid input. Please use letters only.")

    print(f"Welcome to the Football Quiz {username}!\n")
    print("if you do not know the answer press type 'Pass'")
    score = 0

    questions = [
        "Who won the 2006 World cup?  ",
        "Who scored the winner in the 2014 World cup final?  ",
        "Who is the all time top goalscorer in the World Cup?  ",
        "What team have won the Champions league the most?  ",
        "What player has sold the most football jerseys?  ",
        "Where was the 2016 Champions League final held?  ",
        "Where was the world cup controversially held in 2022?  ",
        "Who is the most decorated manager of all time?  ",
        "What national team made their debut in the 2010 world cup?  ",
        "Who is the current manager of Liverpool FC?  "
    ]

    answers = [
        "Italy",
        "Mario Gotze",
        "Miroslav Klose",
        "Real Madrid",
        "Lionel Messi",
        "San Siro",
        "Qatar",
        "Alex Ferguson",
        "Slovakia",
        "Jurgen Klopp"
    ]

    for i in range(10):
        print(f"Question{i + 1}\n")
        user_input = get_valid_input(questions[i])

        if user_input.lower() == answers[i].lower():
            print("That is correct!")
            print("-------------------------------")
            score += 1
        else:
            print(f"Sorry, the correct answer is {answers[i]}")
            print("-------------------------------")

    print(f"Thanks for playing {username}, your final score was {score}")
    score_sheet = SHEET.worksheet("football")
    score_sheet.append_row([username, score])
    print("-----------------------------")
    print("----------Recent scores------")
    print("-----------------------------\n")
    highscores = score_sheet.get_all_values()
    for row in highscores:
        print(row[0] + ':  ' + row[1])
    print("-----------------------------")
    print("-----------------------------")
    print("-----------------------------\n")
    play_again()


# Music Quiz
def music_quiz():
    """
    This function will be the music quiz, this will ask the
    user 10 questions and then tell them their final score.
    Then add their highscores to the Quiz_Scores Google spreadsheet
    and relay the highscore table back to them
    """
    def valid_input(user_input):
        """
        Checks if the input is a string and allows a whitespace to be entered, but
        does not allow just a whitespace to be entered.
        """
        has_letters = any(char in string.ascii_letters for char in user_input)
        has_valid_chars = all(char in string.ascii_letters + ' ' for char in user_input)
        return has_letters and has_valid_chars

    def get_valid_input(question):
        while True:
            user_input = input(question)
            if valid_input(user_input):
                return user_input
            else:
                print("Invalid input. Please use letters only.")

    print(f"Welcome to the Music Quiz {username}!\n")
    print("if you do not know the answer press type 'pass' to pass")
    score = 0

    questions = [
        "What band wrote 'Let it be?'  ",
        "What is the name of the sold vinyl of all time?  ",
        "What band tragically died in Sweden in 2016?  ",
        "Finish the song name 'Mr Blue ...' ?  ",
        "What song has been streamed the most (as of march 2023)?  ",
        "Who has won the most Grammy awards?  ",
        "What artist has played at glastonbury festival the most?  ",
        "Who 'wrote' Party in the USA?  ",
        "What city are the band Arctic Monkeys from?  ",
        "Who is the lead singer of Coldplay?  "
    ]

    answers = [
        "The Beatles",
        "Thriller",
        "Viola beach",
        "Sky",
        "Blinding lights",
        "Beyonce",
        "Van morrison",
        "Jessie J",
        "Sheffield",
        "Chris Martin"
    ]

    for i in range(10):
        print(f"Question{i + 1}\n")
        user_input = get_valid_input(questions[i])

        if user_input.lower() == answers[i].lower():
            print("That is correct!")
            print("-------------------------------")
            score += 1
        else:
            print(f"Sorry, the correct answer is {answers[i]}")
            print("-------------------------------")

    print(f"Thanks for playing {username}, your final score was {score}")
    score_sheet = SHEET.worksheet("music")
    score_sheet.append_row([username, score])
    print("-----------------------------")
    print("----------Recent scores------")
    print("-----------------------------\n")
    highscores = score_sheet.get_all_values()
    for row in highscores:
        print(row[0] + ':  ' + row[1])
    print("-----------------------------")
    print("-----------------------------")
    print("-----------------------------\n")

    play_again()


def play_again():
    """
    Asks the user if they would like to restart the game.
    """
    replay = input("Would you like to play again?(Y/N): ").lower()
    if replay == "Y".lower():
        choose_quiz()
    elif replay == "N".lower():
        print("Thanks for playing!")
    else:
        print("Invalid input entered, the game has been ended.")


def choose_quiz():
    """
    asks the user what quiz they would like to play
    """
    while True:
        print("What quiz would you like to play?\n")
        print("Your choices are:")
        print("General Knowledge\nFootball\nMusic")
        print("Please type general, football or music")
        userInput = input().lower()
        if userInput == "general":
            general_knowledge()
            break
        elif userInput == "football":
            football_quiz()
            break
        elif userInput == "music":
            music_quiz()
            break
        else:
            print(f"{userInput} is an invalid choice, please try again")


choose_quiz()
