from tkinter import *

print("test1")
form = Tk()

# region config
form.title("First GUI app")
form.geometry("500x500")
form.resizable(False, False)
# form.configure(bg="red")
# form.configure(bg="#000000")
# form.attributes("-alpha", 0.7)
form_icon = PhotoImage(
    file=r"C:\Users\h.ramezani\Downloads\Telegram Desktop\python learning\icons\phone.png"
)
form.iconphoto(False, form_icon)

# endregion

# region Frame

print("test2")
header = Frame(
    master=form,
    height=70,
    bg="#eff2f5",
    highlightbackground="#d0d0d1",
    highlightthickness=5,
)
header.pack(side=TOP, fill=X)


# endregion


form.mainloop()

print("test3")
