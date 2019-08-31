

def Frac_Init(hy):
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

# --------------- FRACTIONS 0_0 -----------------
Cours_Frac0_0=r"On considère une unité $\obj_rect{60,20,1,1,8,6,0}$.\n"\
		r"On la partage en 6 : $\obj_rect{60,20,3,2,8,6,0}$.\n"\
		r" \nDonc 6 petits carreaux forment une unité.\n"\
		r"On en colorie 4 sur les 6: $\obj_rect{60,20,3,2,8,6,4} = \frac{4}{6}$\n"\
		r" \nPlus compliqué:\n"\
		r"                             $\obj_rect{60,20,3,2,8,6,4}+\obj_rect{60,20,3,2,8,6,3} = \frac{7}{6}$\n"
#arial=arial12b;RdispText(myBigtext,0,170,25,'red','blue');arial=arial14b
def JeuFraction0_0():
	global NbreBonneReponse,SessionInit,Method
	Method=1
	if SessionInit==1:
		Frac_Init(120) #On initialise au début de la session.Tableau de réponse,etc
	y_cours=240
	arial=arial12b;RdispText(r'COURS:',0,y_cours,27,'red','blue');arial=arial14b
	arial=arial12b;RdispText(Cours_Frac0_0,100,y_cours,27,'black','blue');arial=arial14b
	linehdle=can1.create_line(0,y_cours-15,WidthCan1,y_cours-15,width=4,fill='red')
	WSaveList.append(linehdle)
	#Création d'une permutation aléatoire
	X0text=10;Y0text=40
	matPerm=GetmatPerm(4)
	a=Ralea1(4)
	b=Ralea2(3)
	c=Ralea2(a*b+1)

#Usage: \obj_rect{width, height, nbr col, nbr rows,color inside, color dashed, nbre square colored}
# $\obj_rect{60,20,1,1,9,6,1}$ is fully colored by color 6 = blue
# $\obj_rect{60,20,1,1,9,6,0}$ is empty color by inside color 9 = white
# Bien faire attention dans Enonce0_0 à la fin du texte à r"}$.\n" car ce sont des caractères spéciaux
	Enonce0_0=r"Soit $\obj_rect{60,20,1,1,8,6,0}$ une unité.\n"\
	r"On colorie une partie: $\obj_rect{60,20,"+str(a)+","+str(b)+",8,6,"+str(c)+r"}$.\n"\
	"Quelle fraction de l'unité représente la partie bleue?"
	#print(Enonce0_0)
	RdispText(Enonce0_0,X0text,Y0text,27,'black','blue');

	#print(matPerm)
	NbreBonneReponse=matPerm[0] #Pour la vérification avec HandleGame	
	#print('bonne réponse=',matPerm[0])
	str2='$    \\frac{'+str(c)+'}{'+str(a*b)+'}$'
	PlaceTxt(MatDim,matPerm[0],str2,'red','black') #matPerm[0] est toujours la bonne réponse

	if a*b-c!=c : str2='$     \\frac{'+str(a*b-c)+'}{'+str(a*b)+'}$'
	else: str2='$     \\frac{'+str(c+1)+'}{'+str(a*b)+'}$'
	PlaceTxt(MatDim,matPerm[1],str2,'red','black')

	if a!=c or b!=a*b: str2='$    \\frac{'+str(a)+'}{'+str(b)+'}$'
	else: str2='$    \\frac{'+str(a)+'}{'+str(b+1)+'}$'
	PlaceTxt(MatDim,matPerm[2],str2,'red','black')

	if a*b-c!=c or c!=a*b: str2='$    \\frac{'+str(a*b-c)+'}{'+str(c)+'}$'
	else:  str2='$    \\frac{'+str(a*b-c+3)+'}{'+str(c+1)+'}$'
	PlaceTxt(MatDim,matPerm[3],str2,'red','black')

# --------------- FRACTIONS 0_1 -----------------

def JeuFraction0_1():
	global NbreBonneReponse,SessionInit,Method
	Method=1
	yPosTab=160
	if SessionInit==1:
		Frac_Init(yPosTab) #On initialise au début de la session.
	#Création d'une permutation aléatoire
	X0text=10;Y0text=yPosTab-90
	matPerm=GetmatPerm(4)
	a=Ralea2(4)
	b=Ralea1(3)
	c=Ralea1(a*b)
	d=Ralea1(a*b)
	if Session<=2: c=a*b #This is to force having a first complete unit

