from tkinter import *
import random
from tkinter import messagebox


def verify():
    pass


windows = Tk()
windows.title("Lotto Draw")
windows.geometry("1000x320")
windows.config(background="yellow")

lottries = Label(windows, text="WALALA WASALA", font=("bold", 20), bg="yellow", fg="black")
lottries.grid(row=1, column=1)

play = Label(windows, text="Play!! :", font=("bold", 12), bg="black", fg="white")
play.grid(row=4, column=0)

num1 = IntVar()
num2 = IntVar()
num3 = IntVar()
num4 = IntVar()
num5 = IntVar()
num6 = IntVar()

txt1 = Entry(windows, textvariable=num1, font=('bold', 30), width=2)
txt1.grid(row=4, column=2)
txt2 = Entry(windows, textvariable=num2, font=('bold', 30), width=2)
txt2.grid(row=4, column=4)
txt3 = Entry(windows, textvariable=num3, font=('bold', 30), width=2)
txt3.grid(row=4, column=6)
txt4 = Entry(windows, textvariable=num4, font=('bold', 30), width=2)
txt4.grid(row=4, column=8)
txt5 = Entry(windows, textvariable=num5, font=('bold', 30), width=2)
txt5.grid(row=4, column=10)
txt6 = Entry(windows, textvariable=num6, font=('bold', 30), width=2)
txt6.grid(row=4, column=12)

result_answer = Label(windows, width=50, height=8)
result_answer.grid(row=12, column=0)


def luck():
    x = num1.get()
    y = num2.get()
    z = num3.get()
    a = num4.get()
    b = num5.get()
    c = num6.get()

    my_list = [x, y, z, a, b, c]
    my_list.sort()

    todaylotto = sorted(random.sample(range(1, 49), 6))

    if any(my_list) < 0 or any(my_list) < 50:
        messagebox.showinfo("hurray", "Get ready")

        if len(todaylotto) == len(my_list):
            same = set(todaylotto).intersection(set(my_list))
            if len(same) == 6:
                result_answer.config(text="Jackpot Hurray \n" + "You just got your self Price : R10, 000 000.00" + "\n Today Lotto Numbers are" + str(todaylotto))
            elif len(same) == 5:
                result_answer.config(text="Felicitations" + "You got 5 numbers correct" + "\n With this Outstanding Achievement" + "You won yourself R8, 584.00" + "\n Today Lotto Numbers are" + str(todaylotto))
            elif len(same) == 4:
                result_answer.config(text="Felicitations" + "You got 4 numbers correct" + "\n With this Meritorious Achievement" + "You won yourself R2, 384.00" + "\n Today Lotto Numbers are" + str(todaylotto))
            elif len(same) == 3:
                result_answer.config(text="Felicitations" + "You got 3 numbers correct" + "\n With this Substantial Achievement" + "You won yourself R100.50" + "\n Today Lotto Numbers are" + str(todaylotto))
            elif len(same) == 2:
                result_answer.config(text="Felicitations" + "You got 2 numbers correct" + "\n With this Adequate Achievement" + "You won yourself R20.00" + "\n Today Lotto Numbers are" + str(todaylotto))
            elif len(same) == 1:
                messagebox.showinfo("RESULT", "We are sorry you only got one correct lotto numbers are: " + str(todaylotto))
            elif len(same) == 0:
                messagebox.showinfo("RESULT", "Try again Lotto numbers : " + str(todaylotto))
    else:
        messagebox.showinfo("NOOO", "Follow the rules")
        num1.delete(0, END)
        num2.delete(0, END)
        num3.delete(0, END)
        num4.delete(0, END)
        num5.delete(0, END)
        num6.delete(0, END)


btn = Button(windows, text="CHECK YOUR RESULTS", bg="magenta", command=luck)
btn.grid(row=10, column=0)

windows.mainloop()
