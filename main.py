from tkinter import *

root = Tk()

root.title("Calculator")
root.geometry("340x300")

equation = StringVar()

display = StringVar()


def calculate (event):
    clicked = event.widget.cget("text")

    # Operations (negative/positive signs)
    if clicked in ["+", "-", "x", "/","%"]:
        if(equation.get()[-1] in ["+", "-", "*", "/","%"]):
            return
    elif(clicked=="+/-"):
        if(equation.get()[0]=="-"):
            equation.set(equation.get()[1:])
        else:
            equation.set("-"+equation.get())
        return

    # AC
    if(clicked=="AC"):
        equation.set("")
    elif(clicked=="="):
         # Division by 0
        if(equation.get()[-1]=="0" and equation.get()[-2]=="/"):
            equation.set("Error")
            return
        equation.set(eval(equation.get()))
    else:
        equation.set(equation.get()+clicked)

    display.set(equation.get()[-1])
    print(display.get())
    

displayEntry = Entry(font=("Monoid", 25), textvariable = equation)
displayEntry.grid(row=0,column =0, columnspan= 4)

acButton = Button(text="AC", font = ("Monoid", 33), width = "2")
acButton.grid(row=1, column =0)
acButton.bind("<Button-1>", calculate)

plusMinusButton = Button(text="+/-", font = ("Monoid", 33), width = "2")
plusMinusButton.grid(row=1, column =1)
plusMinusButton.bind("<Button-1>", calculate)

percentButton = Button(text="%", font = ("Monoid", 33), width = "2")
percentButton.grid(row=1, column =2)
percentButton.bind("<Button-1>", calculate)

divisionButton = Button(text="/", font = ("Monoid", 33), width = "2")
divisionButton.grid(row=1, column =3)
divisionButton.bind("<Button-1>", calculate)

sevenButton = Button(text="7", font = ("Monoid", 33), width = "2")
sevenButton.grid(row=2, column =0)
sevenButton.bind("<Button-1>", calculate)

eightButton = Button(text="8", font = ("Monoid", 33), width = "2")
eightButton.grid(row=2, column =1)
eightButton.bind("<Button-1>", calculate)

nineButton = Button(text="9", font = ("Monoid", 33), width = "2")
nineButton.grid(row=2, column =2)
nineButton.bind("<Button-1>", calculate)

multiplyButton = Button(text="*", font = ("Monoid", 33), width = "2")
multiplyButton.grid(row=2, column =3)
multiplyButton.bind("<Button-1>", calculate)

fourButton = Button(text="4", font = ("Monoid", 33), width = "2")
fourButton.grid(row=3, column =0)
fourButton.bind("<Button-1>", calculate)

fiveButton = Button(text="5", font = ("Monoid", 33), width = "2")
fiveButton.grid(row=3, column =1)
fiveButton.bind("<Button-1>", calculate)

sixButton = Button(text="6", font = ("Monoid", 33), width = "2")
sixButton.grid(row=3, column =2)
sixButton.bind("<Button-1>", calculate)

subtractButton = Button(text="-", font = ("Monoid", 33), width = "2")
subtractButton.grid(row=3, column =3)
subtractButton.bind("<Button-1>", calculate)

oneButton = Button(text="1", font = ("Monoid", 33), width = "2")
oneButton.grid(row=4, column =0)
oneButton.bind("<Button-1>", calculate)

twoButton = Button(text="2", font = ("Monoid", 33), width = "2")
twoButton.grid(row=4, column =1)
twoButton.bind("<Button-1>", calculate)

threeButton = Button(text="3", font = ("Monoid", 33), width = "2")
threeButton.grid(row=4, column =2)
threeButton.bind("<Button-1>", calculate)

additionButton = Button(text="+", font = ("Anonymous Pro", 33), width = "2")
additionButton.grid(row=4, column =3)
additionButton.bind("<Button-1>", calculate)

zeroButton = Button(text="0", font = ("Monoid", 33), width = "6")
zeroButton.grid(row=5, column =0, columnspan=2)
zeroButton.bind("<Button-1>", calculate)

decimalButton = Button(text=".", font = ("Monoid", 33), width = "2")
decimalButton.grid(row=5, column =2)
decimalButton.bind("<Button-1>", calculate)

equalsButton = Button(text="=", font = ("Monoid", 33), width = "2")
equalsButton.grid(row=5, column =3)
equalsButton.bind("<Button-1>", calculate)




root.mainloop()