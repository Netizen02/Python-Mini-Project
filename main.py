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

    print(f"""After returning form {y.home} you thought the worst was behind you. The war was over, and
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

def lvl_2():
    print(f"""
As you approach the camp you notice something curious. The men are happy and merry as if they just came back from battle
victorious. You decide to get closer in the camp. As you sneak around in the camp you hear someone speak. You crouch down
low lest you be found. 

"I don't believe that nasty little peice of shit had a chance. No one could have survived that burning inn. Revan will be
pleased when we bring him his head. Now let's enjoy the stupidity of the recruits we picked up from Tiefling." 

After saying this the men leave. You breathe a little easy, but realize...These are the same men who attacked you!
They walk away to a set of tents. Everyone seems to retire to their tents now. 

It seems that the camp is going to sleep...
""")

    d1 = int(input("\nDo continue to sneak(press 1) or Do you attack(press 0)?\t"))

    if d1 == 1:
        print(f"""
You continue to sneak around the outskirts of the camp. Soon you see another {y.race}. He goes to a nearby lake to swim 
and bathe. You quietly manage to steal his clothes and armor. You put your visor down so no one will recognise you.
""")
        if (y.stealth >= 550 and y.stealth <=600) :
            print(f"""
            
You hear a voice. "Hey! You! give me back my armor." You turn around and you quickly attack with your{weapon} before he 
makes anymore noise. Even though he puts up a fight, he is no match for you. He dies quickly when you land a strong blow
with your {weapon} on his head. You quickly tie his legs to a stone using a nearby vine. You pick up the body and throw 
it into the lake. The stone keeps the body from floating up.
            """)

        print(f"""
You enter the camp without suspicion. As you are walking through the camp a troll rushes up to you and says,

"Hey! You're just the {y.race} I am looking for! I know it's late but Hera needs to see you. She has a job for a {y.race}.
She said you might get some extra gold if you do it. I can't take you there, I have to fetch her some more wine, but you
know her tent don't you?" 
        """)
        d=int(input("\nPress 1 to nod yes, Press 0 to nod no"))
        if d==1:
            print(f"""
"Great! Saved me a lot of time." He says running off
        """)
        elif d==0:
            print(f""" 
"No, I'm a new recruit from Tiefling," you say
"Oh you stupid new recruits. Look for the blue commander's tent. You can't miss it. And don't tell the guards you're a
new recruit. If Hera finds out I sent her a newbie, she'll have my head for breakfast!" He says running off.
        """)
        print(f"""
You wander around a little trying to find Hera's tent. You overhear that she is the commander-in-charge of the mercenary 
group and the right hand of Revan nowadays. Again that name, Revan who in the nine realms is that? You see that the camp
is organised quite intelligently. The newbies guard the armory, so if attacked they can gear up quickly; but the armory 
is in the center of the camp. The newbies surround the camp in a crescent. The entrance and exit for the camp is 
situated by the lake, to prevent any invading armies. Though you were able to enter the camp from there, so maybe not 
the best judgement. The enitre camp is arranged in a crescent with the smaller crescent of the new recruits inside it. 
The larger crescent has a kitchen, a trainging ground and quarter for the senior members of the group. You found Hera's
tent just facing opposite to the "armory" tent. There has to be something important in there. You wouldn't risk the 
commander's life putting her in front of the armory. As you enter the tent, you find Hera sipping wine. 

"The troll sent me", you say remembering your war years. You immediately stand at attention.

"At ease," says Hera. "Do you know why we burnt down the inn, instead of killing that bastard in the inn itself?"

You nod no, trying to speak as little as possible hoping no one finds out you're actually alive.

"We had to steal a very important saphire from the bank in the town. The inn is owned by the same person who owns the 
bank. When the inn burnt, he diverted most of his men to salvage whatever they could from the inn. Quite useless, as greek
fire burns through everything. And while the bank was unprotected we robbed it."

You nod yes, this makes sense. The strategy was a classic diversion. But why were you targeted???

"Your job now", she continued "is to transport the artifact to Revan himself. The saphire was cursed by an ancient warlock 
from the old country to bring the cause of Revan's death. Now if I send you on such a mission then I need your trust. You
need to take this saphire to Feca of Tiefling. He knows how to crush cursed stones into powder, and destroy them. You will
be given 7000 gold pieces upon the completion of this mission. 350 now and the rest later. Pick it up from the armory."

You go to the armory and pick up the saphire and the gold.

""")
        if (y.stealth >= 550 and y.stealth <=600) :
            print(f"""
After you pick up the saphire you leave the camp. You continue down the path to meet Feca in Tiefling.

There are some things he has to answer for...

""")
            y.hp += 50
            y.stealth += 50
            y.str += 50
        else:
            print(f"""
After you pick up the artifact you walk straight to get out of the camp. But you see him. The {y.race} who was bathing
has come back. He got new armor somehow. The entire camp is facing the entrance to the armory. Fighting head on is stupid.
Before you cane figure an escape, 10 of the newbies charge. You fight them off with near ease, they've just been woken up 
that there is an intruder in the armory. They're sleep deprived and not at all battle hardened. But as you finish of 
those 10, 10 more attack, with more coming up behind them. You can't fight this entire army alone, it isn't possible. 
And definitely not in this setting where you are pinned down by the oncoming swarm. Wait! The armory is right behind you.
Maybe you can use something in there. 

Inside you find a barrel of greek fire. 
""")
            y.hp -= 100
            y.str -= 50
            d=int(input("Do you use greek fire? press 1 for yes and 0 for no"))
            if d== 1 :
                print(f"""
Yes! Greek fire is indestructable, it can catch anything on fire, be it metal or clothes. You dip a spare piece of wood 
into it, light it and throw it onto the incoming army. As they burn, you set up a rudimentary bomb using gunpowder and 
greek fire. However for the plan to work, you need to draw as many soldiers as possible into the armory tent.

You quickly position yourself at the exit and prepare to lure as many possible enemies in as possible. 

""")
                if y.race == "Human" :
                    print(f"""
The enemies are lured into your trap and you leave just as the bomb explodes, igniting greek fire and spraying it all
over the camp. Because of the explosion, the entire camp is in complete disarray. Many men are dead. There is 
confusion all around, similar to what happened at the inn. You smile to yourself. Tonight was good... 
As you walk down your path you see the sun rise. A good omen, but a signal that a lot of time has passed. 
You continue down the path to meet Feca in Tiefling. 

There are some things he has to answer for...
""")
                else:
                    print(f"""
The enemies are lured into your trap and you leave just as the bomb explodes, igniting greek fire and spraying it all 
over the camp. However, you are late by barely a second and your armor is caught on fire. You quickly run out of the 
camp lighting everything on fire. Once you have caused more chaos, you run to the lake to douse the fire. The fire 
douses out, but you have suffered some burns. Luckily as you were in the army, you know how to take care of them. But 
you are weakened for your journey. On a positive note, because of the explosion, the entire camp is in complete disarray.
Many men are dead. There is confusion all around, similar to what happened at the inn. You smile to yourself. 

Tonight was good...

As you walk down your path you see the sun rise. A good omen, but a signal that a lot of time has passed. 
You continue down the path to meet Feca in Tiefling.


There are some things he has to answer for...
""")
                    y.hp -= 50
            if d==0:
                print(f"""
ALAS great warrior. The enemies are too many, and your strength too little. As you continue to fight your enemies, 
someone stabs you in the back. Almost on cue you are cut in the stomach and the neck. You are then left for dead. 
You never found out why they were out to kill you. 

You slowly give in to the Eternal Slumber, the warrior spirit still fighting...

                            GAME OVER
""")
    elif d1 == 0:
        print(f"""
Digusted by these men you attack the entire camp head on! You were in the war you can take on these lumps of clay. You
catch the camp by surprise and kill all the guards who are awake. The rest still sleep. It is only you who is awake.
""")
        if y.str<500:
            print(f"""
Or so you thought. Men awoke in the commotion and are charging at you for battle. You fight and give one last stand but 
ALAS great warrior. The enemies are too many, and your strength too little. As you continue to fight your enemies, 
someone stabs you in the back. Almost on cue you are cut in the stomach and the neck. You are then left for dead. You 
never found out why they were out to kill you. 

You slowly give in to the Eternal Slumber, the warrior spirit still fighting...

                            GAME OVER
""")
        elif y.str>=500 and y.str < 550:
            print(f"""
Or so you thought. Men awoke in the commotion and are charging at you for battle. You fight and give one last stand. You
fight left and right. A sort of blood lust takes over you. You take down tens or hundreds of men with their bodies piling
up around you. You take some deep cuts, but it is almost like the warrior goddess has blessed you. Soon enough the 
mercenaries are scared of facing you and they run away. You finally calm down enough to walk through the near deserted
camp. You reach the armory and find a saphire just carelessly sitting there. It seems to call to you. You pick it up and
decide to keep it. After you pick up the saphire you leave the camp. You continue down the path to meet Feca in Tiefling. 

There are some things he has to answer for...
""")
            y.hp -= 100
        elif y.str>=600:
            print(f"""
Or so you thought. Men awoke in the commotion and are charging at you for battle. You fight and give one last stand. You 
fight left and right. A sort of blood lust takes over you. You take down tens or hundreds of men with their bodies piling
up around you. It is almost like the warrior goddess has blessed you. This thought gives you more strength that anything. 
Soon enough the mercenaries are scared of facing you and they run away. You finally calm down enough to walk through the
near deserted camp. You reach the armory and find a saphire just carelessly sitting there. It seems to call to you. You 
pick it up and decide to keep it. After you pick up the saphire you leave the camp. 
You continue down the path to meet Feca in Tiefling. 

There are some things he has to answer for...
""")
        y.hp += 50
        y.str += 50
        y.stealth += 50
    else:
        print(f"""Please enter a correct value""")
def lvl3():
    print(f'''You arrive at Tiefling village, exhausted from spending days on the road. You decide the best place to
start the investigation would be the village tavern. After getting a much needed drink, you start asking around about
Feca.When you ask the man behind the counter, he points towards the half naked bearded man outside the bar.’That’s him
right there’.You had heard stories of him being a drunk loudmouth, but actually seeing him like that was rather
hilarious. Do you invite him for another round or use a more direct method to find out what he knows…
''')
def lvl3_c_ye():
    print(f'''You walk up to him, he immediately shouts “Th-There’s my drinking buddy!What say you buy me another round
to old times eh pal”.He must be rather desperate if he made you, a complete stranger is buddy. “Sure Feca, lets go get 
you a drink”. You get two pints of mead and slowly watch him get drunk. For a rather tiny man he sure could hold his
drink. You were worried you’d run out of cash before you got anything out of him. Then, he suddenly says,’Say what,you 
look trustworthy. Ya wanna share some secrets,I’ll go first. Ya know that inn that was raided a few days ago, I supplied
them with the weapons .It was a proper massacre I hear,all thanks to my weapons.Their Ruthorham weapons looked like toys
in front of my creations I tell ya!’

“So they were from Ruthorham?” you ask

“Where else would they be from, it’s where their dumb kind lurks all the time!Hey now, it’s your turn.Tell me a secret!”

“Ah-well that’s easy, I’m gay Feca”

“You’re WHAT! Ge-Get out of my sight.You and your kind are truly the scum of the Earth,worse than them Ruthorham folks 
yeah!”

“Ah well, as you say Feca, nice meeting you”

“Don’t talk to me!”

So the rumors of him being bigoted were true too. Doesn't matter though, he told you exactly where to go.After resting 
a little more you set out for Ruthorham the next morning
''')
def lvl3_c_nu():
    print(f'''You walk up to him, he immediately shouts “Th-There’s my drinking buddy!What say you buy me another round
to old times eh pal”.He must be rather desperate if he made you, a complete stranger is buddy. “Sure Feca, lets go get 
you a drink”. You get two pints of mead and slowly watch him get drunk. For a rather tiny man he sure could hold his 
drink. You were worried you’d run out of cash before you got anything out of him.Desperate for information, you ask him 
“So,what do you know about the inn that burned down a few days ago”.He looked at you suspiciously.

“No-Nothing! Why do you ask!Ya know what, you’re not my buddy!A buddy won’t ask incriminating questions like that.N-Now
get out before I call the guards!!”

You blew it, now he won’t tell you anything. There must be some other way to find out more about the attack. 
You head to his shop and notice the lights are out, maybe no one’s inside?You manage to break in through the back 
window.It’s pitch black, though you manage to light a lamp and look around. You find a fancy trunk with a huge padlock 
on it. Using your {weapon} you break it and find it’s full of gold from Ruthorham .That must mean his “clients” must be 
from Ruthorham, and that’s where you must go next. As you’re leaving you accidentally trip the lamp,and it lands 
directly on his mead collection. The fire spreads quickly and you manage to get out of there.

Guards and villagers alike quickly surround the burning building.
“Stop right there{y.race}! Explain Yourself!
''')
def lvl3_caught():
    print(f'''“Woah now, let’s all just calm down. That was nothing more than an accident, I’m sure we can find a
compromise here”. You throw a pouch of Ruthorham gold you took from the trunk.

“That pouch is more valuable than anything either of you own, let me go and it’s all yours”.

One of the guards slowly approaches the pouch and picks it up.

“By the Gods, it’s Ruthorham gold!”

The captain of the guards fires an arrow that whizzes past your ear.

“Thanks for the treasure scum!”

You need to think fast, take them head on or try and take them out one by one?
''')
def lvl3_brute():
    print(f'''You take out your {weapon} and charge at the guards. Seeing the berserker in front of them, the guards 
drop their weapons and flee. The captain orders his men back, and attacks you with the ones remaining. You cut through 
them with ease, until it’s just you and the captain.

“You monster!” Shouts the captain as he swings his sword at you wildly. You duck and strike him down.

As soon as the carnage is over, you head for Ruthorham without looking back. You know you can never return to Tiefling 
again.
''')
if y.str>=550:
    y.hp -= 50
elif y.str>=500:
    y.hp -= 100

def lvl3_run():
    print(f'''You use a smoke bomb and manage to disappear in the chaos. After climbing a nearby building, you use your
bow to snipe off the guards below looking for you below. One by one they fall in the darkness of the night. 
Once you cleared a path for yourself, you slowly descend and leave Tiefling village, knowing you can never return.
''')
def lvl3_brute_death():
    print(f'''You take out your {weapon} and charge at the guards, a brave gesture.But foolish.
They fire arrow after arrow till you drop dead in your tracks

Alas mighty hero! Your tale ends here....

''')
def lvl3_run_death():
    print(f'''You try to run away hoping to regroup and take the guards on later, but you’re hit on the head with 
a stone by a villager. Knocked out, the guards easily capture you and execute you!

Alas mighty hero! Your tale ends here....
''')
def lvl3_interrogate():
    print(f'''You walk up to him and grab him by the neck

“H-Hey let go of me!!” “Guards!Guards!!”

You quickly punch him in the face to silence him.You drag him to the back of the inn and tie him to the stable doors.

“Now Feca, These past few days have been rather unpleasant for me, no thanks to you.So don’t make me ask you twice.Who
bought the weapons for the mercenaries that attacked the inn on Dragontail Walk!”

“I-I don’t know what you’re talking about!! Me swears!”

You punch him in the stomach and draw put your {weapon}

“Do your worst! If I talk Hera will have my head!”

“If you don’t, Hera won’t get the chance to”

“Go to hell!”

This was taking too much time, you take out your knife and stab him in the gut. He screams and twitches.” All right 
All right!! It was a group from Ruthorham. They warned me not to talk, now make this stop!!”

“See, that was easy, now hold still”

You bandage him up and release him. “This never happened Feca, are we clear?”

“Y-Yes”

“Good”

With that out of the way, you now knew exactly where to go.After resting a little more you set out for Ruthorham the 
next morning
''')
def lvl3_interrogate_nu():
    print(f'''You walk up to him and grab him by the neck

“H-Hey let go of me!!” “Guards!Guards!!”

You quickly punch him in the face to silence him.You drag him to the back of the inn and tie him to the stable doors.

“Now Feca, These past few days have been rather unpleasant for me, no thanks to you.So don’t make me ask you twice.Who
bought the weapons for the mercenaries that attacked the inn on Dragontail Walk!”

“I-I don’t know what you’re talking about!! Me swears!”

You punch him in the stomach and draw put your {weapon}

“Do your worst! If I talk Hera will have my head!”

“If you don’t, Hera won’t get the chance to”

“Go to hell!”

This was taking too much time, you take out your knife and stab him in the gut. He screams and twitches.He goes limp,his
breathing is faint.You realise you messed up.

After releasing him you rush to the village doctor and tell him Feca was stabbed in a bar fight.The doctor says he’s 
unconscious but may survive

You blew it, now he won’t tell you anything even if he survives. There must be some other way to find out more about 
the attack. You head to his shop and notice the lights are out, maybe no one’s inside?You manage to break in through 
the back window.It’s pitch black, though you manage to light a lamp and look around. You find a fancy trunk with a huge 
padlock on it. Using your {weapon} you break it and find it’s full of gold from Ruthorham .That must mean 
his “clients” must be from Ruthorham, and that’s where you must go next. As you’re leaving you accidentally trip the 
lamp,and it lands directly on his mead collection. The fire spreads quickly and you manage to get out of there.

Guards and villagers alike quickly surround the burning building.
“Stop right there{y.race}! Explain Yourself!
''')
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
d1 = int(input())

if d1 == 1:
    lvl_2()
lvl3()
e1 = int(input(''))

if e1==1:
    if y.charisma:
        lvl3_c_ye()
    else:
        lvl3_c_nu()
        lvl3_caught()
        e2=int(input(''))
        if e2==1:
            if y.str>=500:
                lvl3_brute()
            else:
                lvl3_brute_death()
        elif e2==2:
            if y.charisma:
                lvl3_run()
            else:
                lvl3_run_death()
elif e1==2:
    if y.str>=500:
        lvl3_interrogate()
    else:
        lvl3_interrogate_nu()
        lvl3_caught()
        e2 = int(input(''))
        if e2 == 1:
            if y.str >= 500:
                lvl3_brute()
            else:
                lvl3_brute_death()
        elif e2 == 2:
            if y.charisma:
                lvl3_run()
            else:
                lvl3_run_death()
