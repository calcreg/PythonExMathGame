
# Present subroutines:
# min(x,y), max(x,y)
# RhalfEllipse(xc,yc,a,b,N)
# Rsqrt(a,eps)
# DrawArrow(x1,y1,x2,y2,d,width,color1,color2)
# Use: DrawArrow(x1,y1,x2,y2,orientation(1 or -1),width, color1,color2)

# Various useful subroutines
def Rsign(x):
	if x<0: return '-'
	else: return ''

def max(x,y):
	if x<y: return y
	else: return x
def min(x,y):
	if x>y: return y
	else: return x

# ------- Subroutines essentially to display an arrow of various dimensions ---------

def RhalfEllipse(xc,yc,a,b,N):
	X=[]; Y=[]
	for i in range(0,N+1):
		x=-a+i*2*a/N
		X.append(xc+x)
		Y.append(yc+b*Rsqrt(1-x*x/(a*a),0.001))
	return X,Y

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

def DrawArrow(x1,y1,x2,y2,d,width,color1,color2):
	#d=-1 or 1 with regards to the positive or negative rotation
	norme=Rsqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2),0.01)
	a=0.5*norme
	xc=(x1+x2)/2;yc=(y1+y2)/2
	b=1.5*a; dl=width/2;N=15
	X1,Y1=RhalfEllipse(xc,yc,a-dl,b-dl,N)
	X2,Y2=RhalfEllipse(xc,yc,a+dl,b+dl,N)
	pts=[]
	#for i in range(N+1):
	for i in range(N):
		pts.append((X1[i],Y1[i]))
	#Make the tip of the arrow
	pts.append((X1[N-1]-2*dl,Y1[N-1]))
	pts.append( ( (X1[N]+X2[N])/2 , (Y1[N]+Y2[N])/2 ) )	
	pts.append((X2[N-1]+2*dl,Y2[N-1]))
	#print('x1,y1=',(X1[i],Y1[i]))
	#for i in range(0,N+1):
	for i in range(1,N+1):
		pts.append((X2[N-i],Y2[N-i]))
		#print('x2,y2=',(X2[i],Y2[i]))
	#Now turn the pts
	Newpts=[]
	cosa=(x2-x1)/norme
	if y2-y1<0: sina=-Rsqrt(1-cosa*cosa,0.001)
	else: sina=Rsqrt(1-cosa*cosa,0.001)
	for i in range(len(pts)):
		#x1=xc+(x-xc)*cosa - (y-yc)*sina
		#y1=yc+(x-xc)*sina + (y-yc)*cosa
		Newpts.append((xc+(pts[i][0]-xc)*cosa-(pts[i][1]-yc)*sina, yc+d*((pts[i][0]-xc)*sina+(pts[i][1]-yc)*cosa)))
	#can1.create_polygon(Newpts, dash=(4, 2), fill=color1, outline=color2, width=3)
	WSaveList.append(can1.create_polygon(Newpts, fill=color1, outline=color2, width=3))
#Examples:
#Use: DrawArrow(x1,y1,x2,y2,orientation(1 or -1),width, color1,color2)
#DrawArrow(100,340,100,300,-1,8,'red','black')
#right side downwards
#DrawArrow(100,340,100,300,-1,2,'red','black')
#right side upwards
#DrawArrow(150,340,150,300,1,2,'red','black')
#left side downwards
#DrawArrow(250,300,250,340,1,2,'red','black')
#left side upwards
#DrawArrow(300,300,300,340,-1,8,'red','black')

#Rprintf(r'Voici le tableau: $\obj_tab{1,8,0, Nombre de barquettes & 3 & 6 ; Prix en Euros & 4,5 & 9 } \times \frac{9}{6}$',10,350,'red','black')

# ---------------------------- horizontal and vertical graduated axis ------------------------
def DrawGradAxis(x0,y0,mode,Length,w,color,Lgrad,Master_Pos,Unit_grads,Master_Value,MaskList,AboveArrowTxt):
	global arial
# mode is a binary code:
#bit0	horizontal (0) / vertical(1)
#bit1	no graduations (0) / graduations (1)
#bit3 - bit2	display Only 0 and 1 (0) / Display all integers (1)/ Display all and with fractions(2)
#bit4	(0) None clickable axis / (1) = Axis is clickable

