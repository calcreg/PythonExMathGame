#
# -----------------------USAGE LICENSE and AUTHOR ---------------------------------------------#
# Licence GNU GPL. 
# This is a freeware, forbidden to be sold full or being part of a program to be sold.
# Author: Bussy-Socrate Regan.
# This program is aimed at maths teachers for their students to improve their knowledge through exercising and guidance.
# It is to be used as a basis for building a suite of exercises of gradual difficulties.
# Subroutine Rprintf is able to display latex (\sqrt{}, \frac{}{} and x^{y}, +, -) without the heavy ans slow latex package under python.
# It can easily be implemented for one who can program in python.
# This program is under GNU GPL License. The author permits the use of this program freely, its sharing, 
# but this header comments containing the license and the author should be kept inside the program.
# Developpers: Contact the author for significant contributions through pull requests. Respect the architecture using the ..._inc.py files.
# Developpers should think in a pedagogical way. Gradual exercises and comments available by click to help kids to fix knowledge.
# Please read the README.md to launch the program.

# Required file as part of the sofware:
# readprog.py, Frac_6_5_inc.py, SubRoutine1_3.py
#Launch with:
#python readprog.py ExJeuxMath6_5.py | python

import tkinter as tk
from tkinter import font as tkFont

from random import randrange
import time
import sys



#Select operating système because fonts are not the same size between linux and windows
sp = sys.platform #;print(sp)
if sp=="linux": OperatingSystem=0 #0 For Linux, 1 for Windows
else: OperatingSystem=1

WidthCan1=500; HeightCan1=500
Score=0;xScore=WidthCan1-90;yScore=10;ScoreTxt=0; 
TotalScore=0;xTotalScore=10;yTotalScore=240;TotalScoreTxt=0; 
Session=0;xSession=10;ySession=10;SessionTxt=0;ChgtSession=0
carreau=0; damier=0
xcol=-1;ycol=-1
MatDim=0
x_ex=0;y_ex=0 #used for RouteSheet
NoCountNextPoint=0  #If the student gives wrong answer, has possibility to set right answer but this will not be counted in the Score

fen1=tk.Tk()
#fen1.title('JEUX DE MATHEMATIQUES                      ')
if OperatingSystem==0: #Linux
	fen1.geometry('1120x530+50+100')
	fen1.title('JEUX DE MATHEMATIQUES                      ')
	arial14b = tkFont.Font(family='Arial', size=14,weight='bold')
	arial12b = tkFont.Font(family='Arial', size=12, weight='bold')
	arial10n = tkFont.Font(family='Arial', size=10, weight='normal')
	arial10b = tkFont.Font(family='Arial', size=10, weight='bold')
	arialm = tkFont.Font(family='Arial', size=8, weight='bold')
	arialLargeb = tkFont.Font(family='Arial', size=16, weight='bold')
	arialHUGEb = tkFont.Font(family='Arial', size=50, weight='bold')
else: #OperatingSystem==1: Windows
	fen1.geometry('1100x530+50+100')
	fen1.title('JEUX DE MATHEMATIQUES     (on windows10)          ')
	arial14b = tkFont.Font(family='Arial', size=13,weight='bold')
	arial12b = tkFont.Font(family='Arial', size=11, weight='bold')
	arial10n = tkFont.Font(family='Arial', size=9, weight='normal')
	arial10b = tkFont.Font(family='Arial', size=10, weight='bold')
	arialm = tkFont.Font(family='Arial', size=7, weight='bold')
	arialLargeb = tkFont.Font(family='Arial', size=15, weight='bold')
	arialHUGEb = tkFont.Font(family='Arial', size=49, weight='bold')


arial=arial14b #Initialisation here the font for Rprintf, Best use with arial12b and arial 14b

can1 = tk.Canvas(fen1, width =WidthCan1, height =HeightCan1,bg='white')
if OperatingSystem ==0: can2 = tk.Canvas(fen1, width =400, height =60,bg='white')
else:  can2 = tk.Canvas(fen1, width =380, height =60,bg='white')
can4 = tk.Canvas(fen1, width =180, height =HeightCan1-70,bg='white')
can5 = tk.Canvas(fen1, width =180, height =70,bg='white')

can1.grid(row=0,column=0,rowspan=2,padx=5,pady=2)
can2.grid(row=0,column=1,padx=5,pady=2)

can4.grid(row=1,column=2,padx=5,pady=0)
can5.grid(row=0,column=2,padx=5,pady=0)

