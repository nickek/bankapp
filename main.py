# Banking app

# Importing GUI, User, Bank Classes
import customtkinter
import customtkinter as tk
from User import *
from Bank import *

Nick = Bank('Nick', 'Ek', 36000, 100000)
Nick.show_details()
Shawn = Bank('Shawn', 'Brutus', 46300, 105000)
Shawn.show_details()
SNBank = [Nick, Shawn]

# Making the GUI
c = 0
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = tk.CTk()
root.geometry('500x500')
root.title('Bank')
title = tk.CTkLabel(root, text='S & N Banking', font=('Roboto', 24))
title.pack(pady=60, padx=20)
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=10)
i = 0


# Login GUI
def login():
    # counter for invalid response
    global c
    global i
    u = username.get()
    p = password.get()
    i = 0
    while i < len(SNBank):
        if u == SNBank[i].show_name() and p == SNBank[i].show_password():
            print(f'Logged in {i}')
            frame.pack_forget()
            ui()
            break
        else:
            if c < 1:
                error.pack(pady=10, padx=10)
                c += 1
        i += 1


# Create Account GUI
def create_account():
    global c
    username.pack_forget()
    password.pack_forget()
    login.pack_forget()
    error.pack_forget()
    c = 0
    create_account.pack_forget()
    new_user.pack(pady=10, padx=10)
    new_pass.pack(pady=10, padx=10)
    new_create_account.pack(pady=10, padx=10)


# Setting new account values
def set_account():
    set_user = new_user.get()
    set_pass = new_pass.get()

    new_user.forget()
    new_pass.forget()
    new_create_account.forget()

    username.pack(pady=10, padx=10)
    password.pack(pady=10, padx=10)
    login.pack(pady=10, padx=10)
    create_account.pack(pady=10, padx=10)

    SNBank.append(Bank(set_user, set_pass, 0, 0))


# User interface
# Deposit and Withdraw functions
def ui_deposit_func():

    ui_user.pack_forget()
    ui_pass.pack_forget()
    ui_logout.pack_forget()
    ui_deposit.pack_forget()
    ui_withdraw.pack_forget()

    ui_amount.pack(pady=10, padx=10)
    ui_dchecking.pack(pady=10, padx=10)
    ui_dsaving.pack(pady=10, padx=10)


def deposit_check_func():
    int_amount = int(ui_amount.get())
    SNBank[i].deposit(int_amount, 0)
    print(f'Deposited ${ui_amount.get()}, balance: {SNBank[i].show_bal(0)}')
    ui_amount.pack_forget()
    ui_dchecking.pack_forget()
    ui_dsaving.pack_forget()
    ui()


def deposit_save_func():
    int_amount = int(ui_amount.get())
    SNBank[i].deposit(int_amount, 1)
    print(f'Deposited ${ui_amount.get()}, balance: {SNBank[i].show_bal(1)}')
    ui_amount.pack_forget()
    ui_dchecking.pack_forget()
    ui_dsaving.pack_forget()
    ui()


def ui_withdraw_func():
    ui_user.pack_forget()
    ui_pass.pack_forget()
    ui_logout.pack_forget()
    ui_deposit.pack_forget()
    ui_withdraw.pack_forget()

    ui_amount.pack(pady=10, padx=10)
    ui_wchecking.pack(pady=10, padx=10)
    ui_wsaving.pack(pady=10, padx=10)


def withdraw_check_func():
    int_amount = int(ui_amount.get())
    SNBank[i].withdraw(int_amount, 0)
    print(f'Withdraw ${ui_amount.get()}, balance: {SNBank[i].show_bal(0)}')
    ui_amount.pack_forget()
    ui_wchecking.pack_forget()
    ui_wsaving.pack_forget()
    ui()


def withdraw_save_func():
    int_amount = int(ui_amount.get())
    SNBank[i].withdraw(int_amount, 1)
    print(f'Withdraw ${ui_amount.get()}, balance: {SNBank[i].show_bal(1)}')
    ui_amount.pack_forget()
    ui_wchecking.pack_forget()
    ui_wsaving.pack_forget()
    ui()


