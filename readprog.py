import sys
#print(sys.argv)
#print(sys.argv[1])
#Lecture du main.py
#Lancer par: python3 readprog.py ExJeuxMath4.py |python3
#Les fichiers *_inc.py doivent être dans le même répertoire.
#Le programme readprog.py sert à réaliser un include sans faire un import
#Comme cela on peut développer chaque programme de jeu à part et il est inclus par readprog
#On pipe le résultat dans python3
#Pour la création d'un executable, il suffira de faire:
#python3 readprog.py ExJeuxMath4.py > fichier_final.py


file = open(sys.argv[1],'r') 

texte=file.read()
while texte.find('include')!=0 and texte.find('include')!=-1:
	place_a = texte.find('include')
	print(texte[0:place_a])
	linelength=texte[place_a:-1].find('\n')
	file2name=texte[place_a+len('include '):place_a+linelength]
	file2 = open(file2name,'r') 
	texte2=file2.read()
	#Insertion du programme_inc.py
	print(texte2)
	#Suite du main.py
	file2.close()
#	texte2.destroy()
	
	texte=texte[place_a+linelength+1:-1] #On prend la suite du texte dans texte pour relancer la boucle while

print(texte) #On imprime la fin du texte
file.close()

