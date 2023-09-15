# Avingo255's Ultimate Calculator v3.1.2
# © 2022

from tkinter import *
import time

intro_line_list = ["Launching Avinash's Calculator..."]
"""how_to_root = ["After the **1/, add the denominator of the number you want to root to.",
               "For, example if you want to use cube root, enter 3.",
               "Likewise, for a square root, enter 2.",
               "Do not enter 0.5 or 0.3333 or anything like that, such as percentages or decimals.",
               "Only enter fractions, with one as the numerator."]"""
for item in intro_line_list:
    for letter in item:
        print(letter, end='')
        time.sleep(0.01)
    print("")

window = Tk()
help_text = StringVar()
window.title("Avinash's Calculator")
window.geometry('440x300')
window.minsize(440, 300)
#window.iconbitmap(r"C:\Users\avina\OneDrive\Documents\Programming\Python Level 2\Homework\Lesson 3\icon_calc.ico")
𝝅 = 3.1415926535897932384626433832795028841971693993751058209749445923078

leftFrame = Frame(window)
secondFrame = Frame(window)
thirdFrame = Frame(window)
fourthFrame = Frame(window)
fifthFrame = Frame(window)

Grid.rowconfigure(window, 0, weight=1)
Grid.columnconfigure(window, 0, weight=1)

leftFrame.grid(row=2, column=0, sticky=N + S + E + W)
secondFrame.grid(row=2, column=1, sticky=N + S + E + W)
thirdFrame.grid(row=2, column=2, sticky=N + S + E + W)
fourthFrame.grid(row=2, column=3, sticky=N + S + E + W)
fifthFrame.grid(row=2, column=4, sticky=N + S + E + W)

calc_no = 0
answer_formula = ""


def clear_clicked():
    entry.delete(0, END)


def one_clicked():
    global entry_cursor
    global answer_formula
    entry_cursor = entry.index(INSERT)
    entry.insert(entry_cursor, "1")


def two_clicked():
    global entry_cursor
    global answer_formula
    entry_cursor = entry.index(INSERT)
    entry.insert(entry_cursor, "2")


def three_clicked():
    global entry_cursor
    global answer_formula
    entry_cursor = entry.index(INSERT)
    entry.insert(entry_cursor, "3")


def four_clicked():
    global entry_cursor
    global answer_formula
    entry_cursor = entry.index(INSERT)
    entry.insert(entry_cursor, "4")


def five_clicked():
    global entry_cursor
    global answer_formula
    entry_cursor = entry.index(INSERT)
    entry.insert(entry_cursor, "5")


def six_clicked():
    global entry_cursor
    global answer_formula
    entry_cursor = entry.index(INSERT)
    entry.insert(entry_cursor, "6")


def seven_clicked():
    global entry_cursor
    global answer_formula

    entry_cursor = entry.index(INSERT)
    entry.insert(entry_cursor, "7")


def eight_clicked():
    global entry_cursor
    entry_cursor = entry.index(INSERT)
    entry.insert(entry_cursor, "8")


def nine_clicked():
    global entry_cursor
    entry_cursor = entry.index(INSERT)
    entry.insert(entry_cursor, "9")


def zero_clicked():
    global entry_cursor
    entry_cursor = entry.index(INSERT)
    entry.insert(entry_cursor, "0")


def subtract_logic():
    global entry_cursor
    entry_cursor = entry.index(INSERT)
    entry.insert(entry_cursor, "-")


def add_logic():
    global entry_cursor
    entry_cursor = entry.index(INSERT)
    entry.insert(entry_cursor, "+")


def multiply_logic():
    global entry_cursor
    entry_cursor = entry.index(INSERT)
    entry.insert(entry_cursor, "*")


def decimal_logic():
    global entry_cursor
    entry_cursor = entry.index(INSERT)
    entry.insert(entry_cursor, ".")


def pi_clicked():
    global entry_cursor
    entry_cursor = entry.index(INSERT)
    entry.insert(entry_cursor, "𝝅")


def power_clicked():
    global entry_cursor
    entry_cursor = entry.index(INSERT)
    entry.insert(entry_cursor, "**")


def root_clicked():
    global entry_cursor
    entry_cursor = entry.index(INSERT)
    entry.insert(entry_cursor, "**(1/)")
    help_text.set("16 to the power of 0.5 is the same as √16.")


def divide_logic():
    global entry_cursor
    entry_cursor = entry.index(INSERT)
    entry.insert(entry_cursor, "/")


def equals_clicked():
    global calc_no
    global answer_formula
    calc_no += 1
    original_entry = entry.get()
    answer = eval(original_entry)
    print("")
    calc_no_string = str(calc_no)
    calc_no_print_formula = "Calculation No. " + calc_no_string + ":"
    calc_no_final = [calc_no_print_formula]
    for item in calc_no_final:
        for letter in item:
            print(letter, end='')
            time.sleep(0.02)
    print("")
    original_string_entry = str(original_entry)
    string_answer_super = str(answer)
    answer_formula = [original_string_entry, '=', string_answer_super]
    for item in answer_formula:
        for letter in item:
            print(letter, end='')
            time.sleep(0.02)
    print("")
    #entry.delete(0, END)
    #entry.insert(END, "= ")
    help_text.set(answer_formula)