#Usage: \obj_rect{width, height, nbr col, nbr rows,color inside, color dashed, nbre square colored}
# $\obj_rect{60,20,1,1,9,6,1}$ is fully colored by color 6 = blue
# $\obj_rect{60,20,1,1,9,6,0}$ is empty color by inside color 9 = white
# Bien faire attention dans Enonce0_0 à la fin du texte à r"}$.\n" car ce sont des caractères spéciaux

	NbreBonneReponse=matPerm[0] #Pour la vérification avec HandleGame	

	if Session!=3:
		Enonce0_0=r"On donne l'unité suivante: $\obj_rect{70,20,1,1,8,6,0}$.\n"\
		r"Quelle fraction de l'unité la somme des carreaux bleus \n suivante représente-t-elle ?:            "\
		r"$\obj_rect{70,20,"+str(a)+","+str(b)+",8,6,"+str(c)+r"} + \obj_rect{70,20,"+str(a)+","+str(b)+",8,6,"+str(d)+r"}$.\n"\

		#print(Enonce0_0)
		RdispText(Enonce0_0,X0text,Y0text,28,'black','blue');
	
		str2='$    \\frac{'+str(c+d)+'}{'+str(a*b)+'}$'
		PlaceTxt(MatDim,matPerm[0],str2,'red','black') #matPerm[0] est toujours la bonne réponse

		str2='$     \\frac{'+str(c)+'}{'+str(a*b)+'}$'
		PlaceTxt(MatDim,matPerm[1],str2,'red','black')

		if c/(a*b) != d/b: str2='$    \\frac{'+str(d)+'}{'+str(b)+'}$'
		else:  str2='$    \\frac{'+str(d+1)+'}{'+str(b)+'}$'
		PlaceTxt(MatDim,matPerm[2],str2,'red','black')

		str2='$    \\frac{'+str(c+d)+'}{'+str(2*a*b)+'}$'
		PlaceTxt(MatDim,matPerm[3],str2,'red','black')
	else: #Pour Session==3
		a=3;b=2
		c=Ralea1(3)
		d=Ralea1(3)
		Enonce0_0=r"On donne l'unité suivante: $\obj_rect{70,20,1,1,8,6,0}$.\n"\
		r"Quelle fraction de l'unité la somme des carreaux bleus \n suivante représente-t-elle ?:            "\
		r"$\obj_rect{70,20,"+str(a)+","+str(b)+",8,6,"+str(c)+r"} + \obj_rect{70,20,"+str(a)+","+str(b)+",8,6,"+str(d)+r"}$.\n"\

		#print(Enonce0_0)
		RdispText(Enonce0_0,X0text,Y0text,28,'black','blue');
	
		str2=r" $\obj_rect{70,20,"+str(a)+","+str(b)+",8,6,"+str(c+d)+r"}$"
		#print ('str2='+str2)
		PlaceTxt(MatDim,matPerm[0],str2,'red','black') #matPerm[0] est toujours la bonne réponse

		str2=r" $\obj_rect{70,20,"+str(a)+","+str(b)+",8,6,"+str(c)+r"}$"
		PlaceTxt(MatDim,matPerm[1],str2,'red','black')

		if c!=d: str2=r" $\obj_rect{70,20,"+str(a)+","+str(b)+",8,6,"+str(d)+r"}$"
		else: str2=r" $\obj_rect{70,20,4,"+str(b)+",8,6,"+str(c+d)+r"}$"
		PlaceTxt(MatDim,matPerm[2],str2,'red','black')

		str2=r" $\obj_rect{70,20,"+str(a)+",3,8,6,"+str(c)+r"}$"
		PlaceTxt(MatDim,matPerm[3],str2,'red','black')


# --------------- FRACTIONS 0_2 -----------------

