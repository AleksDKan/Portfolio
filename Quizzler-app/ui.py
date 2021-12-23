from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question text", \
                                                     font=("Arial",
                                                           20,
                                                           "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 15))
        self.score.grid(row=0, column=1, pady=20)

        yes_image = PhotoImage(file="images/true.png")
        self.yes_button = Button(image=yes_image, highlightthickness=0,
                                 command=self.yes_pressed)
        self.yes_button.grid(row=2, column=0)
        no_image = PhotoImage(file="images/false.png")
        self.no_button = Button(image=no_image, highlightthickness=0, command=self.no_pressed)
        self.no_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")

    def yes_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.window.after(1000, self.get_next_question)

    def no_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        self.window.after(1000, self.get_next_question)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="#B1DDC6")
        else:
            self.canvas.configure(bg="red")

