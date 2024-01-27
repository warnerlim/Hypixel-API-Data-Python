from tkinter import *

def main_screen():
    main_screen = Tk()
    main_screen.geometry("500x300")
    main_screen.title("Bits Calculation")
    
    label = Label(main_screen, text="Something here")
    label.pack(pady=10)

    main_screen.mainloop()
    
main_screen()