def JeuFraction0_2():
	#On ajoute des fractions, le dénominateur de l'une est le double ou triple de l'autre
	global NbreBonneReponse,SessionInit,Method
	Method=1
	if SessionInit==1:
		Frac_Init(160) #On initialise au début de la session.
	X0text=30;Y0text=70
	#Création d'une permutation aléatoire pour dispatcher les réponses possibles sur la grille
	matPerm=GetmatPerm(4)
	a=Ralea2(5)
	b=Ralea1(3)
	c=Ralea1(a*b)
	d=Ralea1(a*b)
	Enonce0_2=r"On donne l'unité suivante: $\obj_rect{70,20,1,1,8,6,0}$.\n"\
			r"La somme $\obj_rect{70,20,"+str(a)+r","+str(b)+r",8,6,"+str(c)+r"} + "\
			r"\obj_rect{70,20,"+str(a)+","+str(b)+",8,6,"+str(d)+r"}$ est égal à :"
	#Careful, do not use Rprintf here as it can only handle one line.
	#Use instead TdispText which can handle several lines display
	RdispText(Enonce0_2,X0text,Y0text,28,'black','blue')

	NbreBonneReponse=matPerm[0] #Pour la vérification avec HandleGame	
	#Remark: The answer is fraction (c+d)/(a*b)
	#We want to have an integer (euclidien division:(c+d)//(a*b) + fraction below 1 (rest (c+d)%(a*b) over (a*b)
	if (c+d)//(a*b) != 0: str2='  '+str((c+d)//(a*b))
	else: str2='  '
	if (c+d)//(a*b) != 0 and (c+d)%(a*b)!=0: str2+=' + '
	if (c+d)%(a*b)!=0: str2+='$\\frac{'+str((c+d)%(a*b))+'}{'+str((a*b))+'}$'
	else: str2='    '+str2 #To place in middle of th rectangle
	PlaceTxt(MatDim,matPerm[0],str2,'black','black') 
	#matPerm[0] est toujours la bonne réponse

	if (c+d)//(a*b)+a*b!= 0: str2='  '+ str((c+d)//(a*b)+a*b)
	else: str2='  '
	if (c+d)//(a*b)+a*b!= 0 and (c+d)%(a*b)!=0: str2+=' + '
	if (c+d)%(a*b)!=0: str2+='$\\frac{'+str((c+d)%(a*b))+'}{'+str((a*b))+'}$'
	else: str2='     '+str2 #To place in middle of th rectangle
	if str2.count(' ')==len(str2): str2='   0  ' #We test if 0 should be written
	PlaceTxt(MatDim,matPerm[1],str2,'black','black')

	if (c+d)//(a*b) != 0: str2='  '+str((c+d)//(a*b))
	else: str2='  '
	if (c+d)//(a*b) != 0 and (c+d+1)%(a*b)!=0: str2+=' + '
	if (c+d+1)%(a*b)!=0: str2+='$\\frac{'+str(c+d+1)+'}{'+str((a*b))+'}$'
	else: str2='     '+str2 #To place in middle of the rectangle
	if str2.count(' ')==len(str2): str2='   0  ' #We test if 0 should be written
	PlaceTxt(MatDim,matPerm[2],str2,'black','black')

	str2='     $\\frac{'+str(a*b)+'}{'+str(2*c+d)+'}$'
	PlaceTxt(MatDim,matPerm[3],str2,'black','black')


# --------------- FRACTIONS 1_0 -----------------

def JeuFraction1_0():
	global NbreBonneReponse,SessionInit,Method
	Method=1
	if SessionInit==1:
		Frac_Init(160) #On initialise au début de la session.
	#Création d'une permutation aléatoire
	X0text=30;Y0text=70
	matPerm=GetmatPerm(4)
	a=Ralea2(10)
	b=Ralea2(10)
	c=Ralea2(10)

	str1='$\\frac{'+str(a)+'}{'+str(c)+'}'+'+\\frac{'+str(b)+'}{'+str(c)+'}$'
	Rprintf('Détermine combien fait '+str1,X0text,Y0text,'black','blue')

	#print(matPerm)
	NbreBonneReponse=matPerm[0] #Pour la vérification avec HandleGame	
	#print('bonne réponse=',matPerm[0])
	str2='$    \\frac{'+str(a+b)+'}{'+str(c)+'}$'
	PlaceTxt(MatDim,matPerm[0],str2,'red','black') #matPerm[0] est toujours la bonne réponse

	str2='$     \\frac{'+str(int(R_abs(a+b)/2))+'}{'+str(c)+'}$'
	PlaceTxt(MatDim,matPerm[1],str2,'red','black')

	str2='$    \\frac{'+str(R_abs(a+b))+'}{'+str(c+c)+'}$'
	PlaceTxt(MatDim,matPerm[2],str2,'red','black')

	str2='$    \\frac{'+str(R_abs(a-b))+'}{'+str(c+c)+'}$'
	PlaceTxt(MatDim,matPerm[3],str2,'red','black')


# --------------- FRACTIONS 1_1 -----------------
Cours_Frac1_1=r"Pour additionner deux fractions, les dénominateurs \n"\
		r"doivent être les mêmes.\n"\
		r"En effet, la division de l'unité de référence doit être la \n"\
		r"même. On doit donc trouver un moyen d'obtenir une\n"\
		r" division identique sans changer la proportion.\n Voici un exemple:\n"\
		r"$\frac{2}{3} + \frac{3}{6} = \obj_rect{60,20,3,1,8,6,2} + \obj_rect{60,20,3,2,8,6,3}$ \n"\
		r"Tu peux remarquer que:        $\obj_rect{60,20,3,1,8,6,2} = \obj_rect{60,20,3,2,8,6,4}$\n"\
		r"On en conclut : $\obj_rect{60,20,3,2,8,6,4} + \obj_rect{60,20,3,2,8,6,3} = \frac{7}{6}$"
