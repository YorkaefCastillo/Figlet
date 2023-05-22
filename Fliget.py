import pyfiglet as glet
import random


Font = ["slant", "3-d", "3x5", "5lineoblique", "alphabet", "banner3-D", "doh", "isometric1", "letters", "alligator", "dotmatrix", "bubble", "bulbhead", "digital"]
ador = ""
#<----------------------------------------------------------------
Titulo = glet.figlet_format("FIGLET".center(50), font=f"{random.choice(Font)}")
print(Titulo)

#<----------------------------------------------------------------
print(f"Bienvenido a figlet".upper())


for id, x in enumerate(Font):
    print(f"{id}: {x}")
    print(glet.figlet_format(x , font= x))


print(f"\nSeleccione que Numero de 'Font' Quiere\n{ador.center(50, '*')}".upper() )
Select = input("Numero de Figlet: ")

palabra = input(f"{ador.center(50,'*')}\nDame una Palabra: ")
print(glet.figlet_format(palabra, font=Font[int(Select)]))
