from tkinter import *
from pb import pbgen
from megmil import meggen
from tkinter import messagebox
from csv_downloader import *

root = None
def buttonPushed():
    user_numbers, count = pbgen()
    messagebox.showinfo(title='PowerBall',
                        message=f'Numbers {str(user_numbers)} appear {count} times in Powerball.')

def buttonPushed2():
    user_numbers, count = meggen()
    messagebox.showinfo(title='Mega Millions',
                        message=f'Numbers {str(user_numbers)} appear {count} times in Mega Millions.')

def buttonpushed3():
    retreve_file_pb()
    messagebox.showinfo(title='Powerball', message='Downloaded CSV File')

def buttonpushed4():
    retreve_file_mega()
    messagebox.showinfo(title='MegaMillions', message='Downloaded CSV File')

def exit():
    global root
    root.destroy()


def main():
    global root
    root = Tk()  # root or base window
    root.geometry('500x500')
    root.title('Coley\'s Lottery Picker')
    w = Label(root, text='Choose a Game')
    w.pack(padx=10, pady=10)  # Put label in window
    myButton = Button(root, text='Powerball Numbers', command=buttonPushed)
    myButton2 = Button(root, text='Exit', command=exit)
    myButton3 = Button(root, text='Mega Millions Numbers', command=buttonPushed2)
    d = Label(root, text='File downloads from data.gov')
    d.pack(padx=10, pady=10)
    myButton4 = Button(root, text='Download PB CSV File', command=buttonpushed3)
    myButton5 = Button(root, text='Download Mega Millions CSV File', command=buttonpushed4)
    myButton.pack(padx=10, pady=10, side=TOP)
    myButton2.pack(padx=5, pady=5, side=BOTTOM)
    myButton3.pack(padx=10, pady=10, side=TOP)
    myButton4.pack(padx=10, pady=10, side=TOP)
    myButton5.pack(padx=10, pady=10, side=TOP)
    root.mainloop()


main()
