import customtkinter as ctk
from database import CreateTable
from tkinter import Toplevel, Menu
from tkinter import ttk


class QuizApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window properties
        self.geometry('600x400')
        self.title('Quiz App')

         # Menu
        self.menubar = Menu(self)
        self.config(menu=self.menubar)

        # Database connection
        tc = CreateTable()

        # Question label
        self.mode_label = ctk.CTkLabel(self, text='Choose a mode', font=('Arial', 20))
        self.mode_label.pack(pady=20)

        # Buttons
        self.buttons_frame = ctk.CTkFrame(self)
        self.buttons_frame.place(relwidth=0.75, relheight=0.6, relx=0.5, rely=0.5, anchor='center')

        self.new_game_button = ctk.CTkButton(self.buttons_frame, text="New game", width=150, height=60, command=lambda: print('hello'))
        self.new_game_button.place(relx=0.25, rely=0.25, anchor='center')

        self.manage_questions_button = ctk.CTkButton(self.buttons_frame, text="Manage questions", width=150, height=60, command=self.open_manage_questions)
        self.manage_questions_button.place(relx=0.75, rely=0.25, anchor='center')

        self.view_scores_button = ctk.CTkButton(self.buttons_frame, text="Scores", width=150, height=60, command=lambda: print('hello'))
        self.view_scores_button.place(relx=0.25, rely=0.75, anchor='center')

        self.settings_button = ctk.CTkButton(self.buttons_frame, text="Beállítások", width=150, height=60, command=lambda: print('hello'))
        self.settings_button.place(relx=0.75, rely=0.75, anchor='center')

        # Run
        self.mainloop()


    # Manage questions window
    def open_manage_questions(self):
        
        # Hide the main window
        self.withdraw()

        # Creating the new window
        manage_questions_window = Toplevel()
        manage_questions_window.geometry('1000x430')
        manage_questions_window.minsize(width=1000, height=430)
        manage_questions_window.title('Manage questions')

        # Question entry
        question_entry = ctk.CTkEntry(manage_questions_window, placeholder_text="Írja be a kérdést itt", width=400)
        question_entry.pack(pady=(20, 20))

        # Answer frame
        answers_frame = ctk.CTkFrame(manage_questions_window)
        answers_frame.pack(pady=(0, 20))

        # Answers entry
        self.answer_entries = []
        for i in range(4):
            entry = ctk.CTkEntry(answers_frame, placeholder_text=f"Válasz {i+1}", width=200)
            entry.grid(row=i//2, column=i%2, padx=10, pady=10)
            self.answer_entries.append(entry)

        # Helyes válasz kiválasztása legördülő menüvel
        correct_answer_label = ctk.CTkLabel(manage_questions_window, text="Helyes válasz:")
        correct_answer_label.pack(pady=(0, 5))

        self.correct_answer_var = ctk.StringVar()
        correct_answer_combobox = ttk.Combobox(manage_questions_window, textvariable=self.correct_answer_var, values=["Válasz 1", "Válasz 2", "Válasz 3", "Válasz 4"], state="readonly", width=30)
        correct_answer_combobox.pack(pady=(0, 20))

        # Back to main menu button
        close_button = ctk.CTkButton(manage_questions_window, text="Go back", width=80, command=lambda: self.close_and_show(manage_questions_window))
        close_button.place(relx=0.03, rely=0.97, anchor='sw')


    # Close window and go back to main menu
    def close_and_show(self, new_window):

        # Close the currently opened window
        new_window.destroy()
        # Show the main window
        self.deiconify()


        


app = QuizApp()