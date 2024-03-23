import tkinter as tk

class CalendarApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendar App")

        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(padx=20, pady=20)

        self.calendar_frame = tk.Frame(self.main_frame)
        self.calendar_frame.pack(padx=10, pady=10)

        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # Add Labels for each day of the week in self.days in the grid starting at index 1 (Column Labels)
        for i, day in enumerate(self.days):
            tk.Label(self.calendar_frame, text=day, width=10, borderwidth=2, relief="ridge").grid(row=0, column=i+1)

        self.hours = ["12:00 AM", "1:00 AM", "2:00 AM", "3:00 AM", "4:00 AM", "5:00 AM", "6:00 AM", "7:00 AM",
                      "8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM",
                      "4:00 PM", "5:00 PM", "6:00 PM", "7:00 PM", "8:00 PM", "9:00 PM", "10:00 PM", "11:00 PM"]

        # Add labels for each time of the day in self.hours in the grid starting at index 1 (Row Labels)
        for i, hour in enumerate(self.hours):
            tk.Label(self.calendar_frame, text=hour, width=10, borderwidth=2, relief="ridge").grid(row=i + 1, column=0)

        # Create Hours X Days table with empty event slots
        self.event_slots = []
        for i in range(len(self.hours)):
            row = []
            for j in range(len(self.days)):
                label = tk.Label(self.calendar_frame, text="", width=20, height=2, borderwidth=1, relief="solid")
                label.grid(row=i + 1, column=j + 1)
                row.append(label)
            self.event_slots.append(row)


def main():
    # Create a blank GUI
    root = tk.Tk()
    # Populate GUI by running it through CalendarApp class
    CalendarApp(root)
    # Run GUI and make it interactive
    root.mainloop()


if __name__ == "__main__":
    main()