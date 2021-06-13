from turtle import Turtle, Screen
import random

# initialize screen
screen = Screen()
game_on = False

# user guesses a winner
guess = screen.textinput("GUESS THE WINNER", "Who Do you think will win: ")

game_on = True

# initialize players/ position / color
colors = ["red", 'green', 'purple', "yellow", "orange", "blue"]
y_pos = [-100, -50, 0, 50, 100, 150]
all_players = []
for player in range(6):
    new_player = Turtle()
    new_player.shape("turtle")
    new_player.color(colors[player])
    new_player.penup()
    new_player.goto(x=-320, y=y_pos[player])
    new_player.pendown()
    all_players.append(new_player)

# generates a random amount to move thew player

winning_position = (310.00)

while game_on:
    for turtle in all_players:
        if turtle.xcor() >= winning_position:
            game_on = False
            print(f"{turtle.pencolor()} is the winner")
            if guess == turtle.pencolor():
                print("You Guessed Right")
            else:
                print("Sorry your guess was incorrect")
        move = random.randint(1, 10)
        turtle.fd(move)

screen.exitonclick()
