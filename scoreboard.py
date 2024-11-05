from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font = ("Ariel", 24, "normal"))
        self.hideturtle()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", align="center", font=("Ariel", 24, "normal"))


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode ="w") as file:
              file.write(f"{self.highscore}")
        self.score = 0
        self.increase_score()
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Ariel", 24, "normal"))