#Image = tk.PhotoImage(file ='~/Bureau/ExJeuxPyMath/images/mandelbrot_bleached.png')
#item = can2.create_image(0, 0, image = Image,anchor='nw')
a=0;b=30
can2.create_text(a+2,b,anchor='w',text='FRACTIONS',font=arialHUGEb,fill='black')
can2.create_text(a,b+2,anchor='w',text='FRACTIONS',font=arialHUGEb,fill='red')

label=tk.Label(can5)
label.config(text = 'Selectionne ta classe')
label.grid(row=0,column=0,columnspan=4)

NbrClasse=0 #Initialisation to the classe 6ème
def sel():
	global NbrClasse
	#selection = "You selected the option " + str(var.get())
	#print(selection)
	NbrClasse=var.get() #0=6ème 1=5ème,...,3=3ème
	
var = tk.IntVar()
Radio = []
rtext = ["6e","5e","4e","3e"]
#iframe=tk.Frame(can2,bd=2,relief=tk.SUNKEN)
#print(iframe)

for i in range(4):
	Radio.append(tk.Radiobutton(can5, text=rtext[i], variable=var, value=i, command=sel,bg='#99FF99'))
	Radio[i].grid(row=1,column=i)

if OperatingSystem==0:
	TextWidth=40 #width of the window in characters
	txt = tk.Text(fen1,width=TextWidth, height=19,font=arial14b, wrap='word')
else:
	TextWidth=42 #width of the window in characters
	txt = tk.Text(fen1,width=TextWidth, height=22,font=arial14b, wrap='word')

Letxt="Le jeux ci-contre est un jeu de maîtrise sur le thème des fractions.\n"\
	"Réponds en cliquant la bonne réponse.\n\n"\
	"Si tu te trompes, tu dois quand même trouver la bonne réponse, mais le point n'est pas compté."
txt.insert(tk.END,Letxt)
txt.grid(row=1,column=1,padx=5,pady=2)

ScoreTxt=can1.create_text(xScore,yScore,anchor='w',text='Score = '+str(Score),font=arial14b,fill='red')
TotalScoreTxt=can4.create_text(xTotalScore,yTotalScore,anchor='w',text='Score Total= '+str(TotalScore),font=arialLargeb,fill='red')
can1.create_line(0,yScore+10,WidthCan1,yScore+10,width=2,fill='blue')
SessionTxt=can1.create_text(xSession,ySession,anchor='w',text='Session = '+str(Session)+' / 5',font=arial14b,fill='red')

mytext=r'On a : $1-\frac{265}{45}+2a=3+2=a+\frac{1}{2}+\sqrt{25}$.'

#Usage: \obj_rect{width, height, nbr col, nbr rows,color inside, color dashed, nbre square colored}
# $\obj_rect{60,20,1,1,9,6,1}$ is fully colored by color 6 = blue
# $\obj_rect{60,20,1,1,9,6,0}$ is empty color by inside color 9 = white



