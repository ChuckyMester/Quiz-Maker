import sqlite3


class CreateTable():

    # Connecting to database
    connect = sqlite3.connect('quiz.db')
    cursor = connect.cursor()

    # Creating the table
    cursor.execute('''CREATE TABLE IF NOT EXISTS questions
                (id INTEGER PRIMARY KEY, question TEXT, answerA TEXT, answerB TEXT, answerC TEXT, answerD TEXT, correctAnswer TEXT)''')

    # Close connection
    connect.close