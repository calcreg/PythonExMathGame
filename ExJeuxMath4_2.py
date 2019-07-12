#
# -----------------------USAGE LICENSE and AUTHOR ---------------------------------------------#
# Licence GNU GPL. 
# This is a freeware, forbidden to be sold full or being part of a prgram to be sold.
# Author: Bussy-Socrate Regan.
# This program is aimed at math teachers for their students to improve their knowledge through exercising and guidance.
# It is to be used as a basis for building a suite of exercise of gradual difficulties.
# Subroutine Rprintf is able to display latex (\sqrt{}, \frac{}{} and x^{y}, +, -) without the heavy ans slow latex package under python.
# It can easily be implemented for one who can program in python.
# This program is under GNU GPL License. The author permits the use of this program freely, its sharing, 
# but this header comments containing the license and the author should be kept inside the program.
# Developpers: Contact the author for significant contributions through pull requests. Respect the architecture ..._inc.py includes files.
# Developpers should think in a pedagogical way. Gradual exercises and comments available by click to help kids to fix knowledge.
# Please read the README.md to launch the program.

import tkinter as tk
from tkinter import font as tkFont
import numpy as np
from random import randrange
import time


Score=0;xScore=310;yScore=10;ScoreTxt=0
Session=0;xSession=10;ySession=10;SessionTxt=0;ChgtSession=0
carreau=0
damier=0
xcol=-1;ycol=-1
MatDim=0

fen1=tk.Tk()
fen1.title('JEUX DE MATHEMATIQUES                      ')
fen1.geometry('1020x340+50+100')

arial14b = tkFont.Font(family='Arial', size=14, weight='bold')
arial12b = tkFont.Font(family='Arial', size=12, weight='bold')
arial10n = tkFont.Font(family='Arial', size=10, weight='normal')
arialm = tkFont.Font(family='Arial', size=8, weight='bold')
arialLargeb = tkFont.Font(family='Arial', size=16, weight='bold')
arialHUGEb = tkFont.Font(family='Arial', size=50, weight='bold')
arial=arial14b #Initialisation de la font pour Rprintf

can1 = tk.Canvas(fen1, width =400, height =320,bg='white')
can2 = tk.Canvas(fen1, width =400, height =60,bg='white')
can4 = tk.Canvas(fen1, width =180, height =320,bg='white')

can1.grid(row=0,column=0,rowspan=2,padx=5,pady=2)
can2.grid(row=0,column=1,padx=5,pady=2)
#can3.grid(row=1,column=0,padx=5,pady=2)
can4.grid(row=0,column=2,rowspan=2,padx=5,pady=2)

#Image = tk.PhotoImage(file ='~/Bureau/ExJeuxPyMath/images/mandelbrot_bleached.png')
#item = can2.create_image(0, 0, image = Image,anchor='nw')

a=0
b=30
can2.create_text(a+2,b,anchor='w',text='FRACTIONS',font=arialHUGEb,fill='black')
can2.create_text(a,b+2,anchor='w',text='FRACTIONS',font=arialHUGEb,fill='red')

TextWidth=40 #Largeur de la fenetre en nombre de caracteres
txt = tk.Text(fen1,width=TextWidth, height=11,font=arial14b, wrap='word')
#for l in range(10): txt.insert(tk.END, 'Ceci est du texte. 123456789 123456789 123456789\n')
Letxt='Le jeux ci-contre est un jeu de maîtrise des fractions.\nLis les consignes et réponds en cliquant les réponses aux questions.'
txt.insert(tk.END,Letxt)
txt.grid(row=1,column=1,padx=5,pady=2)

ScoreTxt=can1.create_text(xScore,yScore,anchor='w',text='Score = '+str(Score),font=arial14b,fill='red')
can1.create_line(0,yScore+10,400,yScore+10,width=2,fill='blue')
SessionTxt=can1.create_text(xSession,ySession,anchor='w',text='Session = '+str(Session)+' / 5',font=arial14b,fill='red')

mytext=r'On a : $1-\frac{265}{45}+2a=3+2=a+\frac{1}{2}+\sqrt{25}$.'

