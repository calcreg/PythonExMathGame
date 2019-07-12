

def Frac_Init():
	global MatDim,Session,SessionInit
	# DIM=[x,y,Nx]
	#     [X,Y,Ny]   Remarque: Nx est le nombre de carreaux sur une ligne
	MatDim=np.array([[60,100,4],[340,150,1]])
	Quadrillage(MatDim) #Construction visuelle de la grille ou tableau à cliquer
	#for Session in range(1,6): #Concrètement de 1 à 5
	Session=1 #Initialisation de la session de 5 questions sur le thème ci-dessous
	DispSession(Session) #Affichage texte
	SessionInit=0 # On le fait passer à 0 puisque l'initialisation a été effectuée

def Ralea(n):# => génère un nombre aléatoire de 2 à n-1
	a = randrange(n)             
	while a==0 or a==1: 
		a = randrange(n)             # => génère un nombre aléatoire de 0 à n-1
	return a

# --------------- FRACTIONS 1_1 -----------------

def JeuFraction1_1():
	global NbreBonneReponse,SessionInit
	if SessionInit==1:	Frac_Init() #On initialise au début de la session.
	#Création d'une permutation aléatoire
	X0text=30;Y0text=70
	matPerm=np.array([0,1,2,3])
	for i in range(0,4):
		p=randrange(4)
		p1=matPerm[p]
		p0=matPerm[0]
		matPerm[0]=p1
		matPerm[p]=p0
	a=Ralea(10)
	b=Ralea(10)
	c=Ralea(10)

	str1='$\\frac{'+str(a)+'}{'+str(c)+'}'+'+\\frac{'+str(b)+'}{'+str(c)+'}$'
	Rprintf('Détermine combien fait '+str1,X0text,Y0text,'black','blue')

	#print(matPerm)
	NbreBonneReponse=matPerm[0] #Pour la vérification avec HandleGame	
	#print('bonne réponse=',matPerm[0])
	str2='$   \\frac{'+str(a+b)+'}{'+str(c)+'}$'
	PlaceTxt(MatDim,matPerm[0],str2,'red','black') #matPerm[0] est toujours la bonne réponse

	str2='$    \\frac{'+str(int(np.abs(a+b)/2))+'}{'+str(c)+'}$'
	PlaceTxt(MatDim,matPerm[1],str2,'red','black')

	str2='$   \\frac{'+str(np.abs(a+b))+'}{'+str(c+c)+'}$'
	PlaceTxt(MatDim,matPerm[2],str2,'red','black')

	str2='$   \\frac{'+str(np.abs(a-b))+'}{'+str(c+c)+'}$'
	PlaceTxt(MatDim,matPerm[3],str2,'red','black')

# --------------- FRACTIONS 1_2 -----------------

def JeuFraction1_2():
	#On ajoute des fractions, le dénominateur de l'une est le double ou triple de l'autre
	global NbreBonneReponse,SessionInit
	if SessionInit==1:	Frac_Init() #On initialise au début de la session.
	X0text=30;Y0text=70
	#Création d'une permutation aléatoire pour dispatcher les réponses possibles sur la grille
	matPerm=np.array([0,1,2,3])
	for i in range(0,4):
		p=randrange(4)
		p1=matPerm[p]
		p0=matPerm[0]
		matPerm[0]=p1
		matPerm[p]=p0
	a=Ralea(10)
	b=Ralea(10)
	c=Ralea(6)
	d=Ralea(4)
	str1='$\\frac{'+str(a)+'}{'+str(c)+'}'+'+\\frac{'+str(b)+'}{'+str(c*d)+'}$'
	Rprintf('Détermine combien fait '+str1,X0text,Y0text,'black','blue')

	NbreBonneReponse=matPerm[0] #Pour la vérification avec HandleGame	
	str2='$   \\frac{'+str(a*d+b)+'}{'+str(c*d)+'}$'
	PlaceTxt(MatDim,matPerm[0],str2,'red','black') #matPerm[0] est toujours la bonne réponse

	str2='$    \\frac{'+str(a*b)+'}{'+str(c+c*d)+'}$'
	PlaceTxt(MatDim,matPerm[1],str2,'red','black')

	str2='$   \\frac{'+str(a*b)+'}{'+str(c*d)+'}$'
	PlaceTxt(MatDim,matPerm[2],str2,'red','black')

	str2='$   \\frac{'+str(a+b)+'}{'+str(c+c*d)+'}$'
	PlaceTxt(MatDim,matPerm[3],str2,'red','black')



# --------------- FRACTIONS 3_2 -----------------

def JeuFraction3_2():
	global NbreBonneReponse,SessionInit
	if SessionInit==1:	Frac_Init() #On initialise au début de la session.
	X0text=30;Y0text=70
	#Création d'une permutation aléatoire pour dispatcher les réponses possibles sur la grille
	matPerm=np.array([0,1,2,3])
	for i in range(0,4):
		p=randrange(4)
		p1=matPerm[p]
		p0=matPerm[0]
		matPerm[0]=p1
		matPerm[p]=p0
	a=Ralea(10)
	b=Ralea(10)
	c=Ralea(5)
	d=Ralea(5)

	str1='$\\frac{'+str(a)+'}{'+str(c)+'}'+'+\\frac{'+str(b)+'}{'+str(d)+'}$'
	Rprintf('Détermine combien fait '+str1,X0text,Y0text,'black','blue')

	NbreBonneReponse=matPerm[0] #Pour la vérification avec HandleGame	
	str2='$   \\frac{'+str(a*d+b*c)+'}{'+str(c*d)+'}$'
	PlaceTxt(MatDim,matPerm[0],str2,'red','black') #matPerm[0] est toujours la bonne réponse

	str2='$    \\frac{'+str(a+b)+'}{'+str(c*d)+'}$'
	PlaceTxt(MatDim,matPerm[1],str2,'red','black')

	str2='$   \\frac{'+str(a+b)+'}{'+str(c+d)+'}$'
	PlaceTxt(MatDim,matPerm[2],str2,'red','black')

	str2='$   \\frac{'+str(a*b)+'}{'+str(c*d)+'}$'
	PlaceTxt(MatDim,matPerm[3],str2,'red','black')


