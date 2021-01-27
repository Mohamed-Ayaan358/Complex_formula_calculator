import mymath
from tkinter import *
def add():
	res=(float(e7.get())+float(e8.get()))
	my.set(res)

def sub():
	res=(float(e7.get())-float(e8.get()))
	my.set(res)

def mult():
	res=(float(e7.get())*float(e8.get()))
	my.set(res)

def div():
	res=(float(e7.get())/float(e8.get()))
	my.set(res)

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
		res=mymath.trianglearea(int(e1.get()),int(e2.get()))
		myText.set(res)
	elif (e5.get() == 'circlearea'):
		res=mymath.circlearea(int(e4.get()))
		myText.set(res)
	elif (e5.get() == 'squarearea'):
		res=mymath.squarearea(int(e1.get()),int(e2.get()))
		myText.set(res)
	elif (e5.get() == 'spherevol'):
		res=mymath.spherevol(int(e4.get()))
		myText.set(res)
	elif (e5.get() == 'cubevol'):
		res=mymath.cubevol(int(e1.get()))
		myText.set(res)
	elif (e5.get() == 'cuboidvol'):
		res=mymath.cuboidvol(int(e1.get()),int(e2.get()),int(e3.get()))
		myText.set(res)
	elif (e5.get() == 'cylinvol'):
		res=mymath.cylinvol(int(e3.get()),int(e4.get()))
		myText.set(res)
	elif (e5.get() == 'hemisvol'):
		res=mymath.hemisvol(int(e4.get()))
		myText.set(res)
	elif (e5.get() == 'conevol'):
		res=mymath.conevol(int(e3.get()),int(e4.get()))
		myText.set(res)
	elif (e5.get() == 'cubecsa'):
		res=mymath.cubecsa(int(e1.get()))
		my.set(res)
		
master = Tk()
myText=StringVar();
Label(master, text="LENGTH").grid(row=0, sticky=W)
Label(master, text="BREATH").grid(row=1, sticky=W)
Label(master, text="HEIGHT").grid(row=2, sticky=W)
Label(master, text="RADIUS").grid(row=3, sticky=W)
Label(master, text="OPERATION").grid(row=4,sticky=W)
Label(master, text="RESULT:").grid(row=6, sticky=W)
Label(master, text="NOTE:").grid(row=8, sticky=W)

result=Label(master, text="", textvariable=myText).grid(row=6,column=1, sticky=W)
my=StringVar();
Label(master, text="NUMBER 1").grid(row=10, sticky=W)
Label(master, text="NUMBER 2").grid(row=12, sticky=W)
resul=Label(master, text="", textvariable=my).grid(row=14,column=1, sticky=W)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = '     '
e7 = Entry(master)
e8 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e7.grid(row=10,column=1)
e8.grid(row=12,column=1)

b = Button(master, text="Calculate", command=calc)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)

c = Button(master, text="Notes", command=fun)
c.grid(row=7, column=1,columnspan=1, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)

d = Button(master, text="Add", command=add)
d.grid(row=10, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)

e = Button(master, text="Subtract", command=sub)
e.grid(row=12, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)

f = Button(master, text="Multiply", command=mult)
f.grid(row=14, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)

g = Button(master, text="Divide", command=div)
g.grid(row=16, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
master.mainloop()

 

