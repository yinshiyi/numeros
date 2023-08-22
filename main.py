import tkinter as tk
import random

def generate_random_options(correct_number):
    options = [correct_number]
    while len(options) < 5:
        new_option = random.randint(0, 100)
        if new_option != correct_number and new_option not in options:
            options.append(new_option)
    random.shuffle(options)
    return options

def check_guess(selected_number):
    if selected_number == correct_number:
        result_label.config(text="Correct!")
    else:
        result_label.config(text="Incorrect! The number was " + str(correct_number))

def generate_new_number():
    global correct_number
    correct_number = random.randint(0, 100)
    result_label.config(text="")
    random_number_label.config(text="Random Number: " + str(correct_number))
    options = generate_random_options(correct_number)
    for i, option in enumerate(options):
        option_buttons[i].config(text=str(option))

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Label to display the result
result_label = tk.Label(root, text="", font=("Arial", 18))
result_label.pack()

# Generate and display the initial random number
random_number_label = tk.Label(root, text="", font=("Arial", 20))
random_number_label.pack()
correct_number = None  # Store the correct number here initially

# Create option buttons
option_buttons = []
for _ in range(5):
    option_button = tk.Button(root, text="", width=5, height=2, command=lambda: None)
    option_buttons.append(option_button)
    option_button.pack(side=tk.LEFT, padx=10, pady=10)

# Button to generate a new random number
new_number_button = tk.Button(root, text="New Number", command=generate_new_number)
new_number_button.pack(pady=20)

# Generate the first random number
generate_new_number()

# Start the main loop
root.mainloop()
