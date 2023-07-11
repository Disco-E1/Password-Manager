from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

def rando_pass():
    pass_txt.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]


    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    
    password = "".join(password_list)
    pass_txt.insert(0, password)
    pyperclip.copy(password)


def save():

    website = website_txt.get()
    email = log_in_txt.get()
    password = pass_txt.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    
    is_ok = messagebox.askokcancel(title=website, message=f"these are the details entered: \nEmail: {email} "
                                   f"\nPassword: {password} \nIs it ok to save?")
    
    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website}, {email}, {password}\n")
            website_txt.delete(0, END)
            pass_txt.delete(0, END)





window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(height=200, width= 200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, columnspan=1)

website_label = Label (text="Website:")
website_label.grid(row=1, column=0, columnspan=1)
website_txt = Entry(width=35)
website_txt.grid(row=1, column=1, columnspan=2)
website_txt.focus()

log_in_label = Label(text="Email/Username:")
log_in_label.grid(row=2, column=0, columnspan=1)
log_in_txt = Entry(width=35)
log_in_txt.grid(row=2, column=1, columnspan=2)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)
pass_txt = Entry(width=21)
pass_txt.grid(row=3, column=1)

pass_button = Button(text="Generate Password", command=rando_pass)
pass_button.grid(row=3, column=2)

add_button = Button(text="Add", height=1, width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()