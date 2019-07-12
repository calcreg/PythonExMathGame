# PythonExMathGame
This program on Python is aimed at students in highschool and for teachers to use as a basis for developping quickly a suite of exercises. 
A minimum level in Python is required.
A set of routine is built to display math equations without the heavy Latex import. It helps display square root, power and fractions as Latex does.
This program is under GNU GPL license. Everyone can use it reminding the GPL license and the author BUSSY-SOCRATE Regan teacher in high school.

A special care is to be given regarding the set of programs:
One can tell it is badly programmed with regards to 'Python programming conventions', but the interactivity between the subroutines imposed the necessity create an include of extra files directly in the main program instead of trying circular imports which fail (two different imports which call routines one from the other). 
Therefore the launching of the program is be made using 'readprog.py' to include the '..._inc.py' various exercise files and a pipe to redirect the output in python3.
Remark: The program can easily run under previous version of python. Use Tkinter instead of tkinter to run below version 3 of python.

Launch can be made using two methods:
Using a pipe to redirect in python
1. open a terminal
2. python3 readprog.py ExJeuxMath4_2.py | python3

Creating a file to be launched with python
1. open a terminal
2. python3 readprog.py ExJeuxMath4_2.py > ExJeuxMath.py
3. python3 ExJeuxMath.py




