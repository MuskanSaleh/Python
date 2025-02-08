from tkinter import *
import time

# Object creation
clock = Tk()

# All graphics here
clock.title("****Digital Clock****")  # Set title
clock.geometry('1000x500')  # Set width and height
clock.config(bg='black')  # Set background color

# Label for hour
lab_hr = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='white', fg="black")
lab_hr.place(x=120, y=50, height=110, width=100)

lab_hr_txt = Label(clock, text="Hour", font=('Times New Roman', 20, "bold"), bg='white', fg="black")
lab_hr_txt.place(x=120, y=190, height=40, width=100)

# Label for minutes
lab_min = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='white', fg="black")
lab_min.place(x=340, y=45, height=110, width=100)

lab_min_txt = Label(clock, text="Min", font=('Times New Roman', 20, "bold"), bg='white', fg="black")
lab_min_txt.place(x=340, y=190, height=40, width=100)

# Label for seconds
lab_sec = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='white', fg="black")
lab_sec.place(x=560, y=45, height=110, width=100)

lab_sec_txt = Label(clock, text="Sec", font=('Times New Roman', 20, "bold"), bg='white', fg="black")
lab_sec_txt.place(x=560, y=190, height=40, width=100)

# Label for AM/PM
lab_am = Label(clock, text="AM", font=('Times New Roman', 60, "bold"), bg='white', fg="black")
lab_am.place(x=780, y=45, height=110, width=100)

lab_am_txt = Label(clock, text="AM/PM", font=('Times New Roman', 20, "bold"), bg='white', fg="black")
lab_am_txt.place(x=780, y=190, height=40, width=100)

# Function to update the time dynamically
def update_time():
    current_time = time.strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
    hr, min_, sec, am_pm = current_time.split(":")[0], current_time.split(":")[1], current_time.split(":")[2][:2], current_time[-2:]
    
    lab_hr.config(text=hr)
    lab_min.config(text=min_)
    lab_sec.config(text=sec)
    lab_am.config(text=am_pm)
    
    clock.after(1000, update_time)  # Update every 1 second

# Call the function once to start the clock
update_time()

# Run the main loop
clock.mainloop()
