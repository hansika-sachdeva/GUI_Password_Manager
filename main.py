from tkinter import *
from tkinter import messagebox
import pandas
from password_generator import generate_password
import pyperclip


def clear_pass():
    pass_entry.delete(0, END)


def clear_website():
    website_entry.delete(0, END)


def clear_email():
    email_entry.delete(0, END)


def generate_pass():
    password = generate_password()
    pass_entry.delete(0, END)
    pass_entry.insert(END, string=password)


def copy_pass():
    password = pass_entry.get()
    pyperclip.copy(password)



def save_pass():
    password = pass_entry.get()
    website = website_entry.get()
    email = email_entry.get()

    new_data_dict = {"Website": website, "Email/Username": email, "Password": password}
    new_df = pandas.DataFrame(new_data_dict, index=[0])

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Error", message="Field(s) cannot be empty")

    else:
        try:
            df = pandas.read_csv("password_data.csv")

        except FileNotFoundError:
            new_df.to_csv('password_data.csv', mode="w", index=False)
            clear_pass()
            clear_website()

        else:
            duplicate_entry = False
            if website in df["Website"].values:
                rows = df[df.Website == website]
                for (index, row) in rows.iterrows():
                    if row["Email/Username"] == email:
                        duplicate_entry = True
                        old_password = row["Password"]
                        ans = messagebox.askyesno(title="Change Password?",
                                                  message=f'You have already saved a password for this '
                                                          f'website and username. Do you want to change it? \n\n'
                                                          f'Old Password: {old_password} \nNew Password: {password}')
                        if ans:
                            df.at[index, 'Password'] = password
                            df.to_csv("password_data.csv", mode="w", index=False)
                            clear_pass()
                            clear_website()

            if not duplicate_entry:
                new_df.to_csv("password_data.csv", mode="a", header=False, index=False)
                clear_pass()
                clear_website()



def find_pass():
    try:
        df = pandas.read_csv("password_data.csv")

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="You haven't saved any passwords yet")

    else:
        website = website_entry.get()
        email = email_entry.get()
        pass_found = False

        if website in df["Website"].values:
            rows = df[df.Website == website]
            for (index, row) in rows.iterrows():
                if row["Email/Username"] == email:
                    pass_found = True
                    saved_password = row["Password"]
                    is_ok = messagebox.showinfo(title="Password info", message=f"Website: {website}\nEmail/Username: "
                                                                               f"{email} \nPassword: {saved_password}")
                    if is_ok:
                        pass_entry.insert(END, saved_password)
                        email_entry.insert(END, email)

        if not pass_found:
            messagebox.showerror(title="Error", message="No passwords saved for this website ans username")


## GUI SETUP ##

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=30)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="bg2.png")
canvas.create_image(102, 100, image=logo_img)
canvas.grid(column=1, row=0, columnspan=2, pady=10)

website_label = Label(text="Website :")
website_label.grid(column=0, row=1, sticky="w", pady=10)
email_label = Label(text="Email/Username :")
email_label.grid(column=0, row=2, sticky="w", pady=10)
pass_label = Label(text="Password :")
pass_label.grid(column=0, row=3, sticky="w", pady=10)

website_entry = Entry(width=53)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()
email_entry = Entry(width=70)
email_entry.grid(column=1, row=2, columnspan=3, sticky="w")
email_entry.insert(END, string="abc@gmail.com")
pass_entry = Entry(width=30)
pass_entry.grid(column=1, row=3, sticky="w")

generate_button = Button(text=" Generate Password ", command=generate_pass)
generate_button.grid(column=2, row=3, sticky="e")
copy_button = Button(text=" Copy Password ", command=copy_pass, width=13)
copy_button.grid(column=3, row=3, sticky="e")
save_button = Button(width=74, text="Save Password", command=save_pass)
save_button.grid(column=0, row=5, columnspan=4, pady=10)
find_button = Button(text="Find Password", command=find_pass, width=13)
find_button.grid(column=3, row=1, sticky="e")

clear_pass_button = Button(text="x", command=clear_pass)
clear_pass_button.grid(column=1, row=3, sticky="e")
clear_email_button = Button(text="x", command=clear_email)
clear_email_button.grid(column=3, row=2, sticky="e")
clear_website_button = Button(text="x", command=clear_website)
clear_website_button.grid(column=2, row=1, sticky="e")

window.mainloop()
