print("WELCOME TO ROCK PAPER SCISSORS GAME")
import tkinter as tk
import random


print("Rule of the game\nRock vs Paper->Paper Win\nRock vs Scissor->Rock Win\nPaper vs Scissors->Scisssors Win\n") 
total_games = 0
player_wins = 0
computer_wins = 0

def determine_winner(user_choice):
    global total_games, player_wins, computer_wins
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    total_games += 1
    
    if user_choice == computer_choice:
        result = f"Both players selected {user_choice}. It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = f"You win! {user_choice} beats {computer_choice}."
        player_wins += 1
    else:
        result = f"You lose! {computer_choice} beats {user_choice}."
        computer_wins += 1
        
    label_result.config(text=result)
    label_stats.config(text=f"Games played: {total_games} | Player wins: {player_wins} | Computer wins: {computer_wins}")


def play_game():
    user_choice = var.get()
    determine_winner(user_choice)


window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("400x400")


var = tk.StringVar()
var.set("Rock")

choices = ["Rock", "Paper", "Scissors"]
for choice in choices:
    radio = tk.Radiobutton(window, text=choice, variable=var, value=choice)
    radio.pack(anchor=tk.W)

button_play = tk.Button(window, text="Play", font=20, width=20, bg="light blue", command=play_game)
button_play.pack()

label_result = tk.Label(window, text="", font=20, width=35, fg="red", pady=40)
label_result.pack()

label_stats = tk.Label(window, text="Games played: 0 | Player wins: 0 | Computer wins: 0", width=80, bg="light grey",pady=40)
label_stats.pack()

window.mainloop()
