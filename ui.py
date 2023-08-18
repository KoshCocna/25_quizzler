from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzlerInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text="score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 16))
        self.score.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quiz_text = self.canvas.create_text(150,
                                                 125,
                                                 text="quiz here...",
                                                 fill=THEME_COLOR,
                                                 width=250,
                                                 font=("Arial", 16, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.trueImg = PhotoImage(file="images/true.png")
        self.trueBtn = Button(image=self.trueImg, highlightthickness=0, command=self.pressedTrue)
        self.trueBtn.grid(row=2, column=0)

        self.falseImg = PhotoImage(file="images/false.png")
        self.falseBtn = Button(image=self.falseImg, highlightthickness=0, command=self.pressedFalse)
        self.falseBtn.grid(row=2, column=1)
        self.get_next_quiz()

        self.window.mainloop()

    def get_next_quiz(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You have done the quiz game!")
            self.trueBtn.config(state="disabled")
            self.falseBtn.config(state="disabled")

    def pressedTrue(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def pressedFalse(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_quiz)
