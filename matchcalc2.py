import mymath
from tkinter import *
from tkinter import ttk
def fun():
	root = Tk() 
	root.geometry("350x250") 
	root.title("Sticky Notes") 
	root.minsize(height=250, width=350) 
	root.maxsize(height=250, width=350) 
	text_info = Text(root,) 
	text_info.pack(fill=BOTH) 
	root.mainloop() 

def calc():
	if (e5.get() == 'trianglearea'):
		res=mymath.trianglearea(float(e2.get()),float(e3.get()))
		myText.set(res)
	elif (e5.get() == 'circlearea'):
		res=mymath.circlearea(float(e4.get()))
		myText.set(res)
	elif (e5.get() == 'squarearea'):
		res=mymath.squarearea(float(e1.get()))
		myText.set(res)

	elif (e5.get() == 'spherevol'):
		res=mymath.spherevol(float(e4.get()))
		myText.set(res)
	elif (e5.get() == 'cubevol'):
		res=mymath.cubevol(float(e1.get()))
		myText.set(res)
	elif (e5.get() == 'cuboidvol'):
		res=mymath.cuboidvol(float(e1.get()),float(e2.get()),float(e3.get()))
		myText.set(res)
	elif (e5.get() == 'cylinvol'):
		res=mymath.cylinvol(float(e3.get()),float(e4.get()))
		myText.set(res)
	elif (e5.get() == 'hemisvol'):
		res=mymath.hemisvol(float(e4.get()))
		myText.set(res)
	elif (e5.get() == 'conevol'):
		res=mymath.conevol(float(e3.get()),float(e4.get()))
		myText.set(res)

	elif (e5.get() == 'cubecsa'):
		res=mymath.cubecsa(int(e1.get()))
		myText.set(res)
	elif (e5.get() == 'cuboidcsa'):
		res=mymath.cuboidcsa(float(e1.get()),float(e2.get()),float(e3.get()))
		myText.set(res)
	elif (e5.get() == 'spherecsa'):
		res=mymath.spherecsa(float(e4.get()))
		myText.set(res)
	elif (e5.get() == 'hemiscsa'):
		res=mymath.spherecsa(float(e4.get()))
		myText.set(res)
	elif (e5.get() == 'cylincsa'):
		res=mymath.cylincsa(float(e3.get()),float(e4.get()))
		myText.set(res)
	elif (e5.get() == 'conecsa'):
		res=mymath.conecsa(float(e1.get()),float(e4.get()))
		myText.set(res)

	elif (e5.get() == 'cubetsa'):
		res=mymath.cubetsa(int(e1.get()))
		myText.set(res)
	elif (e5.get() == 'cuboidtsa'):
		res=mymath.cuboidtsa(float(e1.get()),float(e2.get()),float(e3.get()))
		myText.set(res)
	elif (e5.get() == 'spheretsa'):
		res=mymath.spheretsa(float(e4.get()))
		myText.set(res)
	elif (e5.get() == 'hemistsa'):
		res=mymath.spheretsa(float(e4.get()))
		myText.set(res)
	elif (e5.get() == 'cylintsa'):
		res=mymath.cylintsa(float(e3.get()),float(e4.get()))
		myText.set(res)
	elif (e5.get() == 'conetsa'):
		res=mymath.conetsa(float(e1.get()),float(e4.get()))
		myText.set(res)


master = Tk()
master.title('Area and perimeter calculator')
myText=StringVar();
Label(master, text="LENGTH").grid(row=0, sticky=W)
Label(master, text="BREATH").grid(row=1, sticky=W)
Label(master, text="HEIGHT").grid(row=2, sticky=W)
Label(master, text="RADIUS").grid(row=3, sticky=W)
Label(master, text="NOTE:").grid(row=7, sticky=W)
Label(master, text="RESULT:").grid(row=14, sticky=W)

m=StringVar();
ttk.Label(master, text ="OPERATION").grid(row = 4) 
e5= ttk.Combobox(master, width = 17, textvariable = m) 
  
