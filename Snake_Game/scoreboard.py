from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 260)
        self.color('white')
        self.scorechange()
        self.hideturtle()

    def scorechange(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    
    def clearscore(self):
        self.score += 1
        self.clear()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)