# ---------- Subroutines to display text and meta-text---------
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
			elif text[j:j+9] in {r'\obj_tab{'}: # Must be before elif text[j]=='\\' because of the spaceing used in items
				#print("in --> obj_tab")
				SpStr=""
				SpStr += text[j]
				j+=1
				while text[j]!='\\' and text[j]!=r'$': #Une seule operation a la fois
					SpStr += text[j]
					j+=1
				SpStr+=r'$' #On place un $ pour que SpecPrintf fonctionne correctement
				#print('SpStr='+SpStr)
				L=SpecPrintf(SpStr,tx,ty,L,col2)
			elif text[j:j+6] in {r'\frac{'}: #Specific problem for \frac as we must fill until the second '}'
				SpStr=""
				SpStr += text[j]
				j+=1
				while text[j]!=r'}': #First '}'
					SpStr += text[j]
					if text[j]=='$': print('Error, and of latex formula too early!'); return
					j+=1
				SpStr += text[j]; j+=1
				while text[j]!=r'}': #second '}'
					SpStr += text[j]
					if text[j]=='$': print('Error, and of latex formula too early!'); return
					j+=1
				SpStr += text[j]; j+=1
				SpStr+=r'$' #On place un $ pour que SpecPrintf fonctionne correctement
				#print('SpStr='+SpStr)
				L=SpecPrintf(SpStr,tx,ty,L,col2)				
			elif text[j]=='\\' : 
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
		str1+=text[i]
		i+=1
		ilength1=i+2 # Save character length between $ $
	str1+=text[i] #get the $
	#test du text entre $...$
	#print('pass2, str1 ='+ str1)
	if str1.count(r'\obj_rect{')!= 0: #Metatext this is not latex
		#print('pass3, str1 ='+ str1)
		#\obj_rect{width,height,ncol,nrows,colIn,ColDashed,NbrColored} Example: \obj_rect{50,20,1,1}
		i=10
		str3=""
		while str1[i]!='}' and str1[i]!='$':
			str3+=str1[i]
			i+=1
		ValList=eval(str3) #Creates a list of the different values separated by comas
		if len(ValList)!=7: print('error in obj_rect:should be 4 values')
		w_rect=int(ValList[0]);h_rect=int(ValList[1])
		ncol_rect=int(ValList[2]);nrows_rect=int(ValList[3])
		colIn=int(ValList[4]);colDashed=int(ValList[5]);NbrColored=int(ValList[6])
		rect_matdim=([[tx+L1,int(ty-h_rect/2),ncol_rect],[tx+L1+w_rect,int(ty+h_rect/2),nrows_rect]])
		#print(rect_matdim)
		RectDivision(rect_matdim,colIn,colDashed,NbrColored)
		#Remark: the WSaveList.append is made in RectDivision with the object creation
		L1=w_rect+L1 #Add the width of the object rectangle
		
	if str1.count(r'\obj_tab{')!= 0: #Metatext this is not latex 
		#This subroutine creates a table grid with arrow option display for proportionnal tables
		#\obj_tab{mode,color_in,color_out,L1_text1 & ... & L1_textn ; L2_text1 & ... & L2_textn} 
		#Remark: mode=0:Normal tabular, mode=1:proportionnal Tabular with arrow on right handside
		#print('pass3, str1 ='+ str1)
		i=9;str3="";coma=0
		while str1[i]!='}' and str1[i]!='$' and coma < 3: #3 parameters at beginning
			str3+=str1[i]
			i+=1
			if str1[i]==',': coma+=1
		i+=1 #We overtake the coma
		ValList=eval(str3) #Creates a list of the different values separated by comas
		#Remarks:mode=int(ValList[0])
		#		 color_in=int(ValList[1])
		#Here i contains the place of the third coma
		str2=""
		str3=""
		ListTab=[]
		while str1[i]!='}' and str1[i]!='$':
			if str1[i]=='&' or str1[i]==';' or str1[i]=='}':
				str2+=str1[i] #We take the special character in str2 this is useful to count lines and columns
				ListTab.append(str3) #Get the current item
				#print(str3)
				str3=""
				i+=1
			str2+=str1[i]
			str3+=str1[i]
			i+=1
		ListTab.append(str3) #Get the Last item not taken yet

		#print('pass3, str2 ='+ str2)
		#print('pass3, str3 ='+ str3)
		nlines=str2.count(';')+1 #Number of lines in the table
		ncolumns=str2.count('&')//nlines+1 #euclidian division to get number of columns
		if str2.count('&')%nlines !=0: print(r'syntax error in\obj_tab: number of columns and comas incoherence')
		Length0_max=0
		Length1_max=0
		#print('nlines,ncolumns=',nlines,ncolumns)
		#print(ListTab)
		for b in range(nlines):
			for a in range(0,ncolumns):
				if a==0: Length0_max=max(arial.measure(ListTab[b*ncolumns]),Length0_max) #get size of the first item
				else: Length1_max=max(arial.measure(ListTab[b*ncolumns+a]),Length1_max) #get the size of the others

		#Now we draw the tabular
		#print('Length0_max,Length1_max=',Length0_max,Length1_max)
		w_rect=(Length0_max+(ncolumns-1)*Length1_max)# *arial.measure('_')
		wline=27
		h_rect=wline*nlines
		#h_rect=arial.measure(' ')*3/2 * nlines #We estimate the height of a character using the width
		colors=['black','brown','red','orange','yellow','green','#8888FF','magenta','#dddddd','white']
		#print('ValList=',ValList)
		color_in=colors[int(ValList[1])]
		color_out=colors[int(ValList[2])]
		WSaveList.append(can1.create_rectangle(tx+L1,ty-h_rect/2,tx+L1+w_rect,ty+h_rect/2,outline=color_out,fill=color_in))
		#Vertical lines
		a=Length0_max#*arial.measure('_')
		b=Length1_max#*arial.measure('_')
		#print('a=',a,'Length0_max=',arial.measure(ListTab[0]),'Length1_max=',arial.measure(ListTab[3]))
		for i in range(ncolumns-1):
			WSaveList.append(can1.create_line(tx+L1+a+i*b,ty-h_rect/2,tx+L1+a+i*b,ty+h_rect/2,width=2,fill=color_out))
		for i in range(nlines-1):
			WSaveList.append(can1.create_line(tx+L1,ty+i*wline,tx+L1+w_rect,ty+i*wline,width=2,fill=color_out))
		#Place the text in the tabular. The text in the grid is centered except those on the left carrying the labels generally
		for i in range(nlines):
			for j in range(ncolumns):
				if j==0: WSaveList.append(can1.create_text(tx+L1,ty+(i-0.87)*h_rect/2,anchor='nw',text=ListTab[i*ncolumns+j],font=arial,fill=color2))
				else:  WSaveList.append(can1.create_text(tx+L1+a+(j-1)*b+(b-arial.measure(ListTab[i*ncolumns+j]))/2,ty+(i-0.87)*h_rect/2,anchor='nw',text=ListTab[i*ncolumns+j],font=arial,fill=color2))
		mode=int(ValList[0])
		if mode==0:
			L1=w_rect+L1 #Add the width of the object rectangle	
		elif mode==-1: #mode!=0: we put the arrow and the right of the tabular mode=1 arrow down, mode =-1 arrow up
			DrawArrow(tx+L1+w_rect+arial.measure(' '),ty+h_rect*0.3,tx+L1+w_rect+arial.measure(' '),ty-h_rect*0.3,-mode,6,'red','black')
			L1=w_rect+2*h_rect/3+L1 # this place taken is b=2a see DrawArrow subroutine
		elif mode==1:
			DrawArrow(tx+L1+w_rect+arial.measure(' '),ty+h_rect*0.3,tx+L1+w_rect+arial.measure(' '),ty-h_rect*0.3,-mode,6,'red','black')	
			L1=w_rect+2*h_rect/3+L1 # this place taken is b=2a see DrawArrow subroutine
	if str1.count(r'\sqrt{')!= 0:
		i=6
		str3=""
		while str1[i]!='}' and str1[i]!='$':
			str3+=str1[i]
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

