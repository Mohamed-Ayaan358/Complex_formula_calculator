import math
def trianglearea(*args):
	a=args[0]*args[1]*0.5
	return a

def squarearea(*args):
	a=args[0]*args[1]
	return a

def circlearea(*args):
	a=math.pi *( args[0]**(2))
	return a

#Volume formulas

def cubevol(*args):
	a=args[0]**3
	return a

def cuboidvol(*args):
	a=args[0]*args[1]*args[2]
	return a

def spherevol(*args):
	a=(4/3)*math.pi*(args[0]**3)
	return a

def hemisvol(*args):
	a=(2/3)*math.pi*(args[0]**3)
	return a

def cylinvol(*args):
	a=math.pi*args[0]*(args[1]**2)
	return a

def conevol(*args):
	a=(1/3)*math.pi*args[0]*(args[1]**2)
	return a

#CSA formulas

def cubecsa(*args):
	a=4*(args[0]**2)
	return a

def cuboidcsa(*args):
	a=2*(args[2])*(args[0]+args[1])
	return a

def spherecsa(*args):
	a=4*(math.pi*(args[0]**2))
	return a

def hemiscsa(*args):
	a=2*(math.pi*(args[0]**2))
	return a

def cylincsa(*args):
	a=2*(math.pi*args[0]*args[1])
	return a

def conecsa(*args):
	a=math.pi*args[1]*args[0]
	return a

#TSA formulas

def cubetsa(*args):
	a=6*(args[0]**2)
	return a

def cuboidtsa(*args):
	a=2*((args[0]*args[1])+(args[1]*args[2])+(args[2]*args[0]))
	return a

def spheretsa(*args):
	a=4*(math.pi*(args[0]**2))
	return a

def hemistsa(*args):
	a=3*(math.pi*(args[0]**2))
	return a

def cylintsa(*args):
	a=(2*(math.pi*args[1]*args[0]))+(2*(math.pi)*(args[1]**2))
	return a

def conetsa(*args):
	a=math.pi*args[1]*(args[1]+args[0])
	return a

