def JeuFraction1_1():
	#On ajoute des fractions, le dénominateur de l'une est le double ou triple de l'autre
	global NbreBonneReponse,SessionInit,Method
	Method=1
	if SessionInit==1:
		Frac_Init(120) #On initialise au début de la session.Tableau de réponse,etc
	y_cours=220
	arial=arial12b;RdispText(r'COURS:',0,y_cours,27,'red','blue')
	RdispText(Cours_Frac1_1,15,y_cours+15,29,'black','blue');arial=arial14b
	linehdle=can1.create_line(0,y_cours-15,WidthCan1,y_cours-15,width=4,fill='red')
	WSaveList.append(linehdle)
	#Création d'une permutation aléatoire
	X0text=10;Y0text=80
	#Création d'une permutation aléatoire pour dispatcher les réponses possibles sur la grille
	matPerm=GetmatPerm(4)
	a=Ralea2(10)
	b=Ralea2(10)
	c=Ralea2(6)
	d=Ralea2(4)
	str1='$\\frac{'+str(a)+'}{'+str(c)+'}'+'+\\frac{'+str(b)+'}{'+str(c*d)+'}$'
	Rprintf('Détermine combien fait '+str1,X0text,Y0text,'black','blue')

	NbreBonneReponse=matPerm[0] #Pour la vérification avec HandleGame	
	str2='$    \\frac{'+str(a*d+b)+'}{'+str(c*d)+'}$'
	PlaceTxt(MatDim,matPerm[0],str2,'red','black') #matPerm[0] est toujours la bonne réponse

	str2='$     \\frac{'+str(a*b)+'}{'+str(c+c*d)+'}$'
	PlaceTxt(MatDim,matPerm[1],str2,'red','black')

	str2='$    \\frac{'+str(a*b)+'}{'+str(c*d)+'}$'
	PlaceTxt(MatDim,matPerm[2],str2,'red','black')

	str2='$    \\frac{'+str(a+b)+'}{'+str(c+c*d)+'}$'
	PlaceTxt(MatDim,matPerm[3],str2,'red','black')



# --------------- FRACTIONS 1_2 -----------------

def JeuFraction1_2():
	global NbreBonneReponse,SessionInit,Method
	Method=1
	if SessionInit==1:
		Frac_Init(160) #On initialise au début de la session.
	X0text=30;Y0text=70
	#Création d'une permutation aléatoire pour dispatcher les réponses possibles sur la grille
	matPerm=GetmatPerm(4)
	a=Ralea2(10)
	b=Ralea2(10)
	c=Ralea2(5)
	d=Ralea2(5)

	str1='$\\frac{'+str(a)+'}{'+str(c)+'}'+'+\\frac{'+str(b)+'}{'+str(d)+'}$'
	Rprintf('Détermine combien fait '+str1,X0text,Y0text,'black','blue')

	NbreBonneReponse=matPerm[0] #Pour la vérification avec HandleGame	
	str2='$     \\frac{'+str(a*d+b*c)+'}{'+str(c*d)+'}$'
	PlaceTxt(MatDim,matPerm[0],str2,'red','black') #matPerm[0] est toujours la bonne réponse

	str2='$     \\frac{'+str(a+b)+'}{'+str(c*d)+'}$'
	PlaceTxt(MatDim,matPerm[1],str2,'red','black')

	str2='$    \\frac{'+str(a+b)+'}{'+str(c+d)+'}$'
	PlaceTxt(MatDim,matPerm[2],str2,'red','black')

	str2='$    \\frac{'+str(a*b)+'}{'+str(c*d)+'}$'
	PlaceTxt(MatDim,matPerm[3],str2,'red','black')

