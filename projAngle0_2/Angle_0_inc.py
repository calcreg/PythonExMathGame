
QuestionList=[]

def Angle_Init(hy):
	global MatDim,Session,SessionInit
	# DIM=[x,y,Nx]
	#     [X,Y,Ny]   Remarque: Nx est le nombre de carreaux sur une ligne
	w=WidthCan1; wTab=320; xTab=int((WidthCan1-wTab)/2)
	#hy=120
	#print('hy=',hy)
	MatDim=([[xTab,hy,4],[xTab+wTab,hy+50,1]])
	Quadrillage(MatDim) #Construction visuelle de la grille ou tableau à cliquer
	#for Session in range(1,6): #Concrètement de 1 à 5
	Session=1 #Initialisation de la session de 5 questions sur le thème ci-dessous
	DispSession(Session) #Affichage texte
	SessionInit=0 # On le fait passer à 0 puisque l'initialisation a été effectuée
	#Init a list to avoid same values on questions
	QuestionList.clear()

def GetmatPerm(n): #Get a permutation matrix
	matPerm=[]
	for i in range(0,n):
		matPerm.append(i)
	for i in range(0,n):
		p=randrange(n)
		p1=matPerm[p]
		p0=matPerm[0]
		matPerm[0]=p1
		matPerm[p]=p0
	return matPerm

def Ralea1(n):# => génère un nombre aléatoire de 1 à n-1
	if n <= 1: print('Ralea1: n<=1 error! n=',n)
	a = randrange(n)             
	while a==0 : 
		a = randrange(n)             # => génère un nombre aléatoire de 0 à n-1
	return a
def Ralea2(n):# => génère un nombre aléatoire de 2 à n-1
	if n <= 2: print('Ralea2 : n<=2 error! should be minimum 3. n=',n)
	a = randrange(n)             
	while a==0 or a==1: 
		a = randrange(n)             # => génère un nombre aléatoire de 0 à n-1
	return a
def Ralea3(n):# => génère un nombre aléatoire de 3 à n-1
	if n<3:
		print('Ralea3: n<3 error! should be above or equal to 3 at least.')
		return 3
	a = randrange(n)
	while a==0 or a==1 or a==2: 
		a = randrange(n)             # => génère un nombre aléatoire de 0 à n-1
	return a


def QAlreadyDone(value):
	for i in range(len(QuestionList)):
		#print(QuestionList)
		if value == QuestionList[i]:
			#print('removed already given value')
			return -1
	return 0 # value not in QuestionList
	

# --------------- Angle 0_0 -----------------
Cours_Angle0_0=r""
#arial=arial12b;RdispText(myBigtext,0,170,25,'red','blue');arial=arial14b
def JeuAngles0_0():
	global deltaScore,NbreBonneReponse,SessionInit,Method
	Method=1;deltaScore=1


	X0text=10;Y0text=40
	if SessionInit==1:
		Angle_Init(Y0text+300) #On initialise au début de la session.Tableau de réponse,etc
	y_cours=240
	#Création d'une permutation aléatoire
	matPerm=GetmatPerm(4)
	
	angle=int(1+Ralea1(180)/10)*10
	while QAlreadyDone(angle) != 0:
		angle=int(1+Ralea1(180)/10)*10
	QuestionList.append(angle)

#Usage: \obj_rect{width, height, nbr col, nbr rows,color inside, color dashed, nbre square colored}
# $\obj_rect{60,20,1,1,9,6,1}$ is fully colored by color 6 = blue
# $\obj_rect{60,20,1,1,9,6,0}$ is empty color by inside color 9 = white
# Bien faire attention dans Enonce0_0 à la fin du texte à r"}$.\n" car ce sont des caractères spéciaux
	Enonce0_0=r"Quel est la mesure de l'angle ci-dessous ? "
	#print(Enonce0_0)
	RdispText(Enonce0_0,X0text,Y0text,27,'black','blue');
	Lcolors=['red','green','blue','black','orange']
	color=Lcolors[randrange(5)]
	if Session < 3 :
		DrawAngle(X0text+200,Y0text+250,X0text+400,Y0text+250,-angle*pi/180,color)
	else:
		DrawAngle(X0text+300,Y0text+250,X0text+100,Y0text+250,angle*pi/180,color)

	#print(matPerm)
	NbreBonneReponse=matPerm[0] #Pour la vérification avec HandleGame	
	#print('bonne réponse=',matPerm[0])
	str2='$    '+str(angle)+'^{o}$'
	PlaceTxt(MatDim,matPerm[0],str2,'red','black') #matPerm[0] est toujours la bonne réponse

	if angle != 90: str2='$    '+str(180-angle)+'^{o}$'
	else: str2='$    '+str(50)+'^{o}$' 
	PlaceTxt(MatDim,matPerm[1],str2,'red','black')

	str2='$    '+str(angle+30)+'^{o}$'
	PlaceTxt(MatDim,matPerm[2],str2,'red','black')

	str2='$    '+str(int(angle/2)+12)+'^{o}$'
	PlaceTxt(MatDim,matPerm[3],str2,'red','black')