# -----------------ROUTINE AFFICHAGE PLUSIEURS LIGNES DE TEXTE -----------------
def RdispText(text,tx,ty,space,col1,col2):
	#permet d'écrire des lignes
	a=text.find(r'\n')
	if a==-1:	Rprintf(text,tx,ty,col1,col2);return
	b=0
	str1=""
	while a!=0 and a!=-1:
		str1=""
		for i in range(b,a+b):
			str1+=text[i]
		#print('pass1,str1=',str1)
		Rprintf(str1,tx,ty,col1,col2)
		ty+=space
		str1=""
		b=a+b+2
		for i in range(b,len(text)):
			str1+=text[i]
		a=str1.find(r'\n')
#		print('a,b=',a,b,'str1='+ str1)
	Rprintf(str1,tx,ty,col1,col2)

# ----------------------------------------------------------------
# ----------------------------------------------------------------
#			SOUS-ROUTINES CREATION D'UNE GRILLE POUR CLIQUER
# ----------------------------------------------------------------
def R_abs(x): #Our own function for the absolue value
	if x<0: return -x
	return x

def clic4(event):
	global xcol,ycol,Score,Session,x_ex,y_ex,Programme
	#Launch a program just by clicking on the round in the Route exercises in can4
	#global MatDamier
	i=event.x
	j=event.y
	Nbre=GetNbre(MatDamier,i,j)
	#xcol and ycol contain the values of the column and the row
	if Nbre!=-1:
		#print('xcol,ycol=',xcol,ycol)
		#programme=MatCallbacks[int(ycol)][int(xcol)]#ycol is the lines
		SetColorRond(x_ex,y_ex,'#dddddd')
		x_ex=int(ycol);y_ex=int(xcol)
		#print('x_ex,y_ex=',x_ex,y_ex)
		Programme=RouteSheet(0,Score)
		#print('pass1:x_ex,y_ex=',x_ex,y_ex)
		#print('Program=',Programme)
		DispSession(Session)
		Score=0 #Local score is set back to zero for next set of questions
		DispScore(Score)
		if Programme!=0:
			Quadrillage(MatDim)
			DeletePreviousRText() #Effacer le text de Rprintf avant de renouveler l'énoncé
			SessionInit=1
			Programme()

