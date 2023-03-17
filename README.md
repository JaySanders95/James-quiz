# James' Quiz
![](James-quiz/assets/images/am-i-responsive.png)
![Am i responsive](James-quiz/assets/images/am-i-responsive.png)
James' quiz is an interactive terminal quiz, it presents the user with 10 questions. If they answer a question correct, their score increases by one. When the game is finished the user is presented with their final score, then presented with the recent player scores. The user has the chance to choose 1 of 3 quizzes, the choices are general knowledge, football and music.
Each individual quiz has their respective recent scores which is set on a Google Spreadsheet called Quiz_Scores, these are 3 individual sheets called "general", "football" & "music".
The quiz resides within 4 functions, once a quiz is selected by typing, it will call the appropriate quiz by their function. During this function it will call the get username function, which will obtain the users name and then proceed with the quiz.


## How to play
- This quiz is relatively simple to start, following the on screen instructions will allow the user to choose what quiz they would like. Once one has been typed into the console and selected, the terminal will ask the user for their name and then it will generate 10 pre-written questions.
- The scores are recorded and all previous scores are relayed back to the current user.
![](../James-quiz/assets/images/intro.png)

## Choose a name
- When the user has selected a quiz (general, music, football) they are asked to give a name. This is for 2 reasons, so when the user is starting their quiz and finishing it, this data will be used to add interactivity. ("Let's get started 'name'" & "thanks for playing 'name'") but more importantly, this is used to record their score to an external spreadsheet for the 'recent scores' at the end of the quiz, it will record the data with their score and relay the score back to the user in a tuple ['name','score'].

## Quiz
![](../James-quiz/assets/images/footballquiz.png)
- The quiz will load questions one at a time, some questions have extra explanation for the answer.
- Every question that is answered correctly will increment the score by 1, which will be presented to the user at the end in the form of an F string, which will print "thanks for playing (the name the user chose at the start), your final score was (the score variable and the incremented result).
- This quiz was constructed using a data input with the .capitalize() to ensure that as long as the correct answer is answered it will allow it, checking the data against the correct answer using '==', within the if statement, if they typed the correct answer the score variable will be incremented by 1 and they will be greeted with a print statement confirming they have the correct answer. If they entered an incorrect answer, they will be told the correct answer and within some questions both a correct and incorrect answer will yield a brief comment on the answer. As seen in picture below.
![](../James-Quiz/assets/images/extra-information-answer.png)

## End of game / recent scores

- This is displayed at the bottom of the terminal, it will display the user's chosen name and their final score. Then the terminal will print the recent scores from previously played games.
- The information is initially appended to a Google spreadsheet called "Quiz-Scores", it will check the correct individual sheet based on what test they have taken, append the data into the spreadsheet and return all of the values to the bottom of the terminal.
![](../James-quiz/assets/images/Test-spreadsheet.png)
![](../James-quiz/assets/images/spreadsheet-test.png)

## Restart game
- When the game has ended the user is asked "would you like to play again(Y/N)", when they type Y, the game loops and restarts.
- If the user enters "N", they are greeted with a "Thanks for playing" message.
- If the user enters anything other than Y/N, they are notified that they have entered an invalid character and the game will end.
![](../James-quiz/assets/images/play-again1.png)
![](../James-quiz/assets/images/play-again2.png)

## Testing
- I have manually tested my code through the CI linter at https://pep8ci.herokuapp.com/# and there are no issues with the code.
- I have tested my code through the Git terminal and found all 3 tests run correctly, all 3 send the correct data to the correct page and all 3 relay the correct information back to the user.
- I have tested my code through the Heroku online terminal and found all 3 tests run correctly, all 3 send the correct data to the correct page and all 3 relay the correct information back to the user.

