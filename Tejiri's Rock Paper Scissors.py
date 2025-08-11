import tkinter as tk
import random
import PIL.Image, PIL.ImageTk

# Function to play the game
def play_game(user_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    computer_choice_var.set(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        result.set("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result.set("You win!")
    else:
        result.set("You lose!")

# Create the main window
root = tk.Tk()
root.title("Tejiri's Rock Paper Scissors Game")

result = tk.StringVar()
result.set("Make a move")

computer_choice_var = tk.StringVar()
computer_choice_var.set("Computer chose: ...")

# Load images
images = {
    "Rock": PIL.ImageTk.PhotoImage(PIL.Image.open("rock-paper-scissors-(rock).png").resize((100, 100))),
    "Paper": PIL.ImageTk.PhotoImage(PIL.Image.open("Rock-paper-scissors_(paper).png").resize((100, 100))),
    "Scissors": PIL.ImageTk.PhotoImage(PIL.Image.open("Rock-paper-scissors_(scissors).png").resize((100, 100)))
}

rock_image = images["Rock"]
paper_image = images["Paper"]
scissors_image = images["Scissors"]

# Title label
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 24))
title_label.pack(pady=10)

# Buttons for choices
button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Rock", image=rock_image, compound=tk.TOP,
          command=lambda: play_game("Rock")).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Paper", image=paper_image, compound=tk.TOP,
          command=lambda: play_game("Paper")).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Scissors", image=scissors_image, compound=tk.TOP,
          command=lambda: play_game("Scissors")).pack(side=tk.LEFT, padx=5)

# Label to display the computer's choice
computer_choice_label = tk.Label(root, textvariable=computer_choice_var, font=("Arial", 14))
computer_choice_label.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, textvariable=result, font=("Arial", 18))
result_label.pack(pady=20)

# Start the application
root.mainloop()