# Banking app

# Importing GUI, User, Bank Classes
import customtkinter
import customtkinter as tk
import time
from User import *
from Bank import *

me = Bank('Nick', 'cookies', 21, 0, 0)
me.show_details()

# Making the GUI
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = tk.CTk()
root.geometry('500x500')
root.title('Bank')
title = tk.CTkLabel(root, text='S & N Banking', font=('Roboto', 24))
title.pack(pady=60, padx=20)
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=10)


# Login GUI
def login():

    if username.get() == me.show_name() and password.get() == me.show_password():
        print(f'we did it!')
        frame.destroy()
    else:
        error = tk.CTkLabel(master=frame, text='Incorrect user/pass, Try again!', font=('Roboto', 12), text_color='red')
        error.pack(pady=10, padx=10)


username = customtkinter.CTkEntry(master=frame, placeholder_text='Username')
username.pack(pady=10, padx=10)
password = customtkinter.CTkEntry(master=frame, placeholder_text='Password', show='*')
password.pack(pady=10, padx=10)
button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=10, padx=10)

# User interface


root.mainloop()