Here is the breakdown of the complete testing of this project.
-  The google sheets API
- - This was tested rigorously throughout the entire project. When first added to the project, this was tested by inputting data manually to the spreadsheet and printing the data to the console.
- - Throughout the project i would always test to ensure data was being recorded correctly.
- - At the end of the project i added the return of the data in the highscores, this was tested to ensure the data returned correctly and it was returned with its correct output i.e Name : score.
- Obtaining the users name
- - The testing for this occured by simply using an input option first, then printing the data to the console. Then this was tested to ensure the value received from the input was logged to a variable.
- - This was then tested to ensure that invalid characters could not be entered. ensuring that no whitespace could be entered i amended a try/except statement to the code. Then i proceeded to test whitespace singular and whitespace multiple entries and it would always throw an error if it is left blank.
- Quiz testing
- - As the code for the 3 separate tests is near identical. I thoroughly tested a single quiz for errors, then copied the same code into the other two.
- - First i had to test whether the username variable was being read by the function, i did this by assigning the get_user_name function to a variable and print the username within an f string, this would test whether the entered username was being printed inside this function.
- - Once this was completed i had to test the users input for the answers during the quiz. I had to ensure that the answers they provide aren't capital sensitive, so by adding the .lower() to the input if statement this ensured that the answer would still be correct if entered capitalised or not.
- - Once i had written the lower(), i needed to test whether this was working correctly, so i added the variable score and had an incrementation for every correct answer. I would run the function and enter the correct answer with a capital letter at the start and without a capital letter at the start and both of these returned the score variable printed 1. Then i had to test whether or not it was incrementing with any answer given, i entered an incorrect answer and printed score again and it returned the score of 0.
- - Once i had completed this and written all 10 questions, i had to test each question individually to ensure the scores were incrementing for correct answers, so at the end of the questions i printed the score variable and ran the quiz at least 30 times, purposely answering incorrect on some to test whether it was correctly calculating the score.
- - Once i was happy with the score variable, i wrote it into an F string with the username variable and tested whether at the end it would correctly display the intended message "Thanks for playing (name) your score was (final score).
- - Once this was completed, i needed to ensure the data from the quiz was being recorded into the spreadsheet, so i completed the quiz numerous times with different names, obtaining different scores and was checking the spreadsheet after every quiz. This was recording data correctly and once i had completed all 3 quizzes, i tested to ensure that the correct quiz was saving the scores into the correct sheet.
- - After the quiz has ended and the scores are displayed back to the user, i had to ensure the correct data was being fed back to the user. I ran all 3 quizzes and entered dummy data into the spreadsheet, cross-checking the returned results into the terminal.
- - I also tested that the data was being displayed in a column, so i would run the quiz and test the recent scores output to the console to see if the data was being displayed in a column.
- Play again function
- - Once the quiz has ended, the user is asked whether they would like to play again (Y/N), this code is called at the end of all 3 quizzes and similarly to the quiz questions, i had to ensure that it did not matter whether they entered 'y' or 'Y'. I did this by adding .lower() again to the if statement and elif. I tested this on all 3 quizzes and all 3 allowed the user to play the game again.
- - After testing Y, i tested N, this worked as well with no issues.
- - If a user enters anything other than Y or N, the game will close automatically.

- Choose quiz function
- - The choose quiz function runs similarly to the Y/N function, this will give the user 3 separate options to choose from and there is no difference whether the option entered is capitalized. The only difference is that when a valid input is entered. The function breaks and allows the user to continue. If something other than the correct options are entered, the function will run indefinitely until one is selected.
- - I tested this by typing general without capitalization/with capitalization to see if it runs nicely, if this accepted the input the print statement would say a random string "djkwjwdk" and break. I then tested with invalid inputs and it would only break the function if one of the correct options was entered. 
- - Once a correct option is entered; a function is called depending on the string entered; i tested all 3 of these by individually entering the input, running through the code, selecting Y/y and then entering another valid input. I tested this multiple times for all 3 of the inputs.

## Linking Google Spreadsheet
- The google spreadsheet was an important part of the project, data was needed to be relayed from an API sheet back and forth to the terminal. I created a google spreadsheet and named it relevant to the project, which was "Quiz_Scores".
- Once i had configued the credentials on googles API library using the Code institute guide from Love Sandwiches, i had taken the code from the Love Sandwiches project, amended it and placed it into my project. This allowed me to access the spreadsheet from my terminal.
![](../James-quiz/assets/images/sheets.png)

## Key project goals
- The desired outcome of this project was to create a simple quiz for the user to enjoy. I had intended to further this project by sorting the data received from the recent scores; which would sort them from highest score to lowest score, creating a leaderboard. However, for this i needed to enable API scripts and this was far too advanced and was worried that this would complicate and break my code.
- The picture below shows my intentions for continuing with this script.
![](../James-quiz/assets/images/scripts.jpg)


## Bugs
Solved bugs
- When the user entered a blank name into the terminal at the start, this was allowed and played with an empty string. I fixed this by adding a while loop, the while loop checks for an empty string and will loop until a username is given. As the terminal is asking for a username, it will allow letters and numbers.
- When the user was selecting a quiz, if they had entered something other than the 3 options, it would close the terminal and end the program rather than looping until one of the 3 are entered. This was fixed by adding a while loop to this code, and therefore would loop until the True statement is met.
Remaining Bugs
- There are no known bugs in this project.

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.
- The deployment process was taken from the example project "Love Sandwiches", i followed all steps which were taken.
- - Created requirements.txt from terminal by entering freeze method "pip3 freeze > requirements.txt".
- - After this i created a new app on Heroku, copy/pasted the config vars from cred.json into the key/value inputs.
- - Added buildpacks in the order: Python, nodejs.
- - Connected Heroku to my Git respository and then manually deployed the branch.
![](./James-quiz/assets/images/linter.png)


The link for my Heroku terminal is here: https://james-quiz.herokuapp.com/

## Credits
- Re-used code the example project Love Sandwiches,  This was only basic code to link the google worksheet to my project and to also. This includes the scope and import code.
- The remainder of the code is all of my own.