def clic(event):
	#Warning, method is important as it describes the answering mode (QCM table; click position on axis)
	global Method,ZoneCL
	i=event.x
	j=event.y
	#print('click:Nx,Ny=',MatDim[0][2],MatDim[1][2])
	if Method==1:
		Nbre=GetNbre(MatDim,i,j)
		#print('Nbre=',Nbre)
		if Nbre >=0 : Coord['text']='Le rectangle cliqué est ('+str(Nbre)+'), coordonnées pointeur ('+str(i)+','+str(j)+')'
		else: Coord['text']='Hors quadrillage ('+str(Nbre)+'), coordonnées pointeur ('+str(i)+','+str(j)+')'
		HandleGame(Nbre)
		return
	if Method==2:
		Nbre=GetNbre2(ZoneCL,i,j)
		if Nbre >=0 : Coord['text']='Le rectangle cliqué est ('+str(Nbre)+'), coordonnées pointeur ('+str(i)+','+str(j)+')'
		else: Coord['text']='Hors quadrillage ('+str(Nbre)+'), coordonnées pointeur ('+str(i)+','+str(j)+')'
		HandleGame(Nbre)
		return
	if Method==3:
		Nbre=GetNbre2(ZoneCL,i,j)
		if Nbre >=0 : Coord['text']='Le rectangle cliqué est ('+str(Nbre)+'), coordonnées pointeur ('+str(i)+','+str(j)+')'
		else: Coord['text']='Hors quadrillage ('+str(Nbre)+'), coordonnées pointeur ('+str(i)+','+str(j)+')'
		CallbackAnswer(Nbre)
		return
	print('Wrong Method used! should be 1 or 2 in the program')
	
def RectDivision(DIM,colin,coldashed,nbrcolored): #coin haut gauche et coin droit bas. Remarque: X>x et Y>y
# DIM=[x,y,Nx]
#     [X,Y,Ny]   Remarque: Nx est le nombre de carreaux sur une ligne
	Nx=int(DIM[0][2])
	Ny=int(DIM[1][2])
	wx=R_abs(DIM[0][0]-DIM[1][0])/Nx
	wy=R_abs(DIM[0][1]-DIM[1][1])/Ny
	x=DIM[0][0];y=DIM[0][1]
#	print ('Nx,Ny=',Nx,Ny)
#	colors=['black','brown','red','orange','yellow','green','blue','magenta','grey','white']
	colors=['black','brown','red','orange','yellow','green','#8888FF','magenta','#dddddd','white']
	matcol=[]
	for i in range(Nx*Ny):
		if i<nbrcolored: matcol.append(coldashed)
		else: matcol.append(colin)
	[[WSaveList.append(can1.create_rectangle(x+i*wx,y+j*wy,x+(i+1)*wx,y+(j+1)*wy,fill=colors[matcol[j+i*Ny]])) 
								for i in range(Nx)] for j in range(Ny)]
			

def Quadrillage(DIM): #coin haut gauche et coin droit bas. Remarque: X>x et Y>y
# DIM=[x,y,Nx]
#     [X,Y,Ny]   Remarque: Nx est le nombre de carreaux sur une ligne
	global carreau
	Nx=DIM[0][2]
	Ny=DIM[1][2]
	wx=R_abs(DIM[0][0]-DIM[1][0])/Nx
	wy=R_abs(DIM[0][1]-DIM[1][1])/Ny
	x=DIM[0][0]
	y=DIM[0][1]
#voir http://tkinter.fdex.eu/doc/caw.html?highlight=rectangle#Canvas.create_rectangle
	#if carreau!=0: 
	#	for handle in carreau[0]: can1.delete(handle) #effacer le tableau
	DeleteQuadrillage(carreau)
		#Ce tableau est en fait une liste de handleur sur une liste
	#A la difference de np.array (où mat[i,j]) on a mat[i][j]
	carreau=[[can1.create_rectangle(x+i*wx,y+j*wy,x+(i+1)*wx,y+(j+1)*wy,activewidth=2,fill="#dddddd")
								for i in range(Nx)] for j in range(Ny)]
def DeleteQuadrillage(squares):
	if squares!=0: 
		for handle in squares[0]: can1.delete(handle) #effacer le tableau
	