def Rprintf(text,tx,ty,col1,col2):
	global WSaveList #List contenant tous les handle d'affichage de bouts de textes et de lignes
	if text.count('$')==2:
		#print('pass1')
		#il y a une chaine entre $ $
		a1=text.find('$')
		a2=text.rfind('$') #reverse find où est le dernier $
		#print('a1,a2=',a1,a2)
		str2=""
		for i in range(0,a1):
			str2+=text[i]
		txthandle=can1.create_text(tx,ty,anchor='w',text=str2,font=arial,fill=col1)
		WSaveList.append(txthandle)
		L=arial.measure(str2) #On mesure la longueur du texte ecris jusque le $ (exclus)
		j=a1+1
		while j < a2: #Entre les deux seuls $
			if text[j]==r'+':
				drawPlus(tx+L+4,ty,10,col2)
				L=L+18		
				j+=1
				#print('+')
			elif text[j]==r'-':
				drawMoins(tx+L+4,ty,10,col2)
				L=L+16
				j+=1
			elif text[j]==r'=':
				if (ord(text[j-1]) in range(97,123)): L=L+2
				else: L=L+2*arial.measure(' ')
				drawEgal(tx+L,ty,12,col2)
				L=L+18
				j+=1
			elif ord(text[j]) in range(97,123):
				Rstr=text[j]
				txthandle=can1.create_text(tx+L,ty-2,anchor='w',text=Rstr,font="{LM Roman 8} 14 bold italic",fill=col2)
				WSaveList.append(txthandle)
				if ord(text[j+1]) in range(97,123): L=L+10
				else: L=L+16
				j+=1
			elif text[j]==')' and text[j+1]==r'^':
				Rstr=text[j]
				txthandle=can1.create_text(tx+L-4,ty,anchor='w',text=Rstr,font=arial,fill=col2)
				WSaveList.append(txthandle)
				L=L+arial.measure(r')')-5
				j+=1
			elif text[j]=='\\': 
				SpStr=""
				SpStr += text[j]
				j+=1
				while text[j]!='\\' and text[j]!=r'-'and text[j]!=r'+'and text[j]!=r' ' and text[j]!=r'$': #Une seule operation a la fois
					SpStr += text[j]
					j+=1
				SpStr+=r'$' #On place un $ pour que SpecPrintf fonctionne correctement
				#print('SpStr='+SpStr)
				L=SpecPrintf(SpStr,tx,ty,L,col2)
			elif text[j]=='^': 
				if (ord(text[j-1]) in range(48,58)): L=L+arial.measure(' ') # apres un chiffre
				if text[j-1]==')': L=L+4*arial.measure(' ')/3 # apres une parenthese
				SpStr=""
				SpStr += text[j]
				j+=1
				while text[j]!=r'}' and text[j]!=r'$': #Une seule operation a la fois
					SpStr += text[j]
					j+=1
				SpStr+=r'}$' #On place un $ pour que SpecPrintf fonctionne correctement
				j+=1
				#print('SpStr='+SpStr)
				L=SpecPrintf(SpStr,tx,ty,L,col2)
			else:
				#Aucun caractère special donc:
				Rstr=""
				Rstr+=text[j]
				j+=1
				txthandle=can1.create_text(tx+L,ty,anchor='w',text=Rstr,font=arial,fill=col2)
				WSaveList.append(txthandle)
				L=L+arial.measure(Rstr) #On ecarte bien les nombres des signes
	
		#Il faut ensuite terminer l'ecriture du texte qui suit
		str4=""
		for i in range(a2+1,len(text)): #a2+1 car on ne veut pas prendre le dernier $
			str4+=text[i]

		txthandle=can1.create_text(tx+L+int(arial.measure(' ')/3),ty,anchor='w',text=str4,font=arial,fill=col1)
		WSaveList.append(txthandle)
		can1.grid() #on met à jour l'affichage du text s'il y a eu lieu
		return L+int(arial.measure(' ')/3) #Retourne la taille occupée par la chaine de caractère
	else:
		#print('else pass3')
		txthandle=can1.create_text(tx,ty,anchor='w',text=text,font=arial,fill=col1)
		WSaveList.append(txthandle)
		can1.grid()
		return arial.measure(text)

