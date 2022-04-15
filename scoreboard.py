from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 270)
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # reset and check for high scores
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        # writes current high score to data.txt to save high score
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