# --------------------------- JeuFraction2_0 -----------------------------
def JeuFraction2_0():
	global arial,NbreBonneReponse,SessionInit,Session,NbrClasse,Method
	Method=1
	Cours_Frac2_0="1. Compter les graduations qui forment une unité .\\n"\
		"2. Se repérer par rapport aux autres valeurs .\\n"\
		"3. Savoir transformer une valeur entière en fraction. $( 1 = \\frac{3}{3} )$ \\n"\
		"Exemple:"
	Cours_Frac2_0_b="Ici, deux façons possibles:\\nOn peut faire $1-\\frac{1}{3}=\\frac{3}{3}-\\frac{1}{3}=\\frac{2}{3}$\\n"\
					"ou bien simplement: $\\frac{1}{3} + \\frac{1}{3} = \\frac{2}{3}$"
	if SessionInit==1:
		Frac_Init(140) #On initialise au début de la session.Tableau de réponse,etc
	y_cours=240
	X0text=10;Y0text=45
	arial=arial12b
	RdispText(r'COURS:  Savoir lire une valeur sur un axe gradué',0,y_cours,27,'red','blue')
	RdispText(Cours_Frac2_0,10,y_cours+21,18,'black','blue')
	linehdle=can1.create_line(0,y_cours-15,WidthCan1,y_cours-15,width=4,fill='red')
	WSaveList.append(linehdle)
	#Trace the axis with special options (cf subroutine1_(2 or +).py):
	#DrawGradAxis(x0,y0,mode,Length,w,color,Lgrad,Master_Pos,Unit_grads,Master_Value,MaskList,AboveArrowTxt):
	disp=1;Rarc=2;Larc=4;Quid=8
	Mask=[1,disp,Larc+Quid,1,1,1,0,0,0,0,0,0,0,0]
	Text=['','','$-\\frac{1}{3}$','']
	DrawGradAxis(100,y_cours+5*25+2,10,300,2,'black',30,0,3,0,Mask,Text)
	RdispText(Cours_Frac2_0_b,10,y_cours+6*27+18,28,'black','blue')
	arial=arial14b


	#Création d'une permutation aléatoire pour dispatcher les réponses possibles sur la grille
	matPerm=GetmatPerm(4)

	c=Ralea2(6)
	d=Ralea2(4)
	str1="Quelle est la valeur indiquée par le point d'interrogation ?"
	Rprintf(str1,X0text,Y0text,'black','blue')

	if Session <=3:
		a=Ralea3(5)
		if Session==1: b=0
		else:
			if NbrClasse <=1: b=randrange(4) #If 6ème or 5ème
			else: b=-randrange(5) #If 4ème or 3ème
		#DrawGradAxis(x0,y0,mode,Length,w,color,Lgrad,Master_Pos,Unit_grads,Master_Value,MaskList,AboveArrowTxt):
		disp=1;Rarc=2;Larc=4;Quid=8
		if Session==3: Mask=[1,0,Quid,1,1,1,0,0,0,0,0,0,0,0]
		else: Mask=[1,1,Quid,1,1,1,0,0,0,0,0,0,0,0]
		Text=['','','','']
		arial=arial12b
		DrawGradAxis(50,Y0text+30,10,400,2,'black',40,0,a,b,Mask,Text)
		arial=arial14b
	
			
		NbreBonneReponse=matPerm[0] #Pour la vérification avec HandleGame	
		str2='    $\\frac{'+str(2+a*b)+'}{'+str(a)+'}$'
		PlaceTxt(MatDim,matPerm[0],str2,'red','black') #matPerm[0] est toujours la bonne réponse
	
		str2='    $'+str(a)+'$'
		PlaceTxt(MatDim,matPerm[1],str2,'red','black')

		str2='   $  \\frac{'+str(a)+'}{'+str(2+a*b)+'}$'
		PlaceTxt(MatDim,matPerm[2],str2,'red','black')

		str2='    $\\frac{'+str(2+a*b)+'}{'+str(a+1)+'}$'
		PlaceTxt(MatDim,matPerm[3],str2,'red','black')

	else:
		#DrawGradAxis(x0,y0,mode,Length,w,color,Lgrad,Master_Pos,Unit_grads,Master_Value,MaskList,AboveArrowTxt):
		#Display 10 graduations
		a=Ralea3(7) #Starting value at the first graduation
		b=Ralea3(5)
		disp=1;Rarc=2;Larc=4;Quid=8
		Mask=[];Text=[]
		for i in range(b):
			Mask.append(0)
			Text.append('')
		Mask[0]=disp #for first value to be 1
		Mask+=[disp+Rarc,Quid]
		Text.append('$+\\frac{1}{'+str(b)+'}$')
		print(Text)
		for i in range(10-(b+2)):
			Mask.append(0)
			Text.append('')
		#Mask=[0,0,0,0,disp+Rarc,Quid,0,0,0,0]
		#add 1/b
		#Text=['','','','','$\\frac{1}{'+str(b)+'}$','','','','','']
		arial=arial12b
		DrawGradAxis(100,Y0text+65,10,300,2,'black',30,0,b,a,Mask,Text)
		arial=arial14b

		NbreBonneReponse=matPerm[0] #Pour la vérification avec HandleGame	
		str2='    $\\frac{'+str((a+1)*b+1)+'}{'+str(b)+'}$'
		PlaceTxt(MatDim,matPerm[0],str2,'red','black') #matPerm[0] est toujours la bonne réponse
	
		str2='    $\\frac{'+str(2*(a+1)*b+1)+'}{'+str(b)+'}$'
		PlaceTxt(MatDim,matPerm[1],str2,'red','black')

		str2='   $  \\frac{'+str(a+2)+'}{'+str(b)+'}$'
		PlaceTxt(MatDim,matPerm[2],str2,'red','black')

		str2='    $'+str(a+2)+'$'
		PlaceTxt(MatDim,matPerm[3],str2,'red','black')


