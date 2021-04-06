'''tkinter is a python module that is is used to build the user interface.
we'll only import what we need from our tkinter module.
things we needed to build :
1. Tk : it is used to build the application window
2. Radiobutton : to make checkbox type button
3. button : normal button
4. lable : to form text
5. stringvar : a var of string typr to input string var
6. Intvar : to take input as integer
7. entry : for taking input
'''
from tkinter import Tk, Radiobutton, Button, Label, StringVar, IntVar, Entry


class TipCalculator():
    def __init__(self):
        window = Tk()
        window.title("Tip Calculator Application")
        window.configure(background="purple")
        window.geometry("390x320")
        window.resizable(width=False, height=False)

        self.meal_cost = StringVar()
        self.tip_percent = IntVar()
        self.tip = StringVar()
        self.total_cost = StringVar()

        tip_percent = Label(window, text="Tip Percentage",
                            bg="black", fg="red")
        tip_percent.grid(column=0, row=0, padx=15, pady=30)
        bill_amount = Label(window, text="Bill Amount",
                            bg="orange", fg="black")
        bill_amount.grid(column=1, row=0, padx=15, pady=30)
        bill_amount_entry = Entry(
            window, textvariable=self.meal_cost, width=14)
        bill_amount_entry.grid(column=2, row=0, padx=15, pady=30)

        five_percent_tip = Radiobutton(
            window, text="05%", variable=self.tip_percent, value=5)
        five_percent_tip.grid(column=0, row=1)

        five_percent_tip = Radiobutton(
            window, text="10%", variable=self.tip_percent, value=10)
        five_percent_tip.grid(column=0, row=2)

        five_percent_tip = Radiobutton(
            window, text="15%", variable=self.tip_percent, value=15)
        five_percent_tip.grid(column=0, row=3)

        five_percent_tip = Radiobutton(
            window, text="20%", variable=self.tip_percent, value=20)
        five_percent_tip.grid(column=0, row=4)

        five_percent_tip = Radiobutton(
            window, text="25%", variable=self.tip_percent, value=25)
        five_percent_tip.grid(column=0, row=5)

        tip_amount_lb1 = Label(window, text="Tip Amount",
                               bg="brown", fg="white")
        tip_amount_lb1.grid(column=1, row=3, padx=15)

        tip_amount_entry = Entry(window, textvariable=self.tip, width=14)
        tip_amount_entry.grid(column=2, row=3)

        bill_total_lb1 = Label(window, text="Total Bill Amount",
                               bg="blue", fg="white")
        bill_total_lb1.grid(column=1, row=5, padx=15)

        bill_total_entry = Entry(
            window, textvariable=self.total_cost, width=14)
        bill_total_entry.grid(column=2, row=5)

        calculate_btn = Button(window, text="Calculate",
                               bg="green", fg="black", command=self.calculate)
        calculate_btn.grid(column=1, row=7, padx=25, pady=25)

        clear_btn = Button(window, text="Clear",
                           bg="dark blue", fg="white", command=self.clear)
        clear_btn.grid(column=2, row=7, padx=25, pady=25)

        window.mainloop()

    def calculate(self):
        pre_tip = float(self.meal_cost.get())
        percentage = self.tip_percent.get() / 100
        tip_amount_entry = pre_tip * percentage
        self.tip.set(tip_amount_entry)

        final_bill = pre_tip + tip_amount_entry
        self.total_cost.set(final_bill)

    def clear(self):
        self.total_cost.set("")
        self.meal_cost.set("")
        self.tip.set("")

    # window.mainloop()


TipCalculator()