def SpecPrintf(text,tx,ty,L1,color2): #Trace les fonctions spéciales
	global WSaveList
	#color1 est la couleur du text 
	#color2 est la couleur de l'expression entre $ $
	#mytext.count('$') #Compte le nombre de fois qu'apparait le motif $ dans mytext
	str1="" #Attention on ne peut pas traiter une chaine avec str=[]
	# De même, on ne peut pas faire str[0]=text[1] C'est l'action de gauche qui pose problème
	i=0
	while text[i]!='$':
		str1+=text[i] #On ajoute un caractère
		i+=1
		ilength1=i+2 # on sauvegarde la longueur de caractères entre les $ $
	str1+=text[i] #On récupère le $
	#test du text entre $...$
	#print('pass1, str1 ='+ str1)
	if str1.count(r'\sqrt{')!= 0:
		i=6
		str3=""
		#print('pass2, str1 ='+ str1,'; on a ilength1=',ilength1)
		while str1[i]!='}' and str1[i]!='$':
			str3+=str1[i]
			#print('pass2bis, str3='+str3)
			i+=1
		deltaL=int(5*arial.measure(' ')/2) #la place qu'occupe la racine carree
		txthandle=can1.create_text(tx+L1+deltaL,ty,anchor='w',text=str3,font=arial,fill=color2)
		WSaveList.append(txthandle)
		wstr3=arial.measure(str3) #largeur en pixels du text sous la racine
		#print('largeur wstr3=',wstr3)
		drawsqrt(tx+L1,ty,wstr3,color2) #Tracer le trait suffisamment long (selon wstr3)
		L1=wstr3+L1+deltaL #Ensuite on ajoute les longueurs en pixels du texte
	if str1.count(r'^{')!= 0: #On n'accepte que la forme  ^{nbr} et pas ^nbr
		i=2
		str3=""
		#print('pass2, str1 ='+ str1,'; on a ilength1=',ilength1)
		while str1[i]!='}' and str1[i]!='$':
			str3+=str1[i]
			#print('pass2bis, str3='+str3)
			i+=1
		wstr3=arialm.measure(str3) #largeur en pixels du text sous la racine
		ws=arialm.measure(' ')
		txthandle=can1.create_text(tx+L1-3*ws/2,ty,anchor='sw',text=str3,font=arialm,fill=color2)
		WSaveList.append(txthandle)
		L1=5*wstr3/7+L1 #Ensuite on ajoute les longueurs en pixels du texte
	if str1.count(r'\times')!= 0:
		#print(r'\times')
		i=6
		wstr3=arial.measure('   ') #largeur en pixels du text sous la racine
		drawCroix(tx+L1+2,ty,wstr3,color2) #Tracer le trait suffisamment long (selon wstr3)
		L1=wstr3+L1 #Ensuite on ajoute les longueurs en pixels du texte
	if str1.count(r'\frac{')!= 0:
		i=6
		str3=""
		#print('pass2, str1 ='+ str1,'; on a ilength1=',ilength1)
		while str1[i]!='}' and str1[i]!='$':
			str3+=str1[i]
			#print('pass2bis, str3='+str3)
			i+=1
		deltaL=int(4*arial.measure(' ')/2) #la place qu'occupe la racine carree
		wstr3=arial.measure(str3) #largeur en pixels du text sous la racine
		str3_s=str3 #sauvegarde
		i+=1
		if str1[i]!='{': print('error missing "{".')
		str3=""
		i+=1
		while str1[i]!='}' and str1[i]!='$':
			str3+=str1[i]
			#print('pass2bis, str3='+str3)
			i+=1
		if wstr3<arial.measure(str3):
			txthandle=can1.create_text(tx+L1+deltaL+(arial.measure(str3)-wstr3)/2,ty,anchor='sw',text=str3_s,font=arial,fill=color2)
			WSaveList.append(txthandle)
			txthandle=can1.create_text(tx+L1+deltaL,ty,anchor='nw',text=str3,font=arial,fill=color2)
			WSaveList.append(txthandle)
			wstr3=arial.measure(str3)
		else:
			txthandle=can1.create_text(tx+L1+deltaL,ty,anchor='sw',text=str3_s,font=arial,fill=color2)
			WSaveList.append(txthandle)
			txthandle=can1.create_text(tx+L1+deltaL+(wstr3-arial.measure(str3))/2,ty,anchor='nw',text=str3,font=arial,fill=color2)
			WSaveList.append(txthandle)
		drawfrac(tx+L1+deltaL/2,ty,wstr3+deltaL,color2)
		L1=wstr3+L1+2*deltaL #Ensuite on ajoute les longueurs en pixels du texte
	return L1