# --------------------------- JeuFraction2_1 -----------------------------
def JeuFraction2_1():
	global NbreBonneReponse,SessionInit,Method
	Method=1
	Cours_Frac2_0=r"Pour tout nombre a et b, avec b différent de 0,\n"\
		r"Une fraction $\frac{a}{b}$ est le nombre\n"\
		r"tel que multiplié par b donne a\n"\
		r"Cela signifie que $\frac{a}{b}\times b = a$." 
#arial=arial12b;RdispText(myBigtext,0,170,25,'red','blue');arial=arial14b
	if SessionInit==1:
		Frac_Init(180) #On initialise au début de la session.Tableau de réponse,etc
	y_cours=300
	arial=arial12b
	RdispText(r'COURS:',0,y_cours,27,'red','blue')
	RdispText(Cours_Frac2_0,100,y_cours,27,'black','blue')
	arial=arial14b
	linehdle=can1.create_line(0,y_cours-15,WidthCan1,y_cours-15,width=4,fill='red')
	WSaveList.append(linehdle)
	

	X0text=160;Y0text=100

	#Création d'une permutation aléatoire pour dispatcher les réponses possibles sur la grille
	matPerm=GetmatPerm(4)
	a=Ralea2(10)
	b=Ralea2(10)
	while a==b: b=Ralea2(10)
	c=Ralea2(6)
	d=Ralea2(4)
	if Session<=2:
		str1=r"$\\frac{"+str(a)+"}{"+str(b)+r"}\times  "+str(b)+ "$  est égal à :"
		Rprintf(str1,X0text,Y0text,'black','blue')
	
		NbreBonneReponse=matPerm[0] #Pour la vérification avec HandleGame	
		str2='    $'+str(a)+'$'
		PlaceTxt(MatDim,matPerm[0],str2,'red','black') #matPerm[0] est toujours la bonne réponse
	
		str2='    $'+str(b)+'$'
		PlaceTxt(MatDim,matPerm[1],str2,'red','black')
	
		str2='   $  \\frac{'+str(a)+'}{'+str(b)+'}$'
		PlaceTxt(MatDim,matPerm[2],str2,'red','black')
	
		str2='    $'+str(a*b)+'$'
		PlaceTxt(MatDim,matPerm[3],str2,'red','black')
	elif Session==3:
		str1=r"$"+str(a)+r" \times  \obj_rect{20,30,1,1,8,6,0} ="+str(b)+r"$.\n"\
			r"Quel est le nombre manquant?"
		RdispText(str1,X0text-60,Y0text,28,'black','blue')

		NbreBonneReponse=matPerm[0] #Pour la vérification avec HandleGame	
		str2='   $  \\frac{'+str(b)+'}{'+str(a)+'}$'
		PlaceTxt(MatDim,matPerm[0],str2,'red','black') #matPerm[0] est toujours la bonne réponse
	
		str2='    $'+str(b)+'$'
		PlaceTxt(MatDim,matPerm[1],str2,'red','black')
	
		str2='   $  \\frac{'+str(a)+'}{'+str(b)+'}$'
		PlaceTxt(MatDim,matPerm[2],str2,'red','black')
	
		str2='    $'+str(a)+'$'
		PlaceTxt(MatDim,matPerm[3],str2,'red','black')
	else:
		str1="On considère le tableau de proportionnalité ci-dessous:\\n \\n"\
			" $\obj_tab{1,8,0, Nombre de barquettes &"+str(a)+"&"+str(2*a)+";"\
			" Prix en Euros &  "+str(b)+"  &  "+str(2*b)+"  }  \\times  ... $ \\n"\
			" \\nQuel est le coefficient de proportionnalité ?"

		RdispText(str1,10,30,28,'black','blue')

		NbreBonneReponse=matPerm[0] #Pour la vérification avec HandleGame	
		str2='   $  \\frac{'+str(b)+'}{'+str(a)+'}$'
		PlaceTxt(MatDim,matPerm[0],str2,'red','black') #matPerm[0] est toujours la bonne réponse
	
		str2='   $  \\frac{'+str(2*a)+'}{'+str(2*b)+'}$'
		PlaceTxt(MatDim,matPerm[1],str2,'red','black')
	
		str2='   $  \\frac{'+str(a)+'}{'+str(b)+'}$'
		PlaceTxt(MatDim,matPerm[2],str2,'red','black')
	
		str2='    $'+str(a)+'$'
		PlaceTxt(MatDim,matPerm[3],str2,'red','black')

