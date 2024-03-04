import sqlite3

connection = sqlite3.connect('FridayProj5.db')
cursor = connection.cursor()

def returnQuestions():
    cursor.execute('select * from QUESTANS')
    return cursor.fetchall()

questionBank = returnQuestions()

correct = 0
incorrect = 0

print('Lets start the game.')

for row in questionBank:
    question = row[1]
    answer = row[2]

    print(question)
    user_answer = input('ANSWER: ')

if user_answer() == answer():
    print('That is correct!')
    correct += 1

else:
    print('That is incorrect!')
    incorrect += 1

print('Final results:', correct, "/", incorrect)