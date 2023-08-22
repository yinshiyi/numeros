import tkinter as tk
# MAC does not work very well
import random
from num2words import num2words

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
        result_label.config(text="¡Correcto!")
    else:
        result_label.config(text="¡Incorrecto! El número era " + num2words(correct_number, lang='es'))

def generate_new_number():
    global correct_number
    correct_number = random.randint(0, 100)
    result_label.config(text="")
    random_number_label.config(text="Número aleatorio: " + str(correct_number))
    options = generate_random_options(correct_number)
    for i, option in enumerate(options):
        option_buttons[i].config(text=num2words(option, lang='es'), command=lambda option=option: check_guess(option))

# Create the main window
root = tk.Tk()
root.title("Juego de Adivinanza de Números")
root.configure(bg="white")
#root['background']='white'

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
    option_button = tk.Button(root, text="", width=20, height=2)
    option_buttons.append(option_button)
    option_button.pack(side=tk.LEFT, padx=10, pady=10)

# Button to generate a new random number
new_number_button = tk.Button(root, text="Nuevo número", command=generate_new_number)
new_number_button.pack(pady=20)

# Generate the first random number
generate_new_number()

# Start the main loop
root.mainloop()
