from tkinter import Tk, Frame, Label, Canvas, PhotoImage, Button
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quizzing It Up")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.resizable(width=True, height=True)
        self.window.config(height=250,width=300)
        self.score_label = Label( text="Score: 0",fg= "white" , bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.canvas = Canvas(self.window,width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 15, "bold"),
            width=280,
        )
        self.canvas.grid(pady=50,row=1,column=0, columnspan=2)
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,highlightthickness = 0)
        self.true_button.grid(row=2,column=1)
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image,highlightthickness = 0)
        self.false_button.grid(row=2,column=0)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
