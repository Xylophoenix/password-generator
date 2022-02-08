import random
from tkinter import *
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', ':', ';', '"', '<', '>', ',', '.', '/', '?', '~']
window = Tk()
window.title("GUI Password Generator")
window.geometry("500x500")
window.configure(bg="#00000f")
welcome_label = Label(window, text="Welcome to the Password Generator", bg="#00000f", fg="white", font=("Helvetica", 16))
welcome_label.pack()
instruction_label = Label(window, text="With the following options you will be able to generate a password", bg="#00000f", fg="white", font=("Helvetica", 12))
instruction_label.pack()
letter_entry_label = Label(window, text="How many letters do you want in your password?", bg="#00000f", fg="white", font=("Helvetica", 12))
letter_entry_label.pack()
letter_entry = Entry(window, width=10)
letter_entry.pack()
number_entry_label = Label(window, text="How many numbers do you want in your password?", bg="#00000f", fg="white", font=("Helvetica", 12))
number_entry_label.pack()
number_entry = Entry(window, width=10)
number_entry.pack()
symbol_entry_label = Label(window, text="How many symbols do you want in your password?", bg="#00000f", fg="white", font=("Helvetica", 12))
symbol_entry_label.pack()
symbol_entry = Entry(window, width=10)
symbol_entry.pack()
confirm_button = Button(window, text="Confirm", command=lambda: generate_password(letter_entry.get(), number_entry.get(), symbol_entry.get()))
confirm_button.pack()
def generate_password(letters, numbers, symbols):
    password = ""
    for i in range(1, int(letters) + 1):
        password += (random.choice(letter))
    for i in range(1, int(numbers) + 1):
        password += (random.choice(number))   
    for i in range(1, int(symbols) + 1):
        password += (random.choice(symbol))
    password = random.sample(password, len(password))
    password_label = Label(window, text=password, bg="#00000f", fg="white", font=("Helvetica", 16))
    password_label.pack()

window.mainloop()