def drawsqrt(x,y,largeur,coul):
	#largeur est la largeur en pixel du trait supérieur de la racine
	w=2 #epaisseur du trait de la racine
	X=np.array([[x,x+3,x+7,x+10,x+13+largeur,x+14+largeur],[y,y-5,y+7,y-8,y-8,y-7]])
	for i in range (0,5):
		linehandle=can1.create_line(X[0,i],X[1,i],X[0,i+1],X[1,i+1],width=w,fill=coul)
		WSaveList.append(linehandle)
def drawfrac(x,y,largeur,coul):
	#largeur est la largeur en pixel du trait supérieur de la racine
	w=2 #epaisseur du trait de la racine
	linehandle=can1.create_line(x,y,x+largeur,y,width=w,fill=coul)
	WSaveList.append(linehandle)
def drawPlus(x,y,largeur,coul):
	w=2
	linehandle=can1.create_line(x,y,x+largeur,y,width=w,fill=coul)
	WSaveList.append(linehandle)
	linehandle=can1.create_line(x+5,y-5,x+5,y+5,width=w,fill=coul)
	WSaveList.append(linehandle)
def drawMoins(x,y,largeur, coul):
	w=2
	linehandle=can1.create_line(x,y,x+largeur,y,width=w,fill=coul)
	WSaveList.append(linehandle)
def drawEgal(x,y,largeur, coul):
	w=2
	linehandle=can1.create_line(x,y-2,x+largeur,y-2,width=w,fill=coul)
	WSaveList.append(linehandle)
	linehandle=can1.create_line(x,y+2,x+largeur,y+2,width=w,fill=coul)
	WSaveList.append(linehandle)
def drawCroix(x,y,largeur, coul):
	w=2
	linehandle=can1.create_line(x,y-5,x+largeur,y+5,width=w,fill=coul)
	WSaveList.append(linehandle)
	linehandle=can1.create_line(x,y+5,x+largeur,y-5,width=w,fill=coul)
	WSaveList.append(linehandle)

def DeletePreviousRText():
	global WSaveList
	for handle in WSaveList:
		can1.delete(handle)
	WSaveList=[] #Réinitialisation après effacement total des bouts de texte et de lignes

#--------------- FIN DES SOUS-ROUTINES DE TRACER FORMULES MATHS -------------------


# ----------------------------------------------------------------
#			SOUS-ROUTINES CREATION D'UNE GRILLE POUR CLIQUER
# ----------------------------------------------------------------
def clic(event):
	#global MatDim
	i=event.x
	j=event.y
	#print('click:Nx,Ny=',MatDim[0,2],MatDim[1,2])
	Nbre=GetNbre(MatDim,i,j)
	#print('Nbre=',Nbre)
	if Nbre >=0 : Coord['text']='Le rectangle cliqué est ('+str(Nbre)+'), coordonnées pointeur ('+str(i)+','+str(j)+')'
	else: Coord['text']='Hors quadrillage ('+str(Nbre)+'), coordonnées pointeur ('+str(i)+','+str(j)+')'
	HandleGame(Nbre)

def Quadrillage(DIM): #coin haut gauche et coin droit bas. Remarque: X>x et Y>y
# DIM=[x,y,Nx]
#     [X,Y,Ny]   Remarque: Nx est le nombre de carreaux sur une ligne
	global carreau
	Nx=DIM[0,2]
	Ny=DIM[1,2]
	wx=np.abs(DIM[0,0]-DIM[1,0])/Nx
	wy=np.abs(DIM[0,1]-DIM[1,1])/Ny
	x=DIM[0,0]
	y=DIM[0,1]