help_box = Label(window,
                 textvariable=help_text,
                 fg='grey95',
                 bg='grey30',
                 font=("Consolas", 10),
                 width=30)
help_box.grid(row=1, column=0, sticky=N + S + E + W, columnspan=5)

help_text.set("Enter your calculation...")

entry = Entry(window,
              fg='white',
              bg='grey30',
              font=("Microsoft JhengHei Light", 20),
              width=30)
entry.grid(row=0, column=0, sticky=N + S + E + W, columnspan=5)
entry_cursor = entry.index(INSERT)

one = Button(leftFrame,
             text="1",
             fg='azure',
             bg='black',
             font=("Lucida Sans", 15),
             width=7,
             command=one_clicked)
one.pack(expand=True, fill='both')

two = Button(secondFrame,
             text="2",
             fg='azure',
             bg='black',
             font=("Lucida Sans", 15),
             width=7,
             command=two_clicked)
two.pack(expand=True, fill='both')

three = Button(thirdFrame,
               text="3",
               fg='azure',
               bg='black',
               font=("Lucida Sans", 15),
               width=7,
               command=three_clicked)
three.pack(expand=True, fill='both')

add = Button(fourthFrame,
             text="+",
             fg='azure',
             bg='grey20',
             font=("Lucida Sans", 15),
             width=7,
             command=add_logic)
add.pack(expand=True, fill='both')

four = Button(leftFrame,
              text="4",
              fg='azure',
              bg='black',
              font=("Lucida Sans", 15),
              width=7,
              command=four_clicked)
four.pack(expand=True, fill='both')

five = Button(secondFrame,
              text="5",
              fg='azure',
              bg='black',
              font=("Lucida Sans", 15),
              width=7,
              command=five_clicked)
five.pack(expand=True, fill='both')

six = Button(thirdFrame,
             text="6",
             fg='azure',
             bg='black',
             font=("Lucida Sans", 15),
             width=7,
             command=six_clicked)
six.pack(expand=True, fill='both')

subtract = Button(fourthFrame,
                  text="−",
                  fg='azure',
                  bg='grey20',
                  font=("Lucida Sans", 15),
                  width=7,
                  command=subtract_logic)
subtract.pack(expand=True, fill='both')

seven = Button(leftFrame,
               text="7",
               fg='azure',
               bg='black',
               font=("Lucida Sans", 15),
               width=7,
               command=seven_clicked)
seven.pack(expand=True, fill='both')

eight = Button(secondFrame,
               text="8",
               fg='azure',
               bg='black',
               font=("Lucida Sans", 15),
               width=7,
               command=eight_clicked)
eight.pack(expand=True, fill='both')

nine = Button(thirdFrame,
              text="9",
              fg='azure',
              bg='black',
              font=("Lucida Sans", 15),
              width=7,
              command=nine_clicked)
nine.pack(expand=True, fill='both')

multiply = Button(fourthFrame,
                  text="×",
                  fg='azure',
                  bg='grey20',
                  font=("Lucida Sans", 15),
                  width=7,
                  command=multiply_logic)
multiply.pack(expand=True, fill='both')

clear = Button(fifthFrame,
               text="AC",
               fg='azure',
               bg='orange',
               font=("Lucida Sans", 15),
               width=7,
               command=clear_clicked)
clear.pack(expand=True, fill='both')

zero = Button(secondFrame,
              text="0",
              fg='azure',
              bg='black',
              font=("Lucida Sans", 15),
              width=7,
              command=zero_clicked)
zero.pack(expand=True, fill='both')

equals = Button(fifthFrame,
                text="=",
                fg='azure',
                bg='orange',
                font=("Lucida Sans", 15),
                width=7,
                command=equals_clicked)
equals.pack(expand=True, fill='both')

divide = Button(fourthFrame,
                text="÷",
                fg='azure',
                bg='grey20',
                font=("Lucida Sans", 15),
                width=7,
                command=divide_logic)
divide.pack(expand=True, fill='both')

power = Button(fifthFrame,
               text="^",
               fg='azure',
               bg='grey20',
               font=("Lucida Sans", 15),
               width=7,
               command=power_clicked)
power.pack(expand=True, fill='both')

root = Button(fifthFrame,
              text="√",
              fg='azure',
              bg='grey20',
              font=("Lucida Sans", 15),
              width=7,
              command=root_clicked)
root.pack(expand=True, fill='both')

decimal = Button(leftFrame,
                 text=".",
                 fg='azure',
                 bg='black',
                 font=("Lucida Sans", 15),
                 width=7,
                 command=decimal_logic)
decimal.pack(expand=True, fill='both')

pi_button = Button(thirdFrame,
                   text="𝝅",
                   fg='azure',
                   bg='black',
                   font=("Lucida Sans", 15),
                   width=6,
                   command=pi_clicked)
pi_button.pack(expand=True, fill='both')
window.mainloop()

# Avingo255's Ultimate Calculator v3.1.2
# © 2022
