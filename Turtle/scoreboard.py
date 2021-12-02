from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=250)
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level {self.level}", False, align='center', font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game over.", False, align='center', font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()