#voir http://tkinter.fdex.eu/doc/caw.html?highlight=rectangle#Canvas.create_rectangle
	if carreau!=0: can1.delete(carreau)
	carreau=[[can1.create_rectangle(x+i*wx,y+j*wy,x+(i+1)*wx,y+(j+1)*wy,fill="#dddddd") 
								for i in range(Nx)] for j in range(Ny)]


def GetNbre(DIM,x,y):
	#DIM est une matrice 2,3 contenant les dimensions du tableau
	#x et y contiennent les coordonnées du point cliqué
	global carreau,xcol,ycol
	dX=(DIM[1,0]-DIM[0,0])
	dY=(DIM[1,1]-DIM[0,1])
	Nx=DIM[0,2]
	Ny=DIM[1,2]
	x0=DIM[0,0]
	y0=DIM[0,1]
	a=(x-x0)//(dX/Nx) # a = colonne
	b=(y-y0)//(dY/Ny) # b = ligne
	#print('x0,y0=',x0,y0)
	#print ('x,y=',x,y)
	#print('x-x0,y-y0',x-x0,y-y0)
	#print ('dX,dY=',dX,dY)
	#print ('Nx,Ny=',Nx,Ny)
	if a<0 or b<0 or a+1>Nx or b+1>Ny :
		xcol=-1; ycol=-1
		return -1
	xcol=a;ycol=b
	return a+b*Nx