e5['values'] = ('trianglearea',
	 'squarearea',
	 'circlearea',
	 'cubevol',
	 'cuboidvol',
	 'spherevol',
	 'hemisvol',
	 'cylinvol',
	 'conevol',
	 'cubecsa',
	 'cuboidcsa',
	 'spherecsa',
	 'hemiscsa',
	 'cylincsa',
	 'conecsa',
	 'cubetsa',
	 'cuboidtsa',
	 'spheretsa',
	 'hemistsa',
	 'cylintsa',
	 'conetsa')
  
e5.current(1)  

resul=Label(master, text="", textvariable=myText).grid(row=14,column=1, sticky=W)
	
expression = "" 
def press(num): 
    global expression 
 
    expression = expression + str(num) 
 
    equation.set(expression)

def equalpress(): 
        global expression 
        total = str(eval(expression)) 
 
        equation.set(total) 
        expression = ""  
	  
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
 

if __name__ == "__main__": 
 
    equation = StringVar() 
 
    expression_field = Entry(master, textvariable=equation) 
 
    expression_field.grid(columnspan=4, ipadx=70)
 
    button1 = Button(master, text=' 1 ', fg='black', bg='white',command=lambda: press(1), height=1, width=7) 
    button1.grid(row=20, column=0) 
 
    button2 = Button(master, text=' 2 ', fg='black', bg='white',command=lambda: press(2), height=1, width=7) 
    button2.grid(row=20, column=1) 
 
    button3 = Button(master, text=' 3 ', fg='black', bg='white',command=lambda: press(3), height=1, width=7) 
    button3.grid(row=20, column=2) 
 
    button4 = Button(master, text=' 4 ', fg='black', bg='white',command=lambda: press(4), height=1, width=7) 
    button4.grid(row=21, column=0) 
 
    button5 = Button(master, text=' 5 ', fg='black', bg='white',command=lambda: press(5), height=1, width=7) 
    button5.grid(row=21, column=1) 
 
    button6 = Button(master, text=' 6 ', fg='black', bg='white',command=lambda: press(6), height=1, width=7) 
    button6.grid(row=21, column=2) 
 
    button7 = Button(master, text=' 7 ', fg='black', bg='white',command=lambda: press(7), height=1, width=7) 
    button7.grid(row=22, column=0) 
 
    button8 = Button(master, text=' 8 ', fg='black', bg='white',command=lambda: press(8), height=1, width=7) 
    button8.grid(row=22, column=1) 
 
    button9 = Button(master, text=' 9 ', fg='black', bg='white',command=lambda: press(9), height=1, width=7) 
    button9.grid(row=22, column=2) 
 
    button0 = Button(master, text=' 0 ', fg='black', bg='white',command=lambda: press(0), height=1, width=7) 
    button0.grid(row=23, column=0) 
 
    plus = Button(master, text=' + ', fg='black', bg='white', command=lambda: press("+"), height=1, width=7) 
    plus.grid(row=20, column=4) 
 
    minus = Button(master, text=' - ', fg='black', bg='white', command=lambda: press("-"), height=1, width=7) 
    minus.grid(row=21, column=4) 
 
    multiply = Button(master, text=' * ', fg='black', bg='white', command=lambda: press("*"), height=1, width=7) 
    multiply.grid(row=22, column=4) 
 
    divide = Button(master, text=' / ', fg='black', bg='white', command=lambda: press("/"), height=1, width=7) 
    divide.grid(row=23, column=4) 
 
    equal = Button(master, text=' = ', fg='black', bg='white',command=equalpress, height=1, width=7) 
    equal.grid(row=24, column=4) 
 
    clear = Button(master, text='Clear', fg='black', bg='white',command=clear, height=1, width=7) 
    clear.grid(row=23, column=2) 
 
    Decimal= Button(master, text='.', fg='black', bg='white',command=lambda: press('.'), height=1, width=7) 
    Decimal.grid(row=23, column=1)
    

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e6 = '        '

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row = 4,column=1)


def c():
	b = Button(master, text="Calculate", command=calc)
	b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)

	c = Button(master, text="Notes", command=fun)
	c.grid(row=7, column=1,columnspan=1, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
c()	
master.mainloop()
