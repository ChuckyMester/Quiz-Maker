import sqlite3


class CreateTable():
    
    # Init method
    def __init__(self):

        # Connecting to database
        self.connect = sqlite3.connect('quiz.db')
        self.cursor = self.connect.cursor()

        # Creating the table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS questions
                    (id INTEGER PRIMARY KEY, question TEXT, answer1 TEXT, answer2 TEXT, answer3 TEXT, answer4 TEXT, correct_answer TEXT)''')
        
        # Save the changes
        self.connect.commit()

        # Close connection
        self.connect.close()


    # Question insert method
    def insert_question(self, question, answer1, answer2, answer3, answer4, correct_answer):
        connect = sqlite3.connect('quiz.db')
        cursor = connect.cursor()

        cursor.execute("INSERT INTO questions (question, answer1, answer2, answer3, answer4, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
          (question, answer1, answer2, answer3, answer4, correct_answer))
        
        # Save the changes
        connect.commit()
        
        # Close connection
        connect.close()


    # Fetching questions
    def fetch_questions(self):
        
        # Creating connection
        conn = sqlite3.connect('quiz.db')
        cursor = conn.cursor()

        # SQL command
        cursor.execute('''SELECT id, question, answer1, answer2, answer3, answer4, correct_answer FROM questions''')

        # Adding all the questions to a list
        questions_list = []
        for row in cursor.fetchall():
            question_id, question_text, answer1, answer2, answer3, answer4, correct_answer = row
            question_dict = {
                "id": question_id,
                "question": question_text,
                "answers": [answer1, answer2, answer3, answer4],
                "correct_answer": correct_answer
            }
            questions_list.append(question_dict)
        
        # Closing connection
        conn.close()
        
        # Returning the question list
        return questions_list