def PlaceTxt(DIM,Numero,txt,col1,col2):
	#Sert à placer dans le tableau directement le text numérique ou mathématique
	dX=(DIM[1,0]-DIM[0,0]) #Largeur totale du tableau
	dY=(DIM[1,1]-DIM[0,1]) #Hauteur totale du tableau
	Nx=DIM[0,2]
	Ny=DIM[1,2]
	x0=DIM[0,0]
	y0=DIM[0,1]
	x=x0+(Numero%Nx)*dX/Nx
	y=y0+(Numero//Nx+0.5)*dY/Ny
	#print(r'Numero%Nx=',Numero%Nx)
	#print('emplacement x,y =',x,y)
	Rprintf(txt,x,y,col1,col2)

def DispScore(score):
	global ScoreTxt,xScore,yScore
	if ScoreTxt!=0: can1.delete(ScoreTxt)
	ScoreTxt=can1.create_text(xScore-arialLargeb.measure(str(score)),yScore,anchor='w',text='Score = '+str(score),font=arialLargeb,fill='red')

def DispSession(session):
	global SessionTxt,xSession,ySession
	if ScoreTxt!=0: can1.delete(SessionTxt)
	SessionTxt=can1.create_text(xSession,ySession,anchor='w',text='Session = '+str(session)+' / 5',font=arial14b,fill='red')
	
def HandleGame(N):
	#N contient le numéro du rectangle cliqué
	global btxt,NbreBonneReponse,Score,Session,Programme
	if N==NbreBonneReponse: 
		if btxt!=0: can1.delete(btxt)
		btxt=can1.create_text((MatDim[1,0]+MatDim[0,0])/2,MatDim[1,1]+20,anchor='center',text='BRAVO',font=arialLargeb,fill='red')
		can1.itemconfigure(carreau[int(ycol)][int(xcol)],fill='#00FF00')
		can1.update() #Sert à permettre l'affichage du BRAVO sinon on ne l'aperçoit pas malgré l'attente qui suit
		Score+=1
		DispScore(Score)
		Session+=1
		#Session=6
		if Session==6:
			#Nouvelle session
			if Score==5: SetColorRond(0,1,'#aaFFaa')
			else: SetColorRond(0,1,'red')
			Session=1
			nstxt=can1.create_text((MatDim[1,0]+MatDim[0,0])/2,yScore+25,anchor='center',text='Nouvelle session',font=arialLargeb,fill='black')
			can1.update() #Sert à permettre l'affichage du BRAVO sinon on ne l'aperçoit pas malgré l'attente qui suit
			time.sleep(2)
			can1.delete(nstxt)
			Programme=MatCallbacks[0,2]
			SetColorRond(0,2,'yellow')
		DispSession(Session)
		can1.update() #Sert à permettre l'affichage du BRAVO sinon on ne l'aperçoit pas malgré l'attente qui suit
		time.sleep(0.4)
		#fen1.after(1000,can1.delete(btxt))
		Quadrillage(MatDim)
		DeletePreviousRText() #Effacer le text de Rprintf avant de renouveler l'énoncé
		Programme() #On lance le programme de jeu choisi à partir de MatCallbacks
		if btxt!=0: can1.delete(btxt)

	else : 
		if btxt!=0: can1.delete(btxt)
		btxt=can1.create_text((MatDim[1,0]+MatDim[0,0])/2,MatDim[1,1]+20,anchor='center',text='FAUX',font=arialLargeb,fill='red')
		if xcol!=-1 and ycol!=-1: can1.itemconfigure(carreau[int(ycol)][int(xcol)],fill='#FF0000')

# -----------------------------------------------------------------

# ---------------- SOUS-ROUTINES DE GESTION DE LA SUITE DE PROGRAMMES -----------
def DamierRonds(DIM): #coin haut gauche et coin droit bas. Remarque: X>x et Y>y
# DIM=[x,y,Nx]
#     [X,Y,Ny]   Remarque: Nx est le nombre de carreaux sur une ligne
	global damier
	Nx=DIM[0,2]
	Ny=DIM[1,2]
	wx=np.abs(DIM[0,0]-DIM[1,0])/Nx #largeur d'une colonne
	wy=np.abs(DIM[0,1]-DIM[1,1])/Ny #hauteur d'une grille
	x=DIM[0,0]
	y=DIM[0,1]
#voir http://tkinter.fdex.eu/doc/caw.html?highlight=rectangle#Canvas.create_rectangle
	if damier!=0: can1.delete(damier)
	damier=[[can4.create_oval(x+i*wx,y+j*wy,x+(i+1)*wx,y+(j+1)*wy,fill="#dddddd") 
								for i in range(Nx)] for j in range(Ny)]
	for i in range(0,Ny-1):
		can4.create_text(18,MatDamier[0,1]+wy*(i+0.5),anchor='w',text='niveau '+str(i+1),font=arial12b,fill='grey')
	can4.create_text(0,MatDamier[0,1]+wy*(Ny-0.5),anchor='w',text='Problèmes ',font=arial12b,fill='grey')
	can4.create_text(0,MatDamier[0,1]-20,anchor='w',text='  Difficulté     1     2     3',font=arial12b,fill='grey')

def SetColorRond(i,j,col):
	#if col=='r': can4.itemconfigure(damier[j][i],fill='#FF0000')
	can4.itemconfigure(damier[i][j],fill=col)

# --------------------------------------------------------------------------------

btxt=0
WSaveList=[] #Initialisation de la liste pour mémoriser les bouts de text dans Rprintf pour effacer ensuite
#Rprintf(mytext,20,100,'red','blue') 
#DeletePreviousRText() #efface le texte écris par Rprintf


#----- C'est ici qu'on inclut les fichiers exos _in.py ------
# Attention ce ne sont pas des imports, pour l'inclusion il faudra passer par readprog.py
include Frac_inc.py

#Création d'une matrice 4x3 contenant les callbacks des divers programmes de jeu
#Il faudra l'implémenter à mesure de la construction
MatCallbacks = np.array([[0,JeuFraction1_1,JeuFraction1_2],
					[0,0,0],
					[0,JeuFraction3_2,0],
					[0,0,0],
					[0,0,0]])
# Damier=[x,y,Nx]
#        [X,Y,Ny]   Remarque: Nx est le nombre de ronds sur une ligne
MatDamier=np.array([[90,100,3],[170,220,4]])
can4.create_text(90,30,anchor='center',text='ENSEMBLE\n       DES\nEXERCICES',font=arial12b,fill='red')
DamierRonds(MatDamier)

SessionInit=1 #Pour lancer la phase d'initialisation  de la session à 1. Le reste du temps à 0 
#Démarrage avec JeuFraction1_1
Programme=MatCallbacks[0,1]
SetColorRond(0,1,'#aaaaFF')
Programme()

Coord=tk.Label(fen1)
Coord.grid(row=2,column=0)
can1.bind('<ButtonRelease>',clic) #La lecture des coordonnées souris est désormais possible
# ------- A partir d'ici la souris est liée et les réponses relevable -------


fen1.mainloop()

