from tkinter import *
from tkinter import messagebox


# function
def logins():
    log = age_entry.get()
    log1 = int(log)
    if log1 < 18:
        messagebox.showerror("NOTE!!", "Not for person under the age of 18")

    else:
        lotto.destroy()
        import win
        win.verify()


lotto = Tk()
lotto.title("SIGN UP")
lotto.geometry("1000x330")
lotto.config(background='yellow')

# labels& entries

head = Label(lotto, text="YOUR TICKET TO MILLIONNERS", font=("bold", 20), bg="green", fg="white")
head.grid(row=0, column=4)

name = Label(text="NAME", fg="black", font=("bold", 18))
name.grid(row=2, column=0)

nm_entry = Entry(width=24, fg="black", font=("bold", 18))
nm_entry.grid(row=2, column=6)

sname = Label(text="SURNAME", fg="black", font=("bold", 18))
sname.grid(row=4, column=0)

snm_entry = Entry(width=24, fg="black", font=("bold", 18))
snm_entry.grid(row=4, column=6)

age = IntVar

age_l = Label(text="AGE", fg="black", font=("bold", 18))
age_l.grid(row=6, column=0)

age_entry = Entry(textvariable=age, width=12, fg="black", font=("bold", 18))
age_entry.grid(row=6, column=6)

# button

btn = Button(lotto, text="LOGIN", bg="magenta", command=logins)
btn.grid(row=8, column=4)

lotto.mainloop()
