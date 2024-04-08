import customtkinter as ctk
from database import CreateTable
from tkinter import ttk
import random


class QuizApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window properties
        self.geometry('600x400')
        self.title('Quiz App')

        # Database connection
        self.connected_database = CreateTable()
        
        # Game mode variable
        self.game_mode = '10' # Basic gamemode with 10 questions

        # Question label
        self.mode_label = ctk.CTkLabel(self, text='Choose a mode', font=('Arial', 20))
        self.mode_label.pack(pady=20)

        # Buttons
        self.buttons_frame = ctk.CTkFrame(self)
        self.buttons_frame.place(relwidth=0.75, relheight=0.6, relx=0.5, rely=0.5, anchor='center')

        self.new_game_button = ctk.CTkButton(self.buttons_frame, text="New game", width=150, height=60, command=self.new_game)
        self.new_game_button.place(relx=0.25, rely=0.25, anchor='center')

        self.manage_questions_button = ctk.CTkButton(self.buttons_frame, text="Manage questions", width=150, height=60, command=self.open_manage_questions)
        self.manage_questions_button.place(relx=0.75, rely=0.25, anchor='center')

        self.view_scores_button = ctk.CTkButton(self.buttons_frame, text="Scores", width=150, height=60, command=lambda: print('hello'))
        self.view_scores_button.place(relx=0.25, rely=0.75, anchor='center')

        self.settings_button = ctk.CTkButton(self.buttons_frame, text="Game mode", width=150, height=60, command=self.game_mode_selection)
        self.settings_button.place(relx=0.75, rely=0.75, anchor='center')

        # Run
        self.mainloop()


    # Manage questions window
    def open_manage_questions(self):
        
        # Hide the main window
        self.withdraw()

        # Creating the new window
        manage_questions_window = ctk.CTkToplevel()
        manage_questions_window.geometry('800x400')
        manage_questions_window.minsize(width=800, height=400)
        manage_questions_window.title('Manage questions')

        # If the user closes this toplevel window
        manage_questions_window.protocol("WM_DELETE_WINDOW", self.on_close)

        # Question entry
        self.question_entry = ctk.CTkEntry(manage_questions_window, placeholder_text="Írja be a kérdést itt", width=400)
        self.question_entry.pack(pady=(20, 20))

        # Answer frame
        answers_frame = ctk.CTkFrame(manage_questions_window)
        answers_frame.pack(pady=(0, 20))

        # Answers entry
        self.answer_entries = []
        for i in range(4):
            entry = ctk.CTkEntry(answers_frame, placeholder_text=f"Válasz {i+1}", width=200)
            entry.grid(row=i//2, column=i%2, padx=10, pady=10)
            self.answer_entries.append(entry)

        # Choose the correct answer combobox
        correct_answer_label = ctk.CTkLabel(manage_questions_window, text="Helyes válasz:")
        correct_answer_label.pack(pady=(0, 5))

        self.correct_answer_combobox = ctk.CTkComboBox(manage_questions_window, values=["Válasz 1", "Válasz 2", "Válasz 3", "Válasz 4"], state="readonly")
        self.correct_answer_combobox.pack(pady=(0, 20))

        add_question_button = ctk.CTkButton(manage_questions_window, text="Add question to database", command=self.add_question_to_database, width=120, height=40)
        add_question_button.pack(pady=20)

        # Back to main menu button
        close_button = ctk.CTkButton(manage_questions_window, text="Go back", width=80, command=lambda: self.close_and_show(manage_questions_window))
        close_button.place(relx=0.03, rely=0.97, anchor='sw')


    def add_question_to_database(self):
        # Collecting the data from all entry field
        question_text = self.question_entry.get()
        answers = [entry.get() for entry in self.answer_entries]
        correct_answer = self.correct_answer_combobox.get()

        # Input check
        if not question_text or not all(answers) or not correct_answer:
            print("Missing Data!")
            return

        # Adding entries to the database
        _, correct_num = correct_answer.split(' ')
        correct_answer = answers[int(correct_num) - 1]

        self.connected_database.insert_question(question_text, *answers, correct_answer)


        # Reset all field for new inputs
        self.question_entry.delete(0, 'end')
        for entry in self.answer_entries:
            entry.delete(0, 'end')
        self.correct_answer_combobox.set('')


    # Game mode selection window
    def game_mode_selection(self):

        # Hide the main window
        self.withdraw()

        # Creating the new window
        game_mode_window = ctk.CTkToplevel()
        game_mode_window.geometry('600x400')
        game_mode_window.minsize(width=600, height=400)
        game_mode_window.title('Select game mode')

        # If the user closes this toplevel window
        game_mode_window.protocol("WM_DELETE_WINDOW", self.on_close)

        # Question label
        game_mode_label = ctk.CTkLabel(game_mode_window, text='Choose a game mode', font=('Arial', 20))
        game_mode_label.pack(pady=20)

        # Buttons
        buttons_frame = ctk.CTkFrame(game_mode_window)
        buttons_frame.place(relwidth=0.75, relheight=0.6, relx=0.5, rely=0.5, anchor='center')

        mode1_button = ctk.CTkButton(buttons_frame, text="10 questions", width=150, height=60, command=lambda: self.game_mode_setter('10', game_mode_window))
        mode1_button.place(relx=0.25, rely=0.25, anchor='center')

        mode2_button = ctk.CTkButton(buttons_frame, text="20 questions", width=150, height=60, command=lambda: self.game_mode_setter('20', game_mode_window))
        mode2_button.place(relx=0.75, rely=0.25, anchor='center')

        mode3_button = ctk.CTkButton(buttons_frame, text="30 questions", width=150, height=60, command=lambda: self.game_mode_setter('30', game_mode_window))
        mode3_button.place(relx=0.25, rely=0.75, anchor='center')

        mode4_button = ctk.CTkButton(buttons_frame, text="Extreme", width=150, height=60, command=lambda: self.game_mode_setter('xtreme', game_mode_window))
        mode4_button.place(relx=0.75, rely=0.75, anchor='center')

        # Back to main menu button
        close_button = ctk.CTkButton(game_mode_window, text="Go back", width=80, command=lambda: self.close_and_show(game_mode_window))
        close_button.place(relx=0.03, rely=0.97, anchor='sw')


    # New Game window
    def new_game(self):
    
        # Hide the main window
        self.withdraw()

        # Creating the new window
        game_mode_window = ctk.CTkToplevel()
        game_mode_window.geometry('600x400')
        game_mode_window.minsize(width=600, height=400)
        game_mode_window.title('Quiz')

        # If the user closes this toplevel window
        game_mode_window.protocol("WM_DELETE_WINDOW", self.on_close)

        question_list = self.connected_database.fetch_questions()
        self.questions = None

        # Questions indexing
        self.current_question_index = 0

        # Show the first question
        self.next_question() # TODO: Implement the function

        # Checking game mode
        match self.game_mode:

            # 10 questions mode
            case '10':
                self.questions = random.sample(question_list, 10)
                print(len(self.questions))

            # 20 questions mode
            case '20':
                self.questions = random.sample(question_list, 20)
                print(len(self.questions))

            # 30 questions mode
            case '30':
                self.questions = random.sample(question_list, 30)
                print(len(self.questions))

            # Extreme mode
            case 'xtreme':
                random_questions = random.sample(question_list, 30)

        # Back to main menu button
        close_button = ctk.CTkButton(game_mode_window, text="Go back", width=80, command=lambda: self.close_and_show(game_mode_window))
        close_button.place(relx=0.03, rely=0.97, anchor='sw')


    # Game mode setter
    def game_mode_setter(self, mode, window):
        self.game_mode = mode
        
        # Go back to main menu after choosing the game mode
        self.close_and_show(window)


    # Close window and go back to main menu
    def close_and_show(self, new_window):

        # Close the currently opened window
        new_window.destroy()
        # Show the main window
        self.deiconify()

    
    # Close the application where the user exits a toplevel window
    def on_close(self):

        # Close the application
        self.destroy()


        


app = QuizApp()