# Importing Modules
from tkinter import *
from tkinter import ttk
import time
from PIL import Image, ImageTk
import pygame
import sys

# Initiating Tkinter window
root = Tk()
root.geometry('500x400+450+100')
root.title("Clock")

# Pygame Initialization
pygame.mixer.init()

# Global Image Variables for "Icon Images in Buttons"
# ClockImg = ImageTk.PhotoImage(Image.open(r"C:\Users\patha\Desktop\PYTHON\PYTHON programming Practice\MEGA PROJECTS\CLOCK\Clock img.png"))
# TimerImg = ImageTk.PhotoImage(Image.open(r"C:\Users\patha\Desktop\PYTHON\PYTHON programming Practice\MEGA PROJECTS\CLOCK\Timer img.png"))
# timer_play_img = ImageTk.PhotoImage(Image.open(r"C:\Users\patha\Desktop\PYTHON\PYTHON programming Practice\MEGA PROJECTS\CLOCK\Play.png"))
# timer_stop_img = ImageTk.PhotoImage(Image.open(r"C:\Users\patha\Desktop\PYTHON\PYTHON programming Practice\MEGA PROJECTS\CLOCK\Stop.png"))
# timer_pause_img = ImageTk.PhotoImage(Image.open(r"C:\Users\patha\Desktop\PYTHON\PYTHON programming Practice\MEGA PROJECTS\CLOCK\Pause.png"))
ClockImg = ImageTk.PhotoImage(Image.open(r"Clock Img.png"))
TimerImg = ImageTk.PhotoImage(Image.open(r"Timer img.png"))
timer_play_img = ImageTk.PhotoImage(Image.open(r"Play.png"))
timer_stop_img = ImageTk.PhotoImage(Image.open(r"Stop.png"))
timer_pause_img = ImageTk.PhotoImage(Image.open(r"Pause.png"))

# Main Function for Clock App
def Clock():
    # Title is changed into "Clock" when Clock Button is clicked
    root.title("Clock")

    # Function for Defining and Changing Time, Date, Day
    def Clock_Time():
        # Value of Hour, Minute, Second, Am/Pm, Day, Year, Month, Date
        Hour = time.strftime("%I") 
        Minute = time.strftime("%M") 
        Second = time.strftime("%S") 
        Am_Pm = time.strftime("%p")
        Day = time.strftime("%a")
        Year = time.strftime("%Y")
        Month = time.strftime("%b")
        date_primary = time.strftime("%D")
        Date = date_primary[:5]

        # Text of YearLabel
        YearLabel.config(text=f"{Year}")

        # Text of Time Label
        TimeLabel.config(text=f"{Hour} : {Minute} : {Second}")
        TimeLabel.after(1000, Clock_Time)  # After every 1 second, time is updated using Clock_Time Function i.e. text of label will be the present time every second

        # Text of Am/Pm Label
        AmPmLabel.config(text=f"{Am_Pm}")

        # Text of DayDate Label
        DayDateLabel.config(text=f"{Date}  {Day.upper()}")

    # Out of Clock_Time Function, Inside Clock Function

    # Frame for Clock App(Buttons, Text and other widgets in Clock)
    MainFrame = Frame(root, width=500, height=420)
    MainFrame.place(x=0, y=80)

    # Year Label, text is changed inside Clock_Time function
    YearLabel = Label(MainFrame, font="verdana 25 bold", text="")
    YearLabel.pack(anchor="nw")

    # AmPm Label, text is changed inside Clock_Time function
    AmPmLabel = Label(MainFrame, fg='black', font=("Verdana", 20, 'bold'), text="")
    AmPmLabel.pack(anchor='e', padx=0, pady=0)

    # Time Label, text is changed inside Clock_Time function
    TimeLabel = Label(MainFrame, bg='#292626', fg='red', font=("Verdana", 40, "bold"), text="")
    TimeLabel.pack(side=TOP, padx=60)

    # DayDate Label, text is changed inside Clock_Time function
    DayDateLabel = Label(MainFrame, fg='green', font=("Helvatica", 40, 'bold'), text="")
    DayDateLabel.pack(side=BOTTOM, pady=40)

    # Clock_Time Module is called inside Clock App
    Clock_Time()


