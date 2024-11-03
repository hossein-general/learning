# Whats Tkinter? (from what i understanded)
# Let me put it this way
# you can create a tkinter interpreter by creating an instance of object Tk(), which is kind of main window
# you can also create instances of other tkinter classes known as widgets (at this point you are only creating them, they will only exist and do nothing)
# you have to define its widgets origin (the Tk() object for example is the master of all widgits) (this happens while defining the widgit and is passed as an argument)
# then if you want, you can pack them (or grid them) within your main window
# you can create instances of some objects that are widgets for Tkinter (only creating them, not using them)
# at any time you can call Tk() objects "mainloop" method. this will jump to a loop which is for tkinter to render every widgit that you have packed within and get items live graphic information! like mouse position at the moment
# so your code will simply be excuted lilne by line untill it reaches the main loop.
# at this point the program will enter the loop and you can call function through widgits
# if you close the gui window, the main loop will break and the rest of the module will be excecuted line by line until it reaches the end of the module. (just like a normal program)

from tkinter import *


# Test function
def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!")
    myLabel.pack()
    return None


def magic_function():
    myLabel = Label(root, text=widget_name.get())
    myLabel.pack()


# Creating the Tk()
root = Tk()

# Changing the title
root.title("Tesing program")

# Creating Label
widget_name = Label(root, text="test label")

# Creating Button
widget_name = Button(root, text="click me!")
widget_name = Button(
    root,
    text="click me!",
)
widget_name = Button(
    root,
    text="click me!",
)
widget_name = Button(root, text="click me!", command=myClick)
# Supported arguments:
# state=DISABLED
# padx=50, pady=80
# fg="red", bg="#2cc793" # foreground and background
# command

# Creating Input box
widget_name = Entry(root, width=50, fg="blue", bg="#ffffff", borderwidth=10)
widget_name.insert(0, " play ")
widget_name.insert(0, " test ")
widget_name.insert(9, " ok ")


# Using a widget in the root:
# widget_name.grid(row=0, column=1)
widget_name.pack()


# An extra button
magic_button = Button(root, text="magic!", command=magic_function)
magic_button.pack()

# Calling the main loop fot the root object
root.mainloop()
