import tkinter as tk

frame = tk.Tk()
frame.title("Calculator")

input = tk.StringVar()

def click(num):
    global func
    func = func + str(num)
    input.set(func)

def clear():
    global func
    func = ''
    input.set(func)

def operator():
    global func
    func = str(eval(func))
    input.set(func)

func = ''

entry = tk.Entry(frame, bd = 24, textvariable = input, justify = 'right')
entry.grid(columnspan = 5)

btn_1 = tk.Button(frame, text = "1", bd = 5, command = lambda:click(1))
btn_1.grid(row = 4, column = 0)

btn_2 = tk.Button(frame, text = "2", bd = 5, command = lambda:click(2))
btn_2.grid(row = 4, column = 1)

btn_3 = tk.Button(frame, text = "3", bd = 5, command = lambda:click(3))
btn_3.grid(row = 4, column = 2)

btn_4 = tk.Button(frame, text = "4", bd = 5, command = lambda:click(4))
btn_4.grid(row = 3, column = 0)

btn_5 = tk.Button(frame, text = "5", bd = 5, command = lambda:click(5))
btn_5.grid(row = 3, column = 1)

btn_6 = tk.Button(frame, text = "6", bd = 5, command = lambda:click(6))
btn_6.grid(row = 3, column = 2)

btn_7 = tk.Button(frame, text = "7", bd = 5, command = lambda:click(7))
btn_7.grid(row = 2, column = 0)

btn_8 = tk.Button(frame, text = "8", bd = 5, command = lambda:click(8))
btn_8.grid(row = 2, column = 1)

btn_9 = tk.Button(frame, text = "9", bd = 5, command = lambda:click(9))
btn_9.grid(row = 2, column = 2)

btn_0 = tk.Button(frame, text = "0", bd = 5, command = lambda:click(0))
btn_0.grid(row = 5, column = 1)

btn_dec = tk.Button(frame, text = ".", bd = 5, command = lambda:click("."))
btn_dec.grid(row = 5, column = 2)

btn_clr = tk.Button(frame, text = "C", bd = 5, command = clear)
btn_clr.grid(row = 1, column = 0)

btn_add = tk.Button(frame, text = "+", bd = 5, command = lambda:click("+"))
btn_add.grid(row = 4, column = 3)

btn_minus = tk.Button(frame, text = "-", bd = 5, command = lambda:click("-"))
btn_minus.grid(row = 2, column = 3)

btn_mult = tk.Button(frame, text = "*", bd = 5, command = lambda:click("*"))
btn_mult.grid(row = 3, column = 3)

btn_div = tk.Button(frame, text = "/", bd = 5, command = lambda:click("/"))
btn_div.grid(row = 1, column = 3)

btn_enter = tk.Button(frame, text = "=", bd = 5, command = operator)
btn_enter.grid(row = 5, column = 3)

frame.mainloop()