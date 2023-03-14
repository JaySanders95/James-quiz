import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint


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


    username = input("What is your name? ").capitalize()
    while username == "":
        print("Please enter a valid name.")
        username = input("What is your name? ").capitalize()
    if username != "":
        print(f"Let's get started {username}!")
    return username







def general_knowledge():
    """
    This function will be the general knowledge quiz, this will ask the
    user 10 questions and then tell them their final score.
    Then add their highscores to the Quiz_Scores Google spreadsheet
    and relay the highscore table back to them
    """
    username = get_user_name()
    print("Welcome to the General Knowledge Quiz!\n")
    score = 0
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

    score_sheet = SHEET.worksheet("general")
    score_sheet.append_row([username, score])

    print("-----------------------------")
    print("----------Highscores---------")
    print("-----------------------------\n")
    highscores = score_sheet.get_all_values()
    pprint(highscores)


def football_quiz():
    """
    This function will be the football quiz, this will ask the
    user 10 questions and then tell them their final score.
    Then add their highscores to the Quiz_Scores Google spreadsheet
    and relay the highscore table back to them
    """
    username = get_user_name()
    print("Welcome to the Football Quiz!\n")
    score = 0
    print("Question 1 \n")
    print("Who won the 2006 World cup?")
    userInput = input()
    if (userInput.lower() == "Italy".lower()):
        print("That is correct!")
        print("They won 5-3 on penalties against France.")
        print("-------------------------------")
        score +=1

    else:   
        print("Sorry, the correct answer is Italy.")
        print("They won 5-3 on penalties against France.")
        print("-------------------------------")

    print("Question 2 \n")
    print("Who scored the winner in the 2014 World cup final?")
    userInput = input()
    if (userInput.lower() == "Mario Gotze".lower()):
        print("That is correct!")
        print("He scored in the 113th minute to win.")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Mario Gotze.")
        print("He scored in the 113th minute to win.")
        print("-------------------------------")

    print("Question 3 \n")
    print("Who is the all time top goalscorer in the World Cup?")
    userInput = input()
    if (userInput.lower() == "Miroslav Klose".lower()):
        print("That is correct!")
        print("He is currently top with 16 goals")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Miroslav Klose.")
        print("He is currently top with 16 goals")
        print("-------------------------------")
    
    print("Question 4 \n")
    print("Who won the Premier league in 2015-16.")
    userInput = input()
    if (userInput.lower() == "Leicester".lower()):
        print("That is correct!")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Leicester City.")
        print("-------------------------------")
    
    print("Question 5 \n")
    print("What player has sold the most football jerseys?")
    userInput = input()
    if (userInput.lower() == "Lionel Messi".lower()):
        print("That is correct!")
        print("As of 2023, lionel messi leads the sales with 1.2 million")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Lionel Messi.")
        print("As of 2023, lionel messi leads the sales with 1.2 million")
        print("-------------------------------")
    
    print("Question 6 \n")
    print("What year was VAR introduced into the premier league?")
    userInput = input()
    if (userInput == 2019):
        print("That is correct!")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is 2019.")
        print("-------------------------------")
    
    print("Question 7 \n")
    print("Where was the world cup controversially held in 2022?")
    userInput = input()
    if (userInput.lower() == "Qatar".lower()):
        print("That is correct!")
        print("It was held during the middle of the domestic timetable")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Qatar.")
        print("It was held during the middle of the domestic timetable")
        print("-------------------------------")
    
    print("Question 8 \n")
    print("Who is the most decorated manager of all time?")
    userInput = input()
    if (userInput.lower() == "Alex Ferguson".lower()):
        print("That is correct!")
        print("He has 49 titles")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Alex Ferguson.")
        print("He has 49 titles")
        print("-------------------------------")
    
    print("Question 9 \n")
    print("What national team made their debut in the 2010 world cup?")
    userInput = input()
    if (userInput.lower() == "Slovakia".lower()):
        print("That is correct!")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Slovakia.")
        print("-------------------------------")
    
    print("Question 10 \n")
    print("Who is the current manager of Liverpool FC?")
    userInput = input()
    if (userInput.lower() == "Jurgen Klopp".lower()):
        print("That is correct!")
        print("-------------------------------")
        score +=1

    else:   
        print("Sorry, the correct answer is Jurgen Klopp.")
        print("-------------------------------")
    
    
    print(f"Thanks for playing {username}, your final score was {score}")

    score_sheet = SHEET.worksheet("football")
    score_sheet.append_row([username, score])

    print("-----------------------------")
    print("----------Highscores---------")
    print("-----------------------------\n")
    highscores = score_sheet.get_all_values()
    pprint(highscores)

def music_quiz():
    """
    This function will be the music quiz, this will ask the
    user 10 questions and then tell them their final score.
    Then add their highscores to the Quiz_Scores Google spreadsheet
    and relay the highscore table back to them
    """
    username = get_user_name()
    print("Welcome to the Music Quiz!\n")
    score = 0
    print("Question 1 \n")
    print("What band wrote 'Let it be?'")
    userInput = input()
    if (userInput.lower() == "The Beatles".lower()):
        print("That is correct!")
        print("-------------------------------")
        score +=1

    else:   
        print("Sorry, the correct answer is The Beatles.")
        print("-------------------------------")

    print("Question 2 \n")
    print("What is the name of the sold album of all time?")
    userInput = input()
    if (userInput.lower() == "Thriller".lower()):
        print("That is correct!")
        print("Thriller by Michael Jackson has sold 27 million vinyls")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Portugal.")
        print("Thriller by Michael Jackson has sold 27 million vinyls")
        print("-------------------------------")

    print("Question 3 \n")
    print("What band tragically died in Sweden in 2016?")
    userInput = input()
    if (userInput.lower() == "Viola Beach".lower()):
        print("That is correct!")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Viola Beach.")
        print("-------------------------------")
    
    print("Question 4 \n")
    print("Finish the song name 'Mr Blue ...' .")
    userInput = input()
    if (userInput.lower() == "Sky".lower()):
        print("That is correct!")
        print("Mr Blue Sky by Jeff Lynn's ELO")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Sky.")
        print("Mr Blue Sky by Jeff Lynn's ELO")
        print("-------------------------------")
    
    print("Question 5 \n")
    print("What song has been streamed the most (as of march 2023)?")
    userInput = input()
    if (userInput.lower() == "Blinding Lights".lower()):
        print("That is correct!")
        print("Blinding Lights by The Weekend.")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Blinding Lights.")
        print("-------------------------------")
    
    print("Question 6 \n")
    print("Who had won the most Grammy awards?")
    userInput = input()
    if (userInput.lower() == "Beyonce".lower()):
        print("That is correct!")
        print("-------------------------------")
        score +=1
    else:   
        print("Sorry, the correct answer is Beyonce.")
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

    score_sheet = SHEET.worksheet("general")
    score_sheet.append_row([username, score])

    print("-----------------------------")
    print("----------Highscores---------")
    print("-----------------------------\n")
    highscores = score_sheet.get_all_values()
    pprint(highscores)




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
        print("music quiz")
        break
    else:
        print(f"{userInput} is an invalid choice, please try again\n")




