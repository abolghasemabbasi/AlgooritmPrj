from datetime import datetime
from jdatetime import datetime as jdatetime_datetime, date as jdate, timedelta
import tkinter as tk

class AgeCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Age Calculator")

        self.prev_choice = None

        # Create widgets
        self.label = tk.Label(master, text="Please choose an option:")
        self.label.pack()

        self.button1 = tk.Button(master, text="Calculate age", command=self.calculate_age)
        self.button1.pack()

        self.button2 = tk.Button(master, text="Convert Persian date to Gregorian", command=self.convert_date)
        self.button2.pack()

        self.button3 = tk.Button(master, text="Calculate difference between two dates", command=self.calculate_difference)
        self.button3.pack()

        self.button4 = tk.Button(master, text="Exit", command=master.quit)
        self.button4.pack()

    def calculate_age(self):
        if self.prev_choice == "1":
            return

        # Create a new window
        self.top = tk.Toplevel(self.master)

        # Create widgets for age calculator
        self.label1 = tk.Label(self.top, text="Please enter your birth date (YYYY/MM/DD):")
        self.label1.pack()

        self.entry1 = tk.Entry(self.top)
        self.entry1.pack()

        self.button = tk.Button(self.top, text="Calculate", command=self.calculate_age_result)
        self.button.pack()

        self.prev_choice = "1"

    def calculate_age_result(self):
        birth_date_str = self.entry1.get()
        birth_date = datetime.strptime(birth_date_str, "%Y/%m/%d").date()
        today = datetime.today().date()
        age_delta = today - birth_date
        age_years = age_delta.days // 365
        age_months = (age_delta.days % 365) // 30
        age_days = (age_delta.days % 365) % 30
        result = f"You are {age_years} years, {age_months} months, and {age_days} days old."
        self.label2 = tk.Label(self.top, text=result)
        self.label2.pack()

    def convert_date(self):
        if self.prev_choice == "2":
            return

        # Create a new window
        self.top = tk.Toplevel(self.master)

        # Create widgets for date conversion
        self.label1 = tk.Label(self.top, text="Please enter a Persian date (YYYY/MM/DD):")
        self.label1.pack()

        self.entry1 = tk.Entry(self.top)
        self.entry1.pack()

        self.button = tk.Button(self.top, text="Convert", command=self.convert_date_result)
        self.button.pack()

        self.prev_choice = "2"

    def convert_date_result(self):
        j_date_str = self.entry1.get()
        j_year, j_month, j_day = map(int, j_date_str.split('/'))
        g_date = jdatetime_datetime(j_year, j_month, j_day).togregorian()
        g_date_str = g_date.strftime("%Y/%m/%d")
        result = f"The Gregorian date is: {g_date_str}"
        self.label2 = tk.Label(self.top, text=result)
        self.label2.pack()

    def calculate_difference(self):
        if self.prev_choice == "3":
            return

        # Create a new window
        self.top = tk.Toplevel(self.master)

        # Create widgets for date difference
        self.label1 = tk.Label(self.top, text="Please enter the first date (YYYY/MM/DD):")
        self.label1.pack()

        self.entry1 = tk.Entry(self.top)
        self.entry1.pack()

        self.label2 = tk.Label(self.top, text="Please enter the second date (YYYY/MM/DD):")
        self.label2.pack()

        self.entry2 = tk.Entry(self.top)
        self.entry2.pack()

        self.button = tk.Button(self.top, text="Calculate", command=self.calculate_difference_result)
        self.button.pack()

        self.prev_choice = "3"

    def calculate_difference_result(self):
        date1_str = self.entry1.get()
        date2_str = self.entry2.get()
        date1 = datetime.strptime(date1_str, "%Y/%m/%d").date()
        date2 = datetime.strptime(date2_str, "%Y/%m/%d").date()
        delta = date1 - date2
        result = f"The difference between the two dates is: {delta.days} days."
        self.label3 = tk.Label(self.top, text=result)
        self.label3.pack()

root = tk.Tk()
my_gui = AgeCalculator(root)
root.mainloop()