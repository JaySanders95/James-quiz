# James' Quiz
![](../James-quiz/images/am-i-responsive.png)
James' quiz is an interactive terminal quiz, it presents the user with 10 questions. If they answer a question correct, their score increases by one. When the game is finished the user is presented with their final score, then presented with the recent player scores. The user has the chance to choose 1 of 3 quizzes, the choices are general knowledge, football and music.
Each individual quiz has their respective recent scores which is set on a Google Spreadsheet called Quiz_Scores, these are 3 individual sheets called "general", "football" & "music".
The quiz resides within 4 functions, once a quiz is selected by typing, it will call the appropriate quiz by their function. During this function it will call the get username function, which will obtain the users name and then proceed with the quiz.


## How to play
- This quiz is relatively simple to start, following the on screen instructions will allow the user to choose what quiz they would like. Once one has been typed into the console and selected, the terminal will ask the user for their name and then it will generate 10 pre-written questions.
- The scores are recorded and all previous scores are relayed back to the current user.
![](../James-quiz/images/intro.png)

## Choose a name
- When the user has selected a quiz (general, music, football) they are asked to give a name. This is for 2 reasons, so when the user is starting their quiz and finishing it, this data will be used to add interactivity. ("Let's get started 'name'" & "thanks for playing 'name'") but more importantly, this is used to record their score to an external spreadsheet for the 'recent scores' at the end of the quiz, it will record the data with their score and relay the score back to the user in a tuple ['name','score'].

## Quiz
![](../James-quiz/images/footballquiz.png)
- The quiz will load questions one at a time, some questions have extra explanation for the answer.
- Every question that is answered correctly will increment the score by 1, which will be presented to the user at the end in the form of an F string, which will print "thanks for playing (the name the user chose at the start), your final score was (the score variable and the incremented result).
- This quiz was constructed using a data input with the .capitalize() to ensure that as long as the correct answer is answered it will allow it, checking the data against the correct answer using '==', within the if statement, if they typed the correct answer the score variable will be incremented by 1 and they will be greeted with a print statement confirming they have the correct answer. If they entered an incorrect answer, they will be told the correct answer and within some questions both a correct and incorrect answer will yield a brief comment on the answer. As seen in picture below.
![](../James-quiz/images/extra-information-answer.png)

## End of game / recent scores

- This is displayed at the bottom of the terminal, it will display the user's chosen name and their final score. Then the terminal will print the recent scores from previously played games.
- The information is initially appended to a Google spreadsheet called "Quiz-Scores", it will check the correct individual sheet based on what test they have taken, append the data into the spreadsheet and return all of the values to the bottom of the terminal.
![](../James-quiz/images/Test-spreadsheet.png)
![](../James-quiz/images/spreadsheet-test.png)


## Testing
- I have manually tested my code through the CI linter at https://pep8ci.herokuapp.com/# and there are no issues with the code.
- I have tested my code through the Git terminal and found all 3 tests run correctly, all 3 send the correct data to the correct page and all 3 relay the correct information back to the user.
- I have tested my code through the Heroku online terminal and found all 3 tests run correctly, all 3 send the correct data to the correct page and all 3 relay the correct information back to the user.

## Linking Google Spreadsheet
- The google spreadsheet was an important part of the project, data was needed to be relayed from an API sheet back and forth to the terminal. I created a google spreadsheet and named it relevant to the project, which was "Quiz_Scores".
- Once i had configued the credentials on googles API library using the Code institute guide from Love Sandwiches, i had taken the code from the Love Sandwiches project, amended it and placed it into my project. This allowed me to access the spreadsheet from my terminal.
![](../James-quiz/images/sheets.png)

## Key project goals
- The desired outcome of this project was to create a simple quiz for the user to enjoy. I had intended to further this project by sorting the data received from the recent scores; which would sort them from highest score to lowest score, creating a leaderboard. However, for this i needed to enable API scripts and this was far too advanced and was worried that this would complicate and break my code.
- The picture below shows my intentions for continuing with this script.
![](../James-quiz/images/scripts.jpg)


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
![](../James-quiz/images/linter.png)


The link for my Heroku terminal is here: https://james-quiz.herokuapp.com/

## Credits
- Re-used code the example project Love Sandwiches,  This was only basic code to link the google worksheet to my project and to also. This includes the scope and import code.
- The remainder of the code is all of my own.
