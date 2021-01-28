import mymath
from tkinter import *

def add():
	res=(float(e7.get())+float(e8.get()))
	myText.set(res)

def sub():
	res=(float(e7.get())-float(e8.get()))
	myText.set(res)

def mult():
	res=(float(e7.get())*float(e8.get()))
	myText.set(res)

def div():
	res=(float(e7.get())/float(e8.get()))
	myText.set(res)

def form():
	ro = Tk()
	S = Scrollbar(ro)
	T = Text(ro, height=22, width=50)
	S.pack(side=RIGHT, fill=Y)
	T.pack(side=LEFT, fill=Y)
	S.config(command=T.yview)
	T.config(yscrollcommand=S.set)
	Formulas ="""FORMULAS 1.trianglearea (b,h)
	 2.squarearea (l)
	 3.circlearea (r)
	 4.cubevol (l)
	 5.cuboidvol (l,b,h)
	 6.spherevol (r)
	 7.hemisvol (r)
	 8.cylinvol (r,h)
	 9.conevol (r,l)
	 10.cubecsa (l)
	 11.cuboidcsa (l,b,h)
	 12.spherecsa (r)
	 13.hemiscsa (r)
	 14.cylincsa (r,h)
	 15.conecsa (r,l)
	 16.cubetsa (l)
	 17.cuboidtsa (l,b,h)
	 18.spheretsa (r)
	 19.hemistsa (r)
	 20.cylintsa (r,h)
	 21.conetsa (r,l)"""
	T.insert(END, Formulas)
	ro.mainloop()

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
myText=StringVar();
Label(master, text="LENGTH").grid(row=0, sticky=W)
Label(master, text="BREATH").grid(row=1, sticky=W)
Label(master, text="HEIGHT").grid(row=2, sticky=W)
Label(master, text="RADIUS").grid(row=3, sticky=W)
Label(master, text="OPERATION").grid(row=4,sticky=W)
Label(master, text="NOTE:").grid(row=7, sticky=W)
Label(master, text="NUMBER 1").grid(row=10, sticky=W)
Label(master, text="NUMBER 2").grid(row=12, sticky=W)
Label(master, text="RESULT:").grid(row=14, sticky=W)
resul=Label(master, text="", textvariable=myText).grid(row=14,column=1, sticky=W)


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

def c():
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

	h = Button(master, text="Formulas", command=form)
	h.grid(row=18, column=1,columnspan=1, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)

c()	
master.mainloop()