def GetNbre(DIM,x,y):
	#DIM est une matrice 2,3 contenant les dimensions du tableau
	#x et y contiennent les coordonnées du point cliqué
	global xcol,ycol
	dX=(DIM[1][0]-DIM[0][0])
	dY=(DIM[1][1]-DIM[0][1])
	Nx=DIM[0][2]
	Ny=DIM[1][2]
	x0=DIM[0][0]
	y0=DIM[0][1]
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

def GetNbre2(zonecl,x,y):
	#zonecl should be a pointer on ZoneCL which contains the clickable unlinked rectangles on axis or else
	#x and y are the clicked coordinates
	for i in range(len(zonecl)):
		if x >= zonecl[i][0] and x <= zonecl[i][2]:
			if y >= zonecl[i][1] and y <= zonecl[i][3]:
				#print('nbre clicked is: ',i)
				return i
	#clicked outside the group of rectangles then return code -1
	return -1
	
def PlaceTxt(DIM,Numero,txt,col1,col2):
	#Sert à placer dans le tableau directement le text numérique ou mathématique
	dX=(DIM[1][0]-DIM[0][0]) #Largeur totale du tableau
	dY=(DIM[1][1]-DIM[0][1]) #Hauteur totale du tableau
	Nx=DIM[0][2]
	Ny=DIM[1][2]
	x0=DIM[0][0]
	y0=DIM[0][1]
	x=x0+(Numero%Nx)*dX/Nx
	y=y0+(Numero//Nx+0.5)*dY/Ny
	#print(r'Numero%Nx=',Numero%Nx)
	#print('emplacement x,y =',x,y)
	Rprintf(txt,x,y,col1,col2)

def DispScore(score):
	global ScoreTxt,xScore,yScore
	if ScoreTxt!=0: can1.delete(ScoreTxt)
	ScoreTxt=can1.create_text(xScore-arialLargeb.measure(str(score)),yScore,anchor='w',text='Score = '+str(score),font=arialLargeb,fill='red')

def DispTotalScore(score):
	global TotalScoreTxt,xTotalScore,yTotalScore
	if TotalScoreTxt!=0: can4.delete(TotalScoreTxt)
	TotalScoreTxt=can4.create_text(xTotalScore,yTotalScore,anchor='w',text='Score Total= '+str(TotalScore),font=arialLargeb,fill='red')


def DispSession(session):
	global SessionTxt,xSession,ySession
	if ScoreTxt!=0: can1.delete(SessionTxt)
	SessionTxt=can1.create_text(xSession,ySession,anchor='w',text='Session = '+str(session)+' / 5',font=arial14b,fill='red')
	
def HandleGame(N):
	#N contient le numéro du rectangle cliqué
	global btxt,NbreBonneReponse,Score,TotalScore,Session,Programme,NoCountNextPoint,ZoneCL
	xtxt=10;ytxt=10 #Obsolete Init Values
	if Method==1:
		xtxt=(MatDim[1][0]+MatDim[0][0])/2 ; ytxt=MatDim[1][1]+10
	if Method==2: 
		xtxt=WidthCan1/2;
		a=yScore
		for i in range(len(ZoneCL)):
			a=max(a,ZoneCL[i][3])
		ytxt=a+60 #BRAVO and FAUX text are located under the lowest square among those in ZoneCL

	if N==NbreBonneReponse: 
		if btxt!=0: can1.delete(btxt)
		if NoCountNextPoint==0: #This is if no error was made
			#print('BRAVO!!!')
			btxt=can1.create_text(xtxt,ytxt,anchor='center',text='BRAVO',font=arialLargeb,fill='red')
			Score+=1; DispScore(Score)
			can1.update() #Neede to display text that wouldn't appear otherwise
		else:
			NoCountNextPoint=0
			btxt=can1.create_text(xtxt,ytxt,anchor='center',text='Réponse Correcte',font=arialLargeb,fill='red')
			can1.update() #Neede to display text that wouldn't appear otherwise
		if Method==1: 
			can1.itemconfigure(carreau[int(ycol)][int(xcol)],fill='#00FF00')
			can1.update() #Sert à forcer l'affichage pour ensuite attendre avec time.sleep
		if Method==2: 
			#can1.itemconfigure(ZoneCL[int(N)][4],fill='#00FF00')#The 5th value is the handler of the rectangle see SubRoutine1_(2+).py
			x0=(ZoneCL[int(N)][0]+ZoneCL[int(N)][2])/2
			y0=(ZoneCL[int(N)][1]+ZoneCL[int(N)][3])/2
			w=5
			#Draw a green cross as a right answer
			WSaveList.append(can1.create_line(x0-w,y0,x0+w,y0,width=w,fill='#00FF00'))
			WSaveList.append(can1.create_line(x0,y0-w,x0,y0+w,width=w,fill='#00FF00'))
			can1.update() #Sert à forcer l'affichage pour ensuite attendre avec time.sleep
		time.sleep(0.8)
		Session+=1
		if Session < 6: DispSession(Session)
		if btxt!=0: can1.delete(btxt)
	else : 
		if btxt!=0: can1.delete(btxt)
		if N!=-1: #If click is inside the tabular
			btxt=can1.create_text(xtxt,ytxt,anchor='center',text='FAUX',font=arialLargeb,fill='red')
			if Method==1: can1.itemconfigure(carreau[int(ycol)][int(xcol)],fill='#FF0000')
			if Method==2: 
				can1.itemconfigure(ZoneCL[int(N)][4],fill='#FF0000')#The 5th value is the handler of the rectangle see SubRoutine1_(2+).py
				can1.update()
			NoCountNextPoint=1 #Give the chance to set the right answer but will not count it in the Score
		return
		
	if Session==6:
		#Nouvelle session
		Session=1
		TotalScore+=Score #Accumulates a total  score
		DispTotalScore(TotalScore)
		nstxt=can1.create_text(WidthCan1/2,yScore,anchor='center',text='Nouvelle session',font=arialLargeb,fill='black')
		can1.update() #Sert à permettre l'affichage du BRAVO sinon on ne l'aperçoit pas malgré l'attente qui suit
		time.sleep(2)
		can1.delete(nstxt)
		Programme=RouteSheet(1,Score)
		DispSession(Session)
		Score=0 #Local score is set back to zero for next set of questions
		DispScore(Score)
		#can1.update() #Sert à permettre l'affichage du BRAVO sinon on ne l'aperçoit pas malgré l'attente qui suit
		#time.sleep(0.8)
	if Method==1: Quadrillage(MatDim)
	DeletePreviousRText() #Effacer le text de Rprintf avant de renouveler l'énoncé
	Programme() #On lance le programme de jeu choisi à partir de MatCallbacks



# ---------------- SOUS-ROUTINES DE GESTION DE LA SUITE DE PROGRAMMES -----------
def DamierRonds(DIM): #coin haut gauche et coin droit bas. Remarque: X>x et Y>y
# DIM=[x,y,Nx]
#     [X,Y,Ny]   Remarque: Nx est le nombre de carreaux sur une ligne
	global damier
	Nx=DIM[0][2]
	Ny=DIM[1][2]
	wx=R_abs(DIM[0][0]-DIM[1][0])/Nx #largeur d'une colonne
	wy=R_abs(DIM[0][1]-DIM[1][1])/Ny #hauteur d'une grille
	x=DIM[0][0]
	y=DIM[0][1]
#voir http://tkinter.fdex.eu/doc/caw.html?highlight=rectangle#Canvas.create_rectangle
	if damier!=0: can1.delete(damier)
	damier=[[can4.create_oval(x+i*wx,y+j*wy,x+(i+1)*wx,y+(j+1)*wy,activewidth=2,fill="#dddddd") 
								for i in range(Nx)] for j in range(Ny)]
	for i in range(0,Ny-1):
		can4.create_text(18,MatDamier[0][1]+wy*(i+0.5),anchor='w',text='niveau '+str(i+1),font=arial12b,fill='grey')
	can4.create_text(0,MatDamier[0][1]+wy*(Ny-0.5),anchor='w',text='Problèmes ',font=arial12b,fill='grey')
	can4.create_text(0,MatDamier[0][1]-20,anchor='w',text='  Difficulté     1     2     3',font=arial12b,fill='grey')

def SetColorRond(i,j,col):
	#if col=='r': can4.itemconfigure(damier[j][i],fill='#FF0000')
	if col=='#aaaaaa': can4.itemconfigure(damier[i][j],outline='white',fill=col)
	else: can4.itemconfigure(damier[i][j],fill=col)
	fen1.update()
# --------------------------------------------------------------------------------
# --------- Success handling and course-sheet around the exercises ----------
def DisplayRouteSheet():
	for i in range(4):
		for j in range(3):
			if MatCallbacks[i][j]==0: SetColorRond(i,j,'#aaaaaa') #white for unused
	#print(MatCallbacks)

def RouteSheet(cmd,score):
	global x_ex,y_ex,SessionInit
	SessionInit=1
	#print('pass2:x_ex,y_ex=',x_ex,y_ex)
	if cmd==0:
		Score=score #Initialisation with a certain value of Score
		#Search for the program to start with.
		#Entry point chosen at MatCallbacks[0][1]
		#x_ex=0;y_ex=1
		SetColorRond(x_ex,y_ex,'#9999ff') #Signifies this one is being done
		return MatCallbacks[x_ex][y_ex]
	#print('Score=',score)
	if score==5: SetColorRond(x_ex,y_ex,'#aaFFaa') #validates
	else: SetColorRond(x_ex,y_ex,'red') #write failed
	#Algorithme to Choose the next program 
	if score ==5:
		if y_ex <= 1 and MatCallbacks[x_ex][y_ex+1]!=0:
			y_ex+=1; 
			SetColorRond(x_ex,y_ex,'#9999ff')
			return MatCallbacks[x_ex][y_ex]
		else:
			x_ex+=1
			for i in range(3):
				if MatCallbacks[x_ex][i]!=0:
					y_ex=i
					SetColorRond(x_ex,y_ex,'#9999ff')
					return MatCallbacks[x_ex][y_ex]
	#If score<5 then:
	if y_ex >= 1:
		if MatCallbacks[x_ex][y_ex-1]!=0: y_ex=y_ex-1
		SetColorRond(x_ex,y_ex,'#9999ff')
		return MatCallbacks[x_ex][y_ex]
# Sinon on ne bouge rien et il faut recommencer
	SetColorRond(x_ex,y_ex,'#9999ff')
	return MatCallbacks[x_ex][y_ex]

# -----------------------------------------------------------------------------------

btxt=0
WSaveList=[] #Initialisation de la liste pour mémoriser les bouts de text dans Rprintf pour effacer ensuite
#arial=arial12b;RdispText(myBigtext,0,170,25,'red','blue');arial=arial14b
#DeletePreviousRText() #efface le texte écris par Rprintf

#Answering Method: Method=1 => Click in an array of sticked rectangles
#					Method=2 => Click in separated rectangles at definite places (example: points on an axis)

Method=1 #This is the clicking methode for sticked rectangles
ZoneCL=[] #initialize the table containing the coordinates eventually of the rectangles  (Method=2)
#----- C'est ici qu'on inclut les fichiers exos _in.py ------
# Attention ce ne sont pas des imports, pour l'inclusion il faudra passer par readprog.py
include Frac_6_5_inc.py
#The subroutines to display arrows and containing Rsqrt:
include SubRoutine1_3.py

#Création d'une matrice 4x3 contenant les callbacks des divers programmes de jeu
#Il faudra l'implémenter à mesure de la construction
MatCallbacks = ([[JeuFraction0_0,JeuFraction0_1,JeuFraction0_2],
					[JeuFraction1_0,JeuFraction1_1,JeuFraction1_2],
					[JeuFraction2_0,JeuFraction2_1,JeuFraction2_2],
					[JeuFraction3_0,0,0],
					[0,0,0]])
# Damier=[x,y,Nx]
#        [X,Y,Ny]   Remarque: Nx est le nombre de ronds sur une ligne
MatDamier=([[90,100,3],[170,220,4]])
can4.create_text(90,30,anchor='center',text='ENSEMBLE\n       DES\nEXERCICES',font=arial12b,fill='red')
DamierRonds(MatDamier)
#Set color with regards to the existing exercises in MatCallBacks
DisplayRouteSheet()

#SessionInit=1 #Pour lancer la phase d'initialisation  de la session à 1. Le reste du temps à 0 
#Démarrage avec JeuFraction1_1
#x_ex=0; y_ex=0;Programme=RouteSheet(1,0) #0 for starting, this set the value for programme
x_ex=0;y_ex=1
Programme=RouteSheet(0,0) #0 for starting, this set the value for programme
#Programme=MatCallbacks[0][2]
#print(MatCallbacks)
#print(Programme)
Programme()

Coord=tk.Label(fen1)
Coord.grid(row=2,column=0)
can1.bind('<ButtonRelease>',clic) #La lecture des coordonnées souris est désormais possible
can4.bind('<ButtonRelease>',clic4) #La lecture des coordonnées souris est désormais possible
# ------- A partir d'ici la souris est liée et les réponses relevable -------


fen1.mainloop()