# --------------- Angle 0_1 -----------------

def JeuAngles0_1():
	global deltaScore,NbreBonneReponse,SessionInit,Method
	Method=1;deltaScore=1

	X0text=10;Y0text=40
	if SessionInit==1:
		Angle_Init(Y0text+300) #On initialise au début de la session.Tableau de réponse,etc
	y_cours=240
	#Création d'une permutation aléatoire
	matPerm=GetmatPerm(4)
	
	angle=int(1+Ralea1(180)/10)*10
	while QAlreadyDone(angle) != 0:
		angle=int(1+Ralea1(180)/10)*10
	QuestionList.append(angle)

	Enonce0_1=r"Quel est la mesure de l'angle ci-dessous ? "

	RdispText(Enonce0_1,X0text,Y0text,27,'black','blue');
	Lcolors=['red','green','blue','black','orange']
	color=Lcolors[randrange(5)]
	if Ralea1(10) > 5 : DrawAngle(X0text+200,Y0text+80,X0text+400,Y0text+Ralea1(30),angle*pi/180,color)
	else: DrawAngle(X0text+300,Y0text+80,X0text+100,Y0text+20+Ralea1(30),-angle*pi/180,color)

	NbreBonneReponse=matPerm[0] #Pour la vérification avec HandleGame	
	#print('bonne réponse=',matPerm[0])
	str2='$    '+str(angle)+'^{o}$'
	PlaceTxt(MatDim,matPerm[0],str2,'red','black') #matPerm[0] est toujours la bonne réponse

	if angle != 90: str2='$    '+str(180-angle)+'^{o}$'
	else: str2='$    '+str(50)+'^{o}$' 
	PlaceTxt(MatDim,matPerm[1],str2,'red','black')

	str2='$    '+str(angle+30)+'^{o}$'
	PlaceTxt(MatDim,matPerm[2],str2,'red','black')

	str2='$    '+str(int(angle/2)+12)+'^{o}$'
	PlaceTxt(MatDim,matPerm[3],str2,'red','black')


	
# --------------- Angle 0_2 -----------------

def JeuAngles0_2():
	global ZoneCL,deltaScore,NbreBonneReponse,Session,SessionInit,Method
	Method=2;deltaScore=1

	#Initialisation
	if SessionInit==1:
		#empty QuestionList This is the list which contains the angles already 
		#asked in this session.
		QuestionList.clear()
		Session=1 #Initialisation de la session de 5 questions sur le thème ci-dessous
		DispSession(Session) #Affichage texte
		DeleteQuadrillage(carreau)
		SessionInit=0

	angle=int(1+Ralea1(180)/10)*10
	while QAlreadyDone(angle) != 0:
		angle=int(1+Ralea1(180)/10)*10
	QuestionList.append(angle)

	X0text=10;Y0text=40
	Enonce0_1=r"Clique dans le bon rectangle pour choisir la bonne\n" \
			  r" mesure de l'angle de $"+ str(angle) + r"^{o}$ ."

	Lcolor=['#9999FF','#FF9999','#9999FF','#FF9999','#9999FF','#FF9999']
	RdispText(Enonce0_1,X0text,Y0text,27,'black','blue');

	#The idea is to create clickable rectangles in ZoneCL which define
	#positions of lines.
	#One line (therefore one rectangle) is solution to end the drawing 
	#of the correct angle.
		
	ZoneCL.clear()
	#ZoneCL contains a list of ...,(x0,y0,x1,y1,rect_handler),...
	b=9
	#To change colors at each session
	if Session < 3:
		x0m=X0text+240; y0m=Y0text+300
		xm=X0text+400; ym=Y0text+300
		for i in range(19):
			#print(i)
			(x1,y1)=DrawAngle(x0m,y0m,xm+40,ym,-i*pi/18,Lcolor[Session])
			rect=can1.create_rectangle(x1-b,y1-b,x1+b,y1+b,activefill='#9999FF',outline='black',fill='black')
			WSaveList.append(rect) #Important so that it is washed away with next question
			ZoneCL.append( (x1-b,y1-b,x1+b,y1+b,rect))
		#The first segment
		WSaveList.append(can1.create_line(x0m,y0m,xm,ym,width=4,fill='black'))
	else:
		x0m=X0text+240; y0m=Y0text+300
		xm=X0text+40; ym=Y0text+300
		for i in range(19):
			#print(i)
			(x1,y1)=DrawAngle(x0m,y0m,xm,ym,i*pi/18,Lcolor[Session])
			rect=can1.create_rectangle(x1-b,y1-b,x1+b,y1+b,activefill='blue',outline='black',fill='black')
			WSaveList.append(rect) #Important so that it is washed away with next question
			ZoneCL.append( (x1-b,y1-b,x1+b,y1+b,rect))
		#The first segment
		WSaveList.append(can1.create_line(x0m,y0m,xm,ym,width=4,fill='black'))
	global X0m,Y0m
	X0m=x0m; Y0m=y0m #Important to be used in MouseMoves
	NbreBonneReponse=int(angle/10) #We have only 19 possibilities 0 to 180
	can1.bind('<Motion>',MouseMoves) #This is to detect mouse moves and display
	#At each session it is unbound with UnbindPreviousBinds() in ExAngles.py
	#Then it is bound again here.
	
	
