#import pygame
#from pygame import mixer
#pygame.init()
#mixer.music.load("Everybody's Circulation (Mashup) - TMABird.mp3")
#mixer.music.play()

name=input('Enter the name of your character\n')

class character:
    def __init__(self,race,hp,stealth,strength,charisma,home):
        self.race = race
        self.hp = hp
        self.stealth = stealth
        self.str = strength
        self.charisma = charisma
        self.home = home

x= int(input(f"""Welcome {name}.Before you begin the game you must choose a race. Given below are some of the races that 
inhabit this land. Choose wisely:

1.  Human

    Humans are one of the most charismatic races of this realm. They are strong and fast. Humans are often underestimated 
    by the other races as they aren’t the strongest, nor the most stealthy. But the humans are crafty and flexible to any
    given situation. Humans are known for their cunning and clever ways to get out of any situation. However, they are very 
    much capable of battle and war where it may be needed.

2.  Elf

    Elves are the smartest of the four races. They are an advanced species who pride themselves on their intelligence. Elves 
    may be small, but they aren’t weak. It is a matter of pride for an elf to be able to get out of any situation. Their 
    stealth enables them to evade and dodge any war that comes their way.

3.  Dwarf

    The dwarf is a simple creature. They are smart and hardy, but loud and obnoxious. What they lack in stealth, they more
    than make up for in strength. It is said that an army of dwarfs has never lost a battle, no matter the odds. The dwarfs
    are predominantly from the mines, and are well-versed in explosives and jewels.

4.  Rito

    The rito are a strong race. They have the body of a human with wings, but they have the head of a bird. They are covered
    in feathers. Rito are predominantly situated in the mountains, which is easy for them considering they can scale any
    mountain via flight. The rito are known for their aerial archers and their strength, the way humans are known for their
    charisma and versatility.
"""))

if x==1:
    y=character('Human',500,500,550,True,'Cyrodill' )
elif x==2:
    y=character('Elf',600,600,450,True,'Valenwood')
elif x==3:
    y=character('Dwarf',600,450,600,False,'Moria')
elif x==4:
    y=character('Rito',500,550,500,False,'High Rock')
else:
    print('Please choose a valid race!')

weapon = int(input('''It's dangerous to go alone! Pick a Weapon
1) Sword
2) Axe
3) Mace
'''))
if weapon==1:
    weapon='sword'
elif weapon ==2:
    weapon='axe'
elif weapon ==3:
    weapon='mace'
else:
    print('Please choose a valid option!')

def lvl_1_intro():

    print("""After returning form {y.home} you thought the worst was behind you. The war was over, and
here you were, sitting in an inn enjoying a pretty good ale. The horrors of the battlefield were
behind you, or so you thought. The hour is late, and you’re weary from your travels. All you want
is the warm embrace of a soft feather bed and the sweet scent of lilacs from the grove nearby. You
excuse yourself, but your drinking buddies hardly seem to notice, but you can’t blame them, it’s been
a while since either of you have felt this free. You head back to your room on the 3rd floor and call
it a day…
        
You wake up to the sound of a loud crash.Coughing and disoriented, you realize the inn is on fire. No 
this is no dream, you're not back in {y.home}. This is here, this is now and time is running out. The 
door flings open as a man clad in armor leaps at you. You doge his attack at the last minute, quickly 
knocking him out with your bedside oil lamp. You need to get out of here!\n""")

    print("Do you jump out of the window? Or would you rather try and fight your way out of this nightmare?")

def lvl_1_1_rsafe():

    print(f"""You leap through the window, using your wings to descend safely. Looking back, you see the burning 
inn, listen to the cries of the people still trapped inside. There is nothing you can do for them now, it’s 
way too dangerous to go back inside. You pick up a {weapon} form one of the corpses outside, catch your breath 
and continue down the road.This night is far from over…
""")

def lvl_1_1_esafe():

    print(f"""You leap through the window, using your elevn agility to climb down safely. Looking back, you see the 
burning inn, listen to the cries of the people still trapped inside. There is nothing you can do for them now, 
it’s way too dangerous to go back inside. You pick up a {weapon} form one of the corpses outside, catch your 
breath and continue down the road.This night is far from over…
""")

def lvl_1_1_hurt():

    print(f"""You leap through the window, but don’t quite stick the landing. You’re hurt and you know it, but you also 
know it isn’t safe to stick around here. You manage to get up on your feet and look back at the burning inn, 
listening to the cries of the people still trapped inside. There is nothing you can do for them now, 
it’s way too dangerous to go back inside. You pick up a {weapon} form one of the corpses outside, 
catch your breath and continue down the road.This night is far from over…
""")

    y.hp -= 100