# Main Function for Timer App
def Timer():
    # Title is changed into "Timer" when Timer Button is clicked
    root.title('Timer')

    # It will Pause the Timer Music and return to Main Timer Window when Pause Button is clicked while Timer Music is player 
    def Pause_Timer_Music():
        # pygame.mixer.music.load(r'C:\Users\patha\Desktop\PYTHON\PYTHON programming Practice\MEGA PROJECTS\CLOCK\Timer Notifier.mp3')
        pygame.mixer.music.load(r'Timer Notifier.mp3')
        pygame.mixer.music.stop()       # to stop the above loaded Timer Music
        Timer()     # after pausing the music, Main Function of Timer App is called to return to Main Timer Window 

    # It will Play the Timer Music 
    def play_timer_music():
        # pygame.mixer.music.load(r'C:\Users\patha\Desktop\PYTHON\PYTHON programming Practice\MEGA PROJECTS\CLOCK\Timer Notifier.mp3')
        pygame.mixer.music.load(r'Timer Notifier.mp3')
        pygame.mixer.music.play()
        indicator_timer.configure(text="Timer Finished.")       # the text of indicator label is changed when timer music plays.
        Label(MainFrame, text="Click To Stop The Music", font="verdana 10 bold").place(x=160, y=290)        # it will show user that, clicking the button above will stop the music being played.
        StopButton.destroy()
        PauseButton.place(x=210, y=200)

    # TODO
    def Stop_Timer():
        sys.exit()

    # It will Set Timer
    def Set_Timer():
        # Hour, Minute, Second value as Inputted by User in ComboBox
        Set_Hour = HourValue.get()
        Set_Minute = MinuteValue.get()
        Set_Second = SecondValue.get()

        # Whem Timer Starts, PlayButton is destroyed and StopButton for stopping the Timer is placed
        PlayButton.destroy()
        StopButton.place(x=210, y=200)

        # Other all widgets inside TimerMainFrame is destroyed
        HourText_Label.destroy()
        MinuteText_Label.destroy()
        SecondText_Label.destroy()
        HourBox.destroy()
        MinuteBox.destroy()
        SecondBox.destroy()

        # the label which indicates timer is running, is placed
        indicator_timer.place(x=25, y=80)
        
        # To know the exact time of Timer
        _AfterTime = (Set_Hour * 3600 *1000) + (Set_Minute * 60 *1000) + (Set_Second *1000)
        # After the Timer Duration finishes, music is played in play_timer_music
        root.after(_AfterTime, play_timer_music)

    # Still Inside Timer Function

    # Frame for Timer App(Buttons, Text and other widgets in Timer)    
    MainFrame = Frame(root, width=500, height=420)
    MainFrame.place(x=0, y=80)

    # Labels with Text:- Hour, Minute and Second above the ComboBoxes
    HourText_Label = Label(MainFrame, text="Hour", font="lucida 20 bold")
    HourText_Label.place(x=28, y=20)
    MinuteText_Label = Label(MainFrame, text="Minute", font="lucida 20 bold")
    MinuteText_Label.place(x=140, y=20)
    SecondText_Label = Label(MainFrame, text="Second", font="lucida 20 bold")
    SecondText_Label.place(x=255, y=20)

    # Hour Combobox
    HourValue = IntVar()
    HourBox = ttk.Combobox(MainFrame, width=15, textvariable=HourValue)
    HourBox['values'] = tuple(range(0, 13))     # Values of 12 Hours
    HourBox.current()
    HourBox.place(x=10, y=60)

    # Minute Combobox
    MinuteValue = IntVar()
    MinuteBox = ttk.Combobox(MainFrame, width=15, textvariable=MinuteValue)
    MinuteBox['values'] = tuple(range(0, 60))    # Values of 60 Minutes
    MinuteBox.current()
    MinuteBox.place(x=130, y=60)

    # Second Combobox
    SecondValue = IntVar()
    SecondBox = ttk.Combobox(MainFrame, width=15, textvariable=SecondValue)
    SecondBox['values'] = tuple(range(0, 59))      # Values of 60 seconds
    SecondBox.current()
    SecondBox.place(x=250, y=60)

    # PlayButton linked with Set_Timer function to Set the Timer
    PlayButton = Button(MainFrame, image=timer_play_img, command=Set_Timer)
    PlayButton.place(x=210, y=200)

    # StopButton linked with Stop_Timer function to Stop the Timer while it's running,
    #  and The button is placed inside Set_Timer Function, after destroying PlayButton when timer Starts
    StopButton = Button(MainFrame, image=timer_stop_img, command=Stop_Timer)

    # PauseButton linked with Pause_Timer_Music function to Pause the TimerMusic while it's running,
    #  and The button is placed inside Play_Timer_Music Function, after destroying StopButton when TimerMusic starts Ringing
    PauseButton = Button(MainFrame, image=timer_pause_img, command=Pause_Timer_Music)

    # To indicate that timer is running, A label is displayed and its text changes when music starts playing.
    indicator_timer = Label(MainFrame, text="Timer Running", fg="blue", font='verdana 40 bold')

# When The MainApp starts, at first ClockApp is displayed
Clock()

# Frame containing Clock and Timer Button to switch between the two Secondary Apps
UpperFrame = Frame(root, width=500, height=80, bg="skyblue")
UpperFrame.place(x=0, y=0)

# ClockAppButton for going inside Clock App, linked with Clock() Function
ClockApp_button = Button(UpperFrame, image=ClockImg, bg="skyblue", command=Clock)
ClockApp_button.place(x=100, y=5)

# TimerAppButton for going inside Timer App, linked with Timer() Function
TimerApp_button = Button(UpperFrame, image=TimerImg, bg="skyblue", command=Timer)
TimerApp_button.place(x=330, y=5)

# Running the MainLoop
root.mainloop()