from tkinter import *


#from win import luck


def verify():
    pass

winings = Tk()
winings.title("Lotto Draw")
winings.geometry("1000x250")
winings.config(background = "white")

lottries = Label(winings, text = "RESULTS", font =("bold",20))
lottries.grid(row = 1,column = 4)

userlist = Listbox(winings)
userlist.grid(row = 3,column = 1, sticky='nsew')

def new_list(my_list):
    userlist.delete(0, END)
    my_list = luck()

    for i in range(0, len(my_list)):
        userlist.insert(END,my_list[i])

btn_update = Button(winings, text ="Updated results",command = new_list)
btn_update.grid(row = 5,column = 4, sticky='nsew')

winings.mainloop()