# Ui function
def ui():
    global ui_user
    global ui_pass
    global ui_deposit
    global ui_withdraw
    global ui_logout
    ui_user = customtkinter.CTkLabel(master=ui_frame, text=f'Name: {SNBank[i].show_name()}'
                                                           f'\t\tChecking: ${SNBank[i].show_bal(0)}', anchor='e')
    ui_pass = customtkinter.CTkLabel(master=ui_frame, text=f'Password: {SNBank[i].show_password()}'
                                                           f'\t\t  Saving: ${SNBank[i].show_bal(1)}', anchor='e')
    ui_deposit = customtkinter.CTkButton(master=ui_frame, text='Deposit', command=ui_deposit_func)
    ui_withdraw = customtkinter.CTkButton(master=ui_frame, text='Withdraw', command=ui_withdraw_func)
    ui_logout = customtkinter.CTkButton(master=ui_frame, text='Logout', command=logout)

    ui_frame.pack(pady=10, padx=10)
    ui_user.pack(pady=5, padx=5)
    ui_pass.pack(pady=5, padx=5)
    ui_deposit.pack(pady=10, padx=10)
    ui_withdraw.pack(pady=10, padx=10)
    ui_logout.pack(pady=10, padx=10)


# Logout function
def logout():
    ui_frame.pack_forget()
    frame.pack(pady=10, padx=10)
    ui_user.destroy()
    ui_pass.destroy()
    ui_deposit.destroy()
    ui_withdraw.destroy()
    ui_logout.destroy()
    error.pack_forget()


# GUIs

# Login GUIs
username = customtkinter.CTkEntry(master=frame, placeholder_text='Username')
username.pack(pady=10, padx=10)
password = customtkinter.CTkEntry(master=frame, placeholder_text='Password', show='*')
password.pack(pady=10, padx=10)
login = customtkinter.CTkButton(master=frame, text='Login', command=login)
login.pack(pady=10, padx=10)
create_account = customtkinter.CTkButton(master=frame, text='Create account', command=create_account)
create_account.pack(pady=10, padx=10)
error = tk.CTkLabel(master=frame, text='Incorrect user/pass', font=('Roboto', 12), text_color='red')

new_user = customtkinter.CTkEntry(master=frame, placeholder_text='Username')
new_pass = customtkinter.CTkEntry(master=frame, placeholder_text='Password')
new_create_account = customtkinter.CTkButton(master=frame, text='Create account', command=set_account)

# UI GUIs
ui_frame = customtkinter.CTkFrame(master=root)
ui_deposit = customtkinter.CTkButton(master=ui_frame, text='Deposit', command=ui_deposit_func)
ui_withdraw = customtkinter.CTkButton(master=ui_frame, text='Withdraw', command=ui_withdraw_func)
ui_logout = customtkinter.CTkButton(master=ui_frame, text='Logout', command=logout)
ui_user = customtkinter.CTkLabel(master=ui_frame, text=f'Name: {SNBank[i].show_name()}'
                                                       f'\t\tChecking: ${SNBank[i].show_bal(0)}', anchor='e')
ui_pass = customtkinter.CTkLabel(master=ui_frame, text=f'Password: {SNBank[i].show_password()}'
                                                       f'\t\t  Saving: ${SNBank[i].show_bal(1)}', anchor='e')
ui_amount = customtkinter.CTkEntry(master=ui_frame, placeholder_text='Amount')
ui_dchecking = customtkinter.CTkButton(master=ui_frame, text='Checking', command=deposit_check_func)
ui_dsaving = customtkinter.CTkButton(master=ui_frame, text='Saving', command=deposit_save_func)
ui_wchecking = customtkinter.CTkButton(master=ui_frame, text='Checking', command=withdraw_check_func)
ui_wsaving = customtkinter.CTkButton(master=ui_frame, text='Saving', command=withdraw_save_func)

root.mainloop()
