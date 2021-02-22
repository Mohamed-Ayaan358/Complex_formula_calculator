import math
import cmath

#AREA formulas
def trianglearea(*args):
	a=(args[1]*2)/args[0]
	return a

def squarearea(*args):
	a=math.sqrt(args[0])
	return a

def circlearea(*args):
	a=math.sqrt(args[0]/math.pi)
	return a

#VOLUME formulas
def cubevol(*args):
	a=(args[0]**(1/3))
	return a

def cuboidvol(*args):
	a=(args[2]/(args[0]*args[1]))
	return a

def spherevol(*args):
	a=((3*args[0])/(4*math.pi))**(1/3)
	return a

def hemisvol(*args):
	a=((3*args[0])/(2*math.pi))**(1/3)
	return a

def cylinvol(*args):
	if (args[2]=='R'):
		a=((args[1])/(args[0]*math.pi))**(1/2)
		return a
	elif (args[2]=='H'):
		a=((args[1])/((math.pi)*(args[0]**2)))
		return a

def conevol(*args):
	if (args[2]=='R'):
		a=((3*args[1])/(args[0]*math.pi))**(1/2)
		return a
	elif (args[2]=='H'):
		a=(3*(args[1])/((math.pi)*(args[0]**2)))



#CSA formulas
def cubecsa(*args):
	a=math.sqrt((args[0])/4)
	return a

def cuboidcsa(*args):
	if (args[3]=='L'):
		a=((args[2]/(2*args[1]))-args[0])
		return a
	elif (args[3]=='B'):
		a=((args[2]/(2*args[1]))-args[0])
		return a
	elif (args[3]=='H'):
		a=(args[2]/(2*(args[0]+args[1])))
		return a

def spherecsa(*args):
	a=(args[1]/(4*math.pi))**(1/2)
	return a

def hemiscsa(*args):
	a=(args[1]/(2*math.pi))**(1/2)
	return a

def cylincsa(*args):
	if (args[2]=='H'):
		a=(args[1]/(2*args[0]*math.pi))
		return a
	elif (args[2]=='R'):
		a=(args[1]/(2*args[0]*math.pi))
		return a

def conecsa(*args):
	if (args[2]=='L'):
		a=(args[1]/(args[0]*math.pi))
		return a
	elif (args[2]=='R'):
		a=(args[1]/(args[0]*math.pi))
		return a


#TSA formulas
def cubetsa(*args):
	a=math.sqrt((args[0])/6)
	return a

def cuboidtsa(*args):
	if (args[3]=='L'):
		a=(((args[2]/2)-(args[0]*args[1]))/(args[0]+args[1]))
		return a
	elif (args[3]=='B'):
		a=(((args[2]/2)-(args[0]*args[1]))/(args[0]+args[1]))
		return a
	elif(args[3]=='H'):
		a=(((args[2]/2)-(args[0]*args[1]))/(args[0]+args[1]))
		return a
def spheretsa():
	a=(args[1]/(4*math.pi))**(1/2)
	return a
def hemistsa(*args):
	a=(args[1]/(3*math.pi))**(1/2)
	return a
def cylintsa(*args):
	if(args[2]=='H'):
		a=(args[1]-(2*math.pi*((args[0])**(2))))/(2*math.pi*args[0])
		return a
	elif(args[2]=='R'):
		a=(args[0]**2)+(2*(args[1]/math.pi))
		b=((args[0])*(-1))
		c=(b+cmath.sqrt(a))/2
		return c
def conetsa(*args):
	if(args[2]=='L'):
		a=(args[1]-(math.pi*((args[0])**(2))))/(math.pi*args[0])
		return a
	elif (args[2]=='R'):
		a=(args[0]**2)+(4*(args[1]/math.pi))
		b=((args[0])*(-1))
		c=(b+cmath.sqrt(a))/2
		return c