import mymath
from tkinter import *
from tkinter import ttk

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
Label(master, text="RESULT:").grid(row=14, sticky=W)

m=StringVar();
ttk.Label(master, text ="OPERATION").grid(row = 4) 

resul=Label(master, text="", textvariable=myText).grid(row=14,column=1, sticky=W)
	

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = '        '

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4,column=1)
def c():
	b = Button(master, text="Calculate", command=calc)
	b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)

c()
master.mainloop()
