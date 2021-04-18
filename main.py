#import pygame
#from pygame import mixer
#pygame.init()
#mixer.music.load("Everybody's Circulation (Mashup) - TMABird.mp3")
#mixer.music.play()

class character:
    def __init__(self,race,hp,stealth,strength,charisma):
        self.race = race
        self.hp = hp
        self.stealth = stealth
        self.str = strength
        self.charisma = charisma

name=input('Enter the name of your character\n')
print('\n\nWelcome '+ name +' Before you begin the game you must choose a race. Given below are some of the races that inhabit this land. Choose wisely:\n1.  Human\n\tHumans are the charismatic of the four races of this realm. They are strong and fast. Humans are often underestimated by the other races as they aren’t the strongest, nor the most stealthy. But the humans are crafty and flexible to any given situation. Humans are known for their cunning and clever ways to get out of any situation. However, they are very much capable of battle and war where it may be needed.\n2.  Elf\n\tElves are the smartest of the four races. They are an advanced species who pride themselves on their intelligence. Elves may be small, but they aren’t weak. It is a matter of pride for an elf to be able to get out of any situation. Their stealth enables them to evade and dodge any war that comes their way.\n3.  Dwarf\n\tThe dwarf is a simple creature. They are smart and hardy, but loud and obnoxious. What they lack in stealth, they more than make up for in strength. It is said that an army of dwarfs has never lost a battle, no matter the odds. The dwarfs are predominantly from the mines, and are well-versed in explosives and jewels. \nRito\n\tThe rito are a strong race. They have the body of a human with wings, but they have the head of a bird. They are covered in feathers. Rito are predominantly situated in the mountains, which is easy for them considering they can scale any mountain via flight. The rito are known for their aerial archers and their strength, the way humans are known for their charisma and versatility.')
x= int(input('Choose race'))

if x==1:
    y=character('Human',500,500,550,True)
elif x==2:
    y=character('Elf',600,600,450,True)
elif x==3:
    y=character('Dwarf',600,450,600,False)
elif x==4:
    y=character('Rito',500,550,500,False)
else:
    print('Please choose a valid race!')

weapon = int(input("It's dangerous to go alone! Pick a Weapon\n1) Sword\n2) Axe\n3) Mace"))

