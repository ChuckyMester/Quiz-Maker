import customtkinter as ctk
from database import CreateTable
from tkinter import Toplevel, Menu


class QuizApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window properties
        self.geometry('600x400')
        self.title('Quiz App')

         # Menu
        self.menubar = Menu(self)
        self.config(menu=self.menubar)

        self.menubar.add_command(label='Add new question', command=self.add_new_question)

        # Database connection
        tc = CreateTable()

        # Question label
        self.question_label = ctk.CTkLabel(self, text='Place for the question', wraplength=500)
        self.question_label.pack(pady=20)

        # Answer Buttons
        self.answer_buttons = []

        # Run
        self.mainloop()

    
    # New question window
    def add_new_question(self):
        self.question_window = Toplevel(self)
        self.question_window.title('Add question')
        self.question_window.geometry('600x400')

        # Question entry
        self.question_entry = ctk.CTkEntry(self.question_window, placeholder_text="Question")
        self.question_entry.pack(pady=10)

        # Answers
        self.answer_entry = []
        for i in range(4):
            entry = ctk.CTkEntry(self.question_window, placeholder_text=f"Answer {i+1}")
            entry.pack(pady=5)
            self.answer_entry.append(entry)

        # Correct Answer
        self.correct_answer_combobox = ctk.CTkComboBox(self.question_window, values=["A", "B", "C", "D"])
        self.correct_answer_combobox.pack(pady=10)

        # Handling the data
        answers = [entry.get() for entry in self.answer_entry]
        correct_answer_letter = self.correct_answer_combobox.get()

        # Add Button
        self.hozzaad_gomb = ctk.CTkButton(self.question_window, text="Add", command=lambda: self.handling_question_data())
        self.hozzaad_gomb.pack(pady=10)


    def handling_question_data(self):
        question = self.question_entry.get()
        answers = [entry.get() for entry in self.answer_entry]
        correct_answer_letter = self.correct_answer_combobox.get()

        print("Question:", question)
        print("Answers:", answers)
        print("Correct answer:", correct_answer_letter)

        


app = QuizApp()