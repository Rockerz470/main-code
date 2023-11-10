import tkinter as tk

window = tk.Tk()
window .title("My first Pass checker")
window.geometry("500x500")

label1 = tk.Label(window, text = "Enter your password",font = ("Berlin Sans FB",30 ), fg = "Red", bg = "blue")
label1.place(x = 100, y = 100)

enter = tk.Entry(window, bg = "White", fg = "Black")
enter.place(x = 200, y = 200)

sub = tk.Button(window, text ="Submit", font = ("Berlin Sans FB", 15), bg = "Black", fg = "White")
sub.place(x = 200, y = 300)

window.mainloop()