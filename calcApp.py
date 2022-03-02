from tkinter import *
from numpy import multiply, subtract

expression = ""

def press(num):

    global expression
    expression = expression + str(num)
    equation.set(expression)
 
def equalpress():
    try:
 
        global expression
 
        total = str(eval(expression))
 
        equation.set(total)
        expression = ""

    except:
 
        equation.set(" error ")
        expression = ""
 
 
def clear():
    global expression
    expression = ""
    equation.set("")
 

if __name__ == "__main__":
    window = Tk()
    window.configure(background="Light grey")
    window.title(" Tango & Cash Co. Calculator")
    #window.geometry("500x200")
 
    equation = StringVar()

    expression_field = Entry(window, textvariable=equation, width=15)
    expression_field.grid(columnspan=4, ipadx=70)

    btn1 = Button(window, text=' 1 ', bg='light grey',command=lambda: press(1), height=2, width=10)
    btn1.grid(row=2, column=0)
    btn2 = Button(window, text=' 2 ', bg='light grey',command=lambda: press(2), height=2, width=10)
    btn2.grid(row=2, column=1)
    btn3 = Button(window, text=' 3 ', bg='light grey', command=lambda: press(3), height=2, width=10)
    btn3.grid(row=2, column=2)
    btn4 = Button(window, text=' 4 ', bg='light grey',command=lambda: press(4), height=2, width=10)
    btn4.grid(row=3, column=0)
    btn5 = Button(window, text=' 5 ', bg='light grey',command=lambda: press(5), height=2, width=10)
    btn5.grid(row=3, column=1)
    btn6 = Button(window, text=' 6 ', bg='light grey',command=lambda: press(6), height=2, width=10)
    btn6.grid(row=3, column=2)
    btn7 = Button(window, text=' 7 ', bg='light grey',command=lambda: press(7), height=2, width=10)
    btn7.grid(row=4, column=0)
    btn8 = Button(window, text=' 8 ', bg='light grey', command=lambda: press(8), height=2, width=10)
    btn8.grid(row=4, column=1)
    btn9 = Button(window, text=' 9 ', bg='light grey', command=lambda: press(9), height=2, width=10)
    btn9.grid(row=4, column=2)
    btn0 = Button(window, text=' 0 ', bg='light grey',command=lambda: press(0), height=2, width=10)
    btn0.grid(row=5, column=0)
    add = Button(window, text=' + ', bg='light grey',command=lambda: press("+"), height=2, width=10)
    add.grid(row=2, column=3)
    subtract = Button(window, text=' - ', bg='light grey',command=lambda: press("-"), height=2, width=10)
    subtract.grid(row=3, column=3)
    multiply = Button(window, text=' * ', bg='light grey',command=lambda: press("*"), height=2, width=10)
    multiply.grid(row=4, column=3) 
    divide = Button(window, text=' / ', bg='light grey', command=lambda: press("/"), height=2, width=10)
    divide.grid(row=5, column=3)
    equal = Button(window, text=' = ', bg='light grey',command=equalpress, height=2, width=10)
    equal.grid(row=5, column=2)
    clear = Button(window, text='Clear', bg='light grey',command=clear, height=2, width=10)
    clear.grid(row=5, column='1')

    window.mainloop() 