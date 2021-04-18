import pygame
from pygame import mixer
pygame.init()
mixer.music.load("Everybody's Circulation (Mashup) - TMABird.mp3")
mixer.music.play()
name=input('uiwhauid')

class character:
    def __init__(self,race,hp,stealth,strength):
        self.race = race
        self.hp = hp
        self.stealth = stealth
        self.str = strength

char_1 = character('elf',10000,250,600)
char_2 = character('human',800,300,4000)

x= int(input('fefewef'))

if x==1:
    y=char_1
else:
    y=char_2
def lvl1():
    print(f'ompmpompmpmpop {y.race} sw')

lvl1()

z= input("wefwefe")
mixer.music.load("mgs.mp3")
mixer.music.play()
a=int(imput('dwf'))