# --------------------------- JeuFraction2_2 -----------------------------
def JeuFraction2_2():
	global arial,NbreBonneReponse,SessionInit,Session,carreau,Method
	Method=2 #for separate rectangles to click in as giving an answer

	#if SessionInit==1:
	#	Frac_Init(160) #On initialise au début de la session.Tableau de réponse,etc
	#Force deletion of the answering grid.
	#remark: the old one is deleted in quadrillage at creation of a new one
	DeleteQuadrillage(carreau)

	X0text=10;Y0text=45

	a=Ralea1(10)
	b=Ralea2(4)
	c=Ralea1(10)
	#Trace the axis with special options (cf subroutine1_(2 or +).py):
	#DrawGradAxis(x0,y0,mode,Length,w,color,Lgrad,Master_Pos,Unit_grads,Master_Value,MaskList,AboveArrowTxt):
	disp=1;Rarc=2;Larc=4;Quid=8
	Mask=[1,1,0,1,1,1,0,0,0,0,0,0,0,0]
	Text=['','','','']
	Ngrad=10; Laxis=400
	#Following axis values depend on b and c determined randomly above
	DrawGradAxis(80,Y0text+50,10+16,Laxis,2,'black',Laxis/Ngrad,0,b,c,Mask,Text)
	arial=arial14b


	str1="Click l'emplacement sur l'axe où se trouve le nombre $\\frac{"+str(a+c*b)+"}{"+str(b)+"}$."
	Rprintf(str1,X0text,Y0text,'black','red')
	#The right anwser is the a-th one
	NbreBonneReponse=a
	#print('Place to click is graduation number:',a)

# --------------- Problèmes ----------------
	
def JeuFraction3_0():
	#CallbackAnswer is used as a jump program when a click in ZoneCL is done
	#The use of CallbackAnswer is in Method=3
	global arial,CallbackAnswer,AnswerSumStr,AnswerSum,Method,ZoneCL
	
	DeleteQuadrillage(carreau)

	x_brot=305; y_brot=30;GFactor=2;xgrads=13;x2grads=73;dxg=5
