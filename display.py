from tkinter import *
from tkinter import ttk
import re

class app(Tk):
    def __init__(self,converter):
        Tk.__init__(self)
        self.title("Currency Converter")
        self.currencyConverter = converter
        self.geometry("500x200")
        self.heading = Label(self, text="Real Real Time Currency Converter", fg="blue", font=("Courier", 15, "bold"), relief=RAISED, borderwidth=3).place(x=10, y=5)
        self.defaultLabel = Label(self, text = f"1 South African Rand equals = {self.currencyConverter.convert('ZAR','USD',1)} USD \n Date : {self.currencyConverter.data['date']}", relief = GROOVE, borderwidth = 5).place(x = 160, y= 50)
        numOnly = (self.register(self.numberCheck), "%d", "%P")
        self.enteredNumber = Entry(self, bd=3, relief=RIDGE, justify=CENTER, validate="key", validatecommand=numOnly).place(x=36, y=150)
        self.convertedNumber = Label(self, text="", fg="black", bg="white", relief=RIDGE, justify=CENTER, width=17, borderwidth=3).place(x=346, y=150)
        self.firstCurrency = StringVar()
        self.firstCurrency.set("ZAR")
        self.secondCurrency = StringVar()
        self.secondCurrency.set("USD")
        self.option_add("*TCombobox*Listbox.font", ("Courier", 12, "bold"))
        self.firstDropdown = ttk.Combobox(self, textvariable=self.firstCurrency, values=list(self.currencyConverter.currencies.keys()), font=("Courier", 12, "bold"), state="readonly", width=12, justify=CENTER).place(x=30, y=120)
        self.secondDropdown = ttk.Combobox(self, textvariable=self.secondCurrency, values=list(self.currencyConverter.currencies.keys()), font=("Courier", 12, "bold"), state="readonly", width=12, justify=CENTER).place(x=340, y=120)
        self.convertButton = Button(self, text="Convert", fg="black", font=('Courier', 10, 'bold'), command=self.convert).place(x = 225, y = 135)
        self.mainloop()
    
    def numberCheck(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))
    
    def convert(self):
        amount = float(self.enteredNumber.get())
        firstCurr = self.firstCurrency.get()
        secondCurr = self.secondCurrency.get()
        convertedAmount = self.currencyConverter.convert(firstCurr, secondCurr, amount)
        convertedAmount = round(convertedAmount, 2)
        self.convertedNumber.config(text=str(convertedAmount))