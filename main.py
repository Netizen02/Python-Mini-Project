#import pygame
#from pygame import mixer
#pygame.init()
#mixer.music.load("Everybody's Circulation (Mashup) - TMABird.mp3")
#mixer.music.play()

name=input('Enter the name of your character\n')

class character:
    def __init__(self,race,hp,stealth,strength,charisma):
        self.race = race
        self.hp = hp
        self.stealth = stealth
        self.str = strength
        self.charisma = charisma
char_1 = character('Human',500,500,550,True)
char_2 = character('Elf',600,600,450,True)
char_3 = character('Dwarf',600,450,600,False)
char_4 = character('Rito',500,550,500,False)


x= int(input('Choose race'))#Idhar apna daal de

if x==1:
    y=char_1
elif x==2:
    y=char_2
elif x==3:
    y=char_3
elif x==4:
    y==char_4
else:
    print('Please choose a valid race!')

weapon = int(input('''It's dangerous to go alone! Pick a Weapon
1) Sword
2) Axe
3) Mace
'''))

