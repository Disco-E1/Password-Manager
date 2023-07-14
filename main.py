from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json

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
    
def find_password():
    website = website_txt.get()
    try:
        with open("data.json", "r") as data_file:
            content = json.load(data_file)
        
            if website_txt.get() in content:
                email = content[website]["email"]
                password = content[website]["password"]
                
                messagebox.showinfo(title="User Information", message=f"Website: {website}\n Username: {email}\n Password: {password}")
            
            elif website_txt.get() not in content:
                messagebox.showinfo(title="Oops", message="No details for the website exist.")
    except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump

def save():

    website = website_txt.get()
    email = log_in_txt.get()
    password = pass_txt.get()
    new_data = {
         website : {
        "email": email,
        "password": password
        }
    }
    
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:   
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
             json.dump(new_data, data_file, indent=4)
        
        else:
            data.update(new_data)
        
            with open("data.json", "w") as data_file:
                json.dump(data,data_file, indent=4)
                
        finally:
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
website_txt = Entry(width=21)
website_txt.grid(row=1, column=1)
website_txt.focus()

search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(row=1, column=2)
search_button.config(padx=10)

log_in_label = Label(text="Email/Username:")
log_in_label.grid(row=2, column=0)
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