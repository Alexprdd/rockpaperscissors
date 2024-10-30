import tkinter as tk
import random

# Initialize scores
player_score_value = 0
computer_score_value = 0

#functions

def play(player_choice):
    global player_score_value, computer_score_value

    # Possible choices
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    # Update selection entries
    player_select_entry.delete(0, tk.END)
    player_select_entry.insert(tk.END, player_choice)

    computer_select_entry.delete(0, tk.END)
    computer_select_entry.insert(tk.END, computer_choice)

    # Determine the winner
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        player_score_value += 1
    else:
        result = "Computer wins!"
        computer_score_value += 1

    # Update scores
    player_score_entry.delete(0, tk.END)
    player_score_entry.insert(tk.END, str(player_score_value))

    computer_score_entry.delete(0, tk.END)
    computer_score_entry.insert(tk.END, str(computer_score_value))

    # Display result
    result_label.config(text=result)

#window

window=tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("800x400")

#title/label

title=tk.Label(window, text="Rock Paper Scissors", font=("Arial", 20) ,fg="grey")
title.place(x=270,y=0)

#options label
options=tk.Label(window, text="Your Options:",font=("arial", 12), fg="Grey")
options.place(x=80,y=80)

#buttons
rock = tk.Button(window, text="Rock", font=("Arial", 12), fg="black", bg="pink", width=10, command=lambda: play("Rock"))
rock.place(x=180, y=125)

paper = tk.Button(window, text="Paper", font=("Arial", 12), fg="black", bg="grey", width=10, command=lambda: play("Paper"))
paper.place(x=360, y=125)

scissors = tk.Button(window, text="Scissors", font=("Arial", 12), fg="black", bg="lightblue", width=10, command=lambda: play("Scissors"))
scissors.place(x=550, y=125)

#score label
score=tk.Label(window, text="Score:",font=("arial", 12), fg="Grey")
score.place(x=100,y=170)

#selection and score labels
player_select=tk.Label(window, text="You Selected:",font=("arial", 12), fg="black")
player_select.place(x=180,y=200)

computer_select=tk.Label(window, text="Computer Selected:",font=("arial", 12), fg="black")
computer_select.place(x=160,y=230)

player_score=tk.Label(window, text="Your score:",font=("arial", 12), fg="black")
player_score.place(x=500,y=200)

computer_score=tk.Label(window, text="Computer Score:",font=("arial", 12), fg="black")
computer_score.place(x=480,y=230)

#entries for choices and scores

player_select_entry=tk.Entry(window, width=8)
player_select_entry.place(x=280,y=200)

computer_select_entry=tk.Entry(window, width=8)
computer_select_entry.place(x=301,y=230)

player_score_entry=tk.Entry(window, width=8)
player_score_entry.place(x=582,y=200)

computer_score_entry=tk.Entry(window, width=8)
computer_score_entry.place(x=602,y=230)

# Result label
result_label = tk.Label(window, text="", font=("Arial", 12), fg="blue")
result_label.place(x=350, y=280)

window.mainloop()