#	x_brot=0; y_brot=0
	DataBrot=[(0,2),(73,2),(73,2),(73,80),(73,80),(68,85),(68,85),(17,85),(17,85),(13,78),(13,78),(13,10),(13,10),(6,6),(6,6),(0,2)]
	AnseBrot=[(73,24),(86,16),(86,16),(95,20),(95,20),(96,27),(96,27),(96,49),(96,49),(85,61),(85,61),(73,67)]
	demi=14;niv0=85;quart=int((demi+niv0)/2);huitieme=int((quart+niv0)/2)
	douzieme=int(niv0-(niv0-demi)/6);cinquieme=int(niv0-2*(niv0-demi)/5); dixieme=int(niv0-(niv0-demi)/5)
	#Grads=[(xgrads,demi),(xgrads+dxg,demi),(xgrads,quart),(xgrads+dxg,quart),(xgrads,huitieme),(xgrads+dxg,huitieme),(xgrads,douzieme),(xgrads+dxg,douzieme),(x2grads,dixieme),(x2grads-dxg,dixieme),(x2grads,cinquieme),(x2grads-dxg,cinquieme)]
	Grads=[(xgrads,demi),(xgrads+dxg,demi),(xgrads,quart),(xgrads+dxg,quart),(xgrads,huitieme),(xgrads+dxg,huitieme),(x2grads,dixieme),(x2grads-dxg,dixieme),(x2grads,cinquieme),(x2grads-dxg,cinquieme)]
	def Homothetie(Data,xv,yv,lamda):
		for i in range(int(len(Data)/2)):
			x0=xv+lamda*Data[2*i][0]
			y0=yv+lamda*Data[2*i][1]
			x1=xv+lamda*Data[2*i+1][0]
			y1=yv+lamda*Data[2*i+1][1]
			WSaveList.append(can1.create_line(x0,y0,x1,y1,width=3,fill='black'))
	Homothetie(DataBrot,x_brot,y_brot,GFactor)
	Homothetie(AnseBrot,x_brot,y_brot,GFactor)
	Homothetie(Grads,x_brot,y_brot,GFactor)
	#Homothetie(DataBrot,0,0,1)
	#Homothetie(AnseBrot,0,0,1)
	#Homothetie(Grads,0,0,1)
	
	#Préparation des rectangles de saisi en dessous des fractions.
	ZoneCL=[]
	for val in [demi, quart, huitieme]:
		x0=x_brot+GFactor*xgrads+10; y0=y_brot+GFactor*val
		dlx=22;dly=15
		rect=can1.create_rectangle(x0,y0-dly,x0+dlx,y0+dly,activefill='grey',outline='white',fill='white')
		WSaveList.append(rect)
		ZoneCL.append((x0,y0-dly,x0+dlx,y0+dly,rect))
	for val in [cinquieme,dixieme]:
		x0=x_brot+GFactor*x2grads-dxg-32; y0=y_brot+GFactor*val
		dlx=22;dly=15
		rect=can1.create_rectangle(x0,y0-dly,x0+dlx,y0+dly,activefill='grey',outline='white',fill='white')
		WSaveList.append(rect)
		ZoneCL.append((x0,y0-dly,x0+dlx,y0+dly,rect))

	# ----------------- Affichage des fractions ----------------
	arial=arial10b
	Rprintf('$\\frac{1}{2}$',x_brot+GFactor*xgrads+10,y_brot+GFactor*demi,'red','blue')
	Rprintf('$\\frac{1}{4}$',x_brot+GFactor*xgrads+10,y_brot+GFactor*quart,'red','blue')
	Rprintf('$\\frac{1}{8}$',x_brot+GFactor*xgrads+10,y_brot+GFactor*huitieme,'red','blue')
	#Rprintf('$\\frac{1}{12}$',x_brot+GFactor*xgrads+14,y_brot+GFactor*douzieme,'red','blue')
	Rprintf('$\\frac{1}{5}$',x_brot+GFactor*x2grads-dxg-32,y_brot+GFactor*cinquieme,'red','blue')
	Rprintf('$\\frac{1}{10}$',x_brot+GFactor*x2grads-dxg-35,y_brot+GFactor*dixieme,'red','blue')
	arial=arial14b
	# ------------------ Fin du dessin du pichet d'eau -------------
	n=2
	a=randrange(2) #fourni un nombre entier entre 0 et n-1
	b=randrange(2);c=randrange(2);d=randrange(2);e=randrange(2)
	while a+b+c <=1: a=randrange(2); b=randrange(2);c=randrange(2)

	if NbrClasse<=1: quantity=a*0.5+b*0.25+c*0.125 #Pour les 6ème ou 5èmes
	else:  quantity=a*0.5+b*0.25+c*0.125+d*0.1+e*0.2 #Pour les 4ème ou 3èmes
	quantity=1000*quantity
	Enonce_Frac3_0=r"Peter souhaite faire un gâteau. Il a suivi les \n"\
		r"cours de mathématique avec beaucoup\nd'attention. Pourtant il "\
		r"n'est plus très sûr de\nsavoir comment additionner les quantités.\n"\
		r" \n \nLa recette lui demande de prendre précisément "+str(int(quantity))+r" ml d'eau.\n" \
		r"Il dispose pour cela d'un verre doseur gradué de fractions de 1L: \n"\
		r"$\\frac{1}{2}L ,\\frac{1}{4}L, \\frac{1}{8}L$, etc...\n"\
		r"Aide-le à constituer ce volume en ajoutant les quantités proposées.\n"\
		r"Pour cela, tu cliqueras sur les fractions du verre doseur.\n"\
		r"(On rappelle que: 1000mL=1L)."
#arial=arial12b;RdispText(myBigtext,0,170,25,'red','blue');arial=arial14b

	x_enonce=5; y_enonce=60
	arial=arial14b; RdispText(r'EXERCICE:',x_enonce,y_enonce,27,'red','blue')
	arial=arial12b; RdispText(Enonce_Frac3_0,x_enonce,y_enonce+27,22,'black','blue')
	arial=arial14b
	
	#ZoneCL contient 2 coins opposés d'un rectangle ainsi que le handler utile pour
	#modifier la couleur si besoin
	#Here it is not a question of good answer: NbreBonneReponse
	#We have to define a new method : Method=3
	Method=3 #This is answering mode: addition
	AnswerSumStr='' #initialize the text of answer
	AnswerSum=0
	CallbackAnswer=JeuFrac3_0_Handling
	
def JeuFrac3_0_Handling(Nbre):
	#In ZoneCL demi,quart, huitieme, cinquieme, dixieme
	global AnswerSumStr,AnswerSum,arial
	#print('Nbre=',Nbre)
	if Nbre==-1: return
	Values=[0.5,0.25,0.125,0.2,0.1]
	AnswerSum+=Values[Nbre]
	PossibleValues=['\\frac{1}{2}','\\frac{1}{4}','\\frac{1}{8}','\\frac{1}{5}','\\frac{1}{10}']
	if AnswerSumStr=='': AnswerSumStr+=PossibleValues[Nbre]
	else: AnswerSumStr+= '+' + PossibleValues[Nbre]

	str='Ta Réponse: $'+AnswerSumStr+'$'
	arial=arial12b; Rprintf(str,10,390,'red','blue'); arial=arial14b
	#Reste à interpréter la somme, ayant sauvegardé les valeurs numériques
	#print('AnswerSum=',AnswerSum)
	
	