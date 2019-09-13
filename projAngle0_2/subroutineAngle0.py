

pi=3.1415927
def Rsqrt(a,eps): #esp is the precision required
	#returns sqrt(a); We use Newton's algorithm
	#x0=u0-f(u0)/f'(u0)
	#we go until dx<=eps
	if a <0:
		print('error trying sqrt of negative number')
		return -1
	if a==0: return 0
	x=a; #We start large for x>1 x>sqrtx (but careful for x<1  sqrt x >x )
	if a < 1:
		x=1/a
	x0=x 
	dx=1+eps
	#print('dx=',dx)
	while dx > eps:
		x1=0.5*(x0+x/x0)
		dx=x0-x1 #the suite of the xi is decreasing
		#print('a,x1,dx=',a,x1,dx)
		x0=x1
	if a >= 1: return x0
	else: return 1/x0
def Rcos(theta):
	#print(theta)
	#Only angles in [0,2*pi]
	if theta <0: theta=-theta #Cosine parity
	a=pi/20
	Lcos=[(0,1),(a,0.9876),(2*a,0.951),(3*a,0.891),(4*a,0.809),
		(5*a,0.7071),(6*a,0.5877),(7*a,0.4539),(8*a,0.309),(9*a,0.1564),
		(10*a,0)]
	#theta is in radian
	#We define the cosine roughtly
	def minicos(theta):
		for i in range(10):
			if Lcos[i][0] <= theta <= Lcos[i+1][0]:
				return Lcos[i][1]+(theta-Lcos[i][0])*(Lcos[i+1][1]-Lcos[i][1])/(Lcos[i+1][0]-Lcos[i][0])
		print('problème dans minicos')

	if 0 <= theta <= pi/2 :
		return minicos(theta)
	if pi/2 <= theta <= pi :
		return -minicos(pi-theta)
	if pi <= theta <= 3*pi/2 :
		return -minicos(theta-pi)
	if 3*pi/2 <= theta <= 2*pi :
		return minicos(2*pi-theta)

def Rsin(theta):
	return Rcos(-pi/2+theta)

def DrawAngle(x0,y0,x1,y1,theta,color):
	#draws 2 lines. One at position (x0,y0)-(x1,y1) 
	#The other line is drawn with regards to theta
	WSaveList.append(can1.create_line(x0,y0,x1,y1,width=2,fill=color))
	#L=Rsqrt((x1-x0)** + (y1-y0)**)
	ux=x1-x0; uy=y1-y0
	xs=x0 + ux*Rcos(theta) - uy*Rsin(theta)
	ys=y0 + ux*Rsin(theta) + uy*Rcos(theta)
	WSaveList.append(can1.create_line(x0,y0,xs,ys,width=2,fill=color))
	#Warning, (xs,ys) is returned at the exit of this subroutine
	#this is to help locate the end of the segment of the angle for ZoneCL
	
	#Trace the arc circle to locate the angle
	xm=x0+0.2*(x1-x0)
	ym=y0+0.2*(y1-y0)
	ux=xm-x0; uy=ym-y0
	N=10
	for i in range(N-1):
		x2=x0 + ux*Rcos(theta/(N-1)) - uy*Rsin(theta/(N-1))
		y2=y0 + ux*Rsin(theta/(N-1)) + uy*Rcos(theta/(N-1))
		WSaveList.append(can1.create_line(xm,ym,x2,y2,width=2,fill=color))
		xm=x2; ym=y2
		ux=xm-x0; uy=ym-y0
	return (xs,ys)

#DrawAngle(100,300,250,300,50*pi/180,'red')
#for i in range(40):
#	print ('cos(',i*pi/20,')=',Rcos(i*pi/20))

#for i in range(40):
#	print ('sin(',i*pi/20,')=',Rsin(i*pi/20))