X0m=0;Y0m=0;anglehdle=0
def MouseMoves(event):
	global anglehdle
	if Method !=2 :
		print('MouseMoves with ZoneCL It should be used with Method 2')
		return
	i=event.x
	j=event.y
	Nbre=GetNbre2(ZoneCL,i,j)
	if Nbre != -1:
		x0=ZoneCL[Nbre][0]
		y0=ZoneCL[Nbre][1]
		x1=ZoneCL[Nbre][2]
		y1=ZoneCL[Nbre][3]
		xm=X0m+0.8*((x0+x1)/2-X0m)
		ym=Y0m+0.8*((y0+y1)/2-Y0m)
		if anglehdle!=0: can1.delete(anglehdle)
		anglehdle=can1.create_line(X0m,Y0m,xm,ym,width=4,fill='black')
	
	#Remark: After each exit of any Session, <Motion> is unbound in ExAngles0.py/UnbindPreviousBinds()

	
# --------------- Angle 1_0 -----------------

def JeuAngles1_0():
	global deltaScore,NbreBonneReponse,SessionInit,Method
	Method=1;deltaScore=1

	X0text=10;Y0text=40
	if SessionInit==1:
		Angle_Init(Y0text+300) #On initialise au début de la session.Tableau de réponse,etc
	y_cours=240
	#Création d'une permutation aléatoire
	matPerm=GetmatPerm(4)
	
	angle=int(1+Ralea1(180)/10)*10
	while QAlreadyDone(angle) != 0:
		angle=int(1+Ralea1(180)/10)*10
	QuestionList.append(angle)

	Enonce0_1=r"Comment s'appelle l'angle ci-dessous ?"

	RdispText(Enonce0_1,X0text,Y0text,27,'black','blue');

	#chr(65)='A';chr(90)='Z';  chr(97)=a ; chr(122)=z
	Submit = chr(65+randrange(8)) #Letter for the submit of the angle
	side1 = chr(115+randrange(8)) #Letter for a side
	side2 = chr(115+randrange(8)) #Letter for a side
	while side1 == side2:
		side2 = chr(115+randrange(8)) #Letter for a side

	Lcolors=['red','green','blue','grey','orange']
	color=Lcolors[randrange(5)]
	if Ralea1(10) > 5 :
		xs = X0text+200 ; ys = Y0text+80 
		xm = X0text+400 ; ym =Y0text+Ralea1(30)
		(xe,ye)=DrawAngle(xs,ys,xm,ym,angle*pi/180,color)
		Rprintf(side1,xs+0.6*(xm-xs),ys+0.6*(ym-ys)-10,'black','black')
		Rprintf(side2,xs+0.6*(xe-xs),ys+0.6*(ye-ys)+10,'black','black')
		Sx=xm-xs+xe-xs; Sy=ym-ys+ye-ys
		L=Rsqrt(Sx*Sx + Sy*Sy,0.001)
		if L==0: L=1 #L==0 can happen if vect1=-vect2
		Rprintf(Submit,xs-15*Sx/L,ys-15*Sy/L,'black','black') #We move away the Letter from the submit
		
	else:
		xs = X0text+200 ; ys = Y0text+80
		xm = X0text+100 ; ym =Y0text+20+Ralea1(30)
		(xe,ye)=DrawAngle(xs,ys,xm,ym,-angle*pi/180,color)
		Rprintf(side1,xs+0.6*(xm-xs),ys+0.6*(ym-ys)-10,'black','black')
		Rprintf(side2,xs+0.6*(xe-xs),ys+0.6*(ye-ys)+10,'black','black')
		#Display Submit name		
		Sx=xm-xs+xe-xs; Sy=ym-ys+ye-ys
		L=Rsqrt(Sx*Sx + Sy*Sy,0.001)
		if L==0: print('La norme du vecteur somme ne devrait pas être nulle')
		Rprintf(Submit,xs-10*Sx/L,ys-10*Sy/L,'black','black') #We move away the Letter from the submit

	
	NbreBonneReponse=matPerm[0] #Pour la vérification avec HandleGame	
	#print('bonne réponse=',matPerm[0])
	str2='$    \widehat{'+side1+Submit+side2+'} $'
	PlaceTxt(MatDim,matPerm[0],str2,'red','black') #matPerm[0] est toujours la bonne réponse

	str2='$    \widehat{'+side1+side2+Submit+'} $'
	PlaceTxt(MatDim,matPerm[1],str2,'red','black')

	str2='$    \widehat{'+Submit+side2+side1+'} $'
	PlaceTxt(MatDim,matPerm[2],str2,'red','black')

	str2='$    \widehat{'+side2+side1+Submit+'} $'
	PlaceTxt(MatDim,matPerm[3],str2,'red','black')

