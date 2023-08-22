import tkinter as tk
import random

def generate_random_number():
    return random.randint(0, 100)

def check_guess(selecsted_number):
    random_number = generate_random_number()
    if selected_number == random_number:
        result_label.config(text="Correct!")
    else:
        result_label.config(text="Incorrect! The number was " + str(random_number))

def generate_new_number():
    result_label.config(text="")
    random_number = generate_random_number()
    random_number_label.config(text="Random Number: " + str(random_number))

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Generate and display the initial random number
random_number_label = tk.Label(root, text="", font=("Arial", 20))
random_number_label.pack()
generate_new_number()

# Create option buttons
option_buttons = []
for i in range(5):
    option_button = tk.Button(root, text=str(i), width=5, height=2, command=lambda i=i: check_guess(i))
    option_buttons.append(option_button)
    option_button.pack(side=tk.LEFT, padx=10, pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=("Arial", 18))
result_label.pack()

# Button to generate a new random number
new_number_button = tk.Button(root, text="New Number", command=generate_new_number)
new_number_button.pack(pady=20)

# Start the main loop
root.mainloop()