#MaskList contains the positions to display. Think as: after all options the mask is set above.
# MaskList uses a binary code: bit0 -> 0=do not display; 1=display
#								bit1 -> 1=arc arrow above with the next graduation left to right
#								bit2 -> 1=arcarrow above with the next graduation right to left
#								bit3 -> 1= put '?' at the graduation
#Master_Pos is taken in terms of graduations position
#x0,y0 left point in mode 0 and lower point in mode 1
#Unit_grads is the length of the unit in graduations


	a=min(Length,10)
	if mode & 1 ==0:
		WSaveList.append(can1.create_line(x0-Lgrad/2,y0,x0+Length,y0,width=w,fill=color))
		WSaveList.append(can1.create_line(x0+Length,y0,x0-a+Length,y0-a/2,width=w,fill=color))
		WSaveList.append(can1.create_line(x0+Length,y0,x0-a+Length,y0+a/2,width=w,fill=color))
	elif mode & 1 ==1:
		WSaveList.append(can1.create_line(x0,y0+Lgrad/2,x0,y0-Length,width=w,fill=color))
		WSaveList.append(can1.create_line(x0,y0-Length,x0-a/2,y0-Length+a,width=w,fill=color))
		WSaveList.append(can1.create_line(x0,y0-Length,x0+a/2,y0-Length+a,width=w,fill=color))
	
	if mode & 2 !=0:
		#display graduations
		b=3*w
		for i in range(int(Length/Lgrad)):
			if mode & 1 ==0: WSaveList.append(can1.create_line(x0+i*Lgrad,y0-b,x0+i*Lgrad,y0+b,width=w,fill=color))
			else :  WSaveList.append(can1.create_line(x0-b,y0-i*Lgrad,x0+b,y0-i*Lgrad,width=w,fill=color))
	
	if mode & 12 ==4 or mode & 12 ==8: #bit3-bit2=01 or 10 
		c=7*w
		#Unit_grads=Unit_Pos-Master_Pos
		#print(Unit_grads)
		delta=1/Unit_grads
		Ndiv=int(Length/Lgrad)
		GradFrac=[]
		for i in range(Ndiv): #Create a Fraction list (Numerator/denominator)
			GradFrac.append((i-Master_Pos+Master_Value*Unit_grads,Unit_grads))
		if Ndiv > len(MaskList): MaskList+=(Ndiv-len(MaskList))*[1] #We complete MaskList with ones
		ListDo=[]
		for i in range(Ndiv): 
			#Create the list to display those selected in the MaskList
			if MaskList[i] & 1 != 0: ListDo.append(i)
			#also Display the arc arrows wanted above the axis
			if MaskList[i] & 2 != 0:
				DrawArrow(x0+i*Lgrad,y0-2*w,x0+(i+1)*Lgrad,y0-2*w,-1,3,'red','red')
				Rprintf(AboveArrowTxt[i],x0+i*Lgrad,y0-Lgrad-arial.measure('_'),color,color)
			if MaskList[i] & 4 != 0:
				DrawArrow(x0+(i+1)*Lgrad,y0-2*w,x0+i*Lgrad,y0-2*w,1,3,'red','red')
				Rprintf(AboveArrowTxt[i],x0+i*Lgrad,y0-Lgrad-arial.measure('_'),color,color)
			if MaskList[i] & 8 != 0:
				arialsave=arial
				arial=arialLargeb;Rprintf('?',x0-arial.measure('?')/2+i*Lgrad,y0+c+arial.measure('?')/2,'red','red')
				arial=arialsave
		for i in ListDo: #Only do those in the mask
			if GradFrac[i][0]%GradFrac[i][1] ==0: #Display the integers
				a=GradFrac[i][0]/GradFrac[i][1]
				if mode & 1 ==0: WSaveList.append(can1.create_text(x0+i*Lgrad-arial.measure(str(int(a)))/2,y0+c+arial.measure('_')/2,anchor='w',text=str(int(a)),font=arial,fill=color))
				else : WSaveList.append(can1.create_text(x0-2*c-arial.measure(str(int(a))),y0-i*Lgrad,anchor='w',text=str(int(a)),font=arial,fill=color))
			elif mode & 12 ==8: #Display also the fractions
				str1='$'+str(Rsign(GradFrac[i][0]))+'\\frac{'+str(R_abs(GradFrac[i][0]))+'}{'+str(GradFrac[i][1])+'}$'
				#print(str1)
				if mode & 1 ==0:
					if GradFrac[i][0]<0:  Rprintf(str1,x0+i*Lgrad-7*arial.measure('_')/2,y0+2*c,'red',color)
					else: Rprintf(str1,x0+i*Lgrad-3*arial.measure('_')/2,y0+2*c,'red',color)
				else : 
					if GradFrac[i][0]<0:  Rprintf(str1,x0-2*c-7*arial.measure('_')/2,y0-i*Lgrad,'red',color)
					else: Rprintf(str1,x0-2*c-3*arial.measure('_')/2,y0-i*Lgrad,'red',color)

				
				#Rprintf(str1,x0-2*c-3*arial.measure('_')/2,y0+i*Lgrad,'red',color)
				
	if mode & 12 ==0:
			print('Mode Options bit3-bit2 = 00 unsupported, instead use 01 to display integers and use the mask')
	if mode & 16 == 16: #bit4==1
		#Create zones to click on small rectangles around graduations
		global ZoneCL
		ZoneCL=[]
		b=3*w
		#print('axis is clickable')
		for i in range(int(Length/Lgrad)):
			if mode & 1 ==0: rect=can1.create_rectangle(x0+i*Lgrad-w,y0-b,x0+i*Lgrad+w,y0+b,activefill='blue',outline='white',fill='black')
			if mode & 1 ==1: rect=can1.create_rectangle(x0-b,y0-i*Lgrad-w,x0+b,y0-i*Lgrad+w,activefill='blue',outline='white',fill='black')
			WSaveList.append(rect)
			ZoneCL.append((x0+i*Lgrad-w,y0-b,x0+i*Lgrad+w,y0+b,rect))
		
		
#Usage:			
#arial=arial12b
#disp=1;Rarc=2;Larc=4;Quid=8
#Mask=[1,Rarc+disp,Quid,0,1]
#Text=['','$+\\frac{1}{3}$','']

#DrawGradAxis(80,380,10,400,2,'black',50,5,3,-1,Mask,Text)
#DrawGradAxis(80,380,10,400,2,'black',50,0,3,0,Mask,Text)

#arial=arial14b