def lvl_1_2_inn():
    print(f"""You grab the man’s {weapon}, and make your way downstairs, all while the whole building collapses around 
you.There are people trapped, people who can’t defend themselves, but there’s no time to save them. A few men do
try to attack you again but you make quick work of them.It’s not long before you find yourself right in front of
the main door. Just as you're about to leave, a huge brute jumps walks in,blocking the exit.You quickly hide 
behind the counter, contemplating your next move…
    
Do you fight him or try and sneak out""")

def lvl_1_2_sneak_ye():
    print(f"""You successfully sneak out from behind him!As you walk out you find no other enemies outside.Looking back,
you see the burning inn, listen to the cries of the people still trapped inside. There is nothing you can do for
them now. You catch your breath and continue down the road.This night is far from over…
""")


def lvl_1_2_sneak_nu():
    print(f"""The brute notices you sneaking around!He approaches you and swings his club wildly,knocking you on the 
ground. He stands over you, ready to finish you off when suddenly a large burning beam falls on him. You got lucky! 
But don’t count on luck all the time. You manage to walk out,still reeling from the hit you took. As you walk out
you find no other enemies outside.Looking back, you see the burning inn, listen to the cries of the people still
trapped inside. There is nothing you can do for them now. You catch your breath and continue down the road.This
night is far from over…
""")

    y.hp -=50

def lvl_1_2_attack_ye():
    print(f"""You jump out from behind the counter, confronting the brute in front of you.He is no match for your skill 
and before long he lies defeated at your feet. As you walk out you find no other enemies outside.Looking back, 
you see the burning inn, listen to the cries of the people still trapped inside. There is nothing you can do for 
them now. You catch your breath and continue down the road.This night is far from over…
""")

def lvl_1_2_attack_ye_2():
    print(f"""You jump out from behind the counter, confronting the brute in front of you.He proves to be a worthy adversary
. You take quite a few hits from him, but eventually you get the upper hand and manage to overpower him! . As 
you walk out you find no other enemies outside.Looking back, you see the burning inn, listen to the cries of the
people still trapped inside. There is nothing you can do for them now. You catch your breath and continue down 
the road.This night is far from over…
""")

    y.hp -= 50

def lvl_1_2_attack_nu():
    print(f"""You jump out from behind the counter, confronting the brute in front of you.A foolish decision!He quickly 
overpowers you and knocks you on the ground with his club. He stands over you, ready to finish you off when suddenly 
a large burning beam falls on him. You got lucky! But don’t count on luck all the time. You manage to walk out,still 
reeling from the hit you took. As you walk out you find no other enemies outside.Looking back, you see the burning 
inn, listen to the cries of the people still trapped inside. There is nothing you can do for them now. You catch 
your breath and continue down the road.This night is far from over…
""")

    y.hp -=100

def lvl_1_3():
    print(f"""You’re walking along the dark road, thinking about what just happened. You look at your {weapon} more closely, 
and see something rather interesting, a brand. You have seen this before.Surely this is the symbol of the great blacksmith
Feca of Tiefling.But he doesn't just hand out his weapons to common mercenaries, no there is more to this.The only person 
who can tell you more about this is Feca himself. Looks like you’re going to Tiefling village.

On the way to Tiefling, you spot a small camp of mercenaries. They’re wearing the same armor as the ones who attacked the inn.
It’s not a company you recognize, could there be something more sinister at play here? 

Do you want to infiltrate the camp? Or do you want to move on to Tiefling village?
""")

lvl_1_intro()
c1= int(input(''))

if c1==1:
    if y.race == 'Elf':
        lvl_1_1_esafe()
    elif y.race == 'Rito':
        lvl_1_1_rsafe()
    else:
        lvl_1_1_hurt()
elif c1==2:
    lvl_1_2_inn()
    c2=int(input(''))
    if c2==1:
        if y.str>=550:
            lvl_1_2_attack_ye()
        elif y.str>=500 and y.str<550:
            lvl_1_2_attack_ye_2()
        else :
            lvl_1_2_attack_nu()
    elif c2==2:
        if y.stealth>=500:
            lvl_1_2_sneak_ye()
        else:
            lvl_1_2_sneak_nu()

lvl_1_3()
