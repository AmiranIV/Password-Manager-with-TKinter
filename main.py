from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# password generator---------------------------------------------------------------------------------------------------
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_letters + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)



# Saving data to files:-------------------------------------------------------------------------------------------------
def save():
    website = entry_website.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="ERROR", message="No empty spaces allowed")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data_js = json.load(data_file)
                # updating ol data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data_js.update(new_data)
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data_js, data_file,indent=4)

        finally:
            entry_website.delete(0, END)
            password_entry.delete(0, END)
def find_password():
    website = entry_website.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="ERROR", message="File Not Found")
    else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title="Website", message=f"Email:{email} \nPassword:{password}")
            else:
                messagebox.showinfo(title="Error", message=f"No detail for {website} found.")


# GUI SETUP
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=1)
# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=2)
email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=3)
password_label = Label(text="Password:")
password_label.grid(column=0, row=4)

# website entry
entry_website = Entry()
entry_website.grid(column=1, row=2)
entry_website.focus()
website_data = entry_website.get()
# Email/Username entry
email_entry = Entry()
email_entry.grid(column=1, row=3)
email_entry.insert(0, "leowolf@gmail.com")
email_data = email_entry.get()

# Password entry
password_entry = Entry()
password_entry.grid(column=1, row=4)
password_data = password_entry.get()

# Button Generate password:
password_button = Button(text="Generate", command=generate_password)
password_button.grid(column=2, row=4)
serch_button = Button(text="Serch", command=find_password)
serch_button.grid(column=2, row=2)
# Add button:
add_button = Button(text="Add", width=15, height=1, command=save)
add_button.grid(column=0, row=5, columnspan=3)

window.mainloop()







