from tkinter import *
from quiz_game.quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Interface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0, bd=0)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.true = PhotoImage(file="quiz_game/images/true.png")
        self.false = PhotoImage(file="quiz_game/images/false.png")
        self.score = 0
        self.answer: bool

        # 1 Label 2 Button
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.score_label = Label(
            text=f"Score: {self.score}",
            bg=THEME_COLOR,
            fg="white",
            bd=0,
            font=("Arial", 14)
        )
        self.tick_button = Button(image=self.true, bd=0, highlightthickness=0, command=self.check_true_answer)
        self.wrong_button = Button(image=self.false, bd=0, highlightthickness=0, command=self.check_false_answer)

        self.score_label.grid(row=0, column=1)
        self.tick_button.grid(row=2, column=0)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.button_state(ACTIVE)
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.button_state(DISABLED)
            self.canvas.itemconfig(self.question_text, text="You have completed the quiz!")

    def check_true_answer(self):
        self.answer = self.quiz.check_answer("True")
        self.feedback()

    def check_false_answer(self):
        self.answer = self.quiz.check_answer("False")
        self.feedback()

    def feedback(self):
        self.button_state(DISABLED)
        if self.answer:
            self.canvas.config(bg="green")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(ms=1000, func=self.get_next_question)

    def button_state(self, state: str):
        self.tick_button.config(state=state)
        self.wrong_button.config(state=state)

