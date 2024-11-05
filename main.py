from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Tanvir's snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() <-280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        snake.reset()
        score.reset()


    for segments in snake.segments[1:]:
        # if segments == snake.segments[0]:
        #     pass
        if snake.segments[0].distance(segments) < 10:
            snake.reset()
            score.reset()

screen.exitonclick()













screen.exitonclick()

