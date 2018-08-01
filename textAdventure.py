import os, sys

inventory = []
classChoice = []
classStat = {'str': [], 'int': [], 'cou': [], 'loy': [], 'luc': []}
diaChoices = []

print()
def printTitle(leftWidth, rightWidth):
    print('SCHOOL LIFE'.center(leftWidth + rightWidth, '-'))
    
printTitle(40, 12)
print()
        
while True:
    classDecision = input('You are the new kid in school. Having moved to the big \
city from the rural suburb of God Knows Where, you are desperate to make friends but have \
yet to settle on "your group," the group and label you would like most to \
be associated with for the foreseeable future. Through sheer hours of \
consideration you have narrowed down your options to 3: the jocks, \
the nerds, and the outcasts —— which will you choose? >>> ')
    print()

    if classDecision.lower() == 'the jocks' or classDecision.lower() == 'jocks':
        finalAnswerJock = input('The Jocks are a hardy breed, able to take hits on the field \
just as well as they might take a hit to the face. They are the quintessential "bro," \
true to their bros, with a sense of loyalty that is rivaled by no other. They are, however, \
often considered meatheads, knowing little, distracted by much — they are average performers \
in school. Would you like to adopt these characteristics? >>> ')
        print()
        if finalAnswerJock.lower() == 'yes':
            classStat['str'].append(5)
            classStat['int'].append(1)
            classStat['cou'].append(3)
            classStat['loy'].append(4)
            classStat['luc'].append(3)
            classChoice.append('jock')
            print('And from there our story begins...')
            break
        else:
            print('Allow me to recount what I told you thus far...')
            print()
            
    elif classDecision.lower() == 'the nerds' or classDecision.lower() == 'nerds':
        finalAnswerNerd = input('The Nerds are beacons of intellect and \
academic achievement. They stand tall in the face of complicated equations, \
combining fiercely the mysteries of chemical equations, all whilst deftly \
keeping their glasses firmly atop their nose. Incredible intellect brings \
with it flaws, however. They are often considered weak physically and \
impressively timid. They are targets of bullying, choosing often to \
avoid the conflicts around them for the problems present in their schoolwork. \
Would you like to adopt these characteristics? >>> ')
        print()
        if finalAnswerNerd.lower() == 'yes':
            classStat['str'].append(1)
            classStat['int'].append(5)
            classStat['cou'].append(2)
            classStat['loy'].append(3)
            classStat['luc'].append(2)
            classChoice.append('nerd')
            print('And from there our story begins...')
            break
        else:
            print('Allow me to recount what I told you thus far...')
            print()

    elif classDecision.lower() == 'the outcasts' or classDecision.lower() == 'outcasts':
        finalAnswerOutcast = input('The Outcasts drew the short straw. Considered the "troubled kids" \
they believe themselves to be the coins in the couch cushions, forgotten by everyone, left to fend \
for themselves by adults and their peers alike. It has created a mistrust, even with regards to those \
closest to them, be it their family or their friends, but what they lack in luck and loyalty, they make up for \
in courage; blend in they don\'t, but stand up for what they believe in —— they always will. Would \
you like to adopt these characteristics? >>> ')
        print()
        if finalAnswerOutcast.lower() == 'yes':
            classStat['str'].append(3)
            classStat['int'].append(3)
            classStat['cou'].append(4)
            classStat['loy'].append(2)
            classStat['luc'].append(1)
            classChoice.append('outcast')
            print('And from there our story begins...')
            break
        else:
            print('Allow me to recount what I told you thus far...')
            print()

    elif classDecision.lower() == 'none' or classDecision.lower() == 'nothing':
        finalAnswerIndiv = input('The role of the Individual is important, but often left \
unfulfilled. Few find the courage and strength to face high school alone, and fewer still \
manage to do it successfully. It\'s easy to blend in when the going gets tough, but \
the individual weathers it all, blending in wherever they choose, making friends \
despite group, despite social standing. Would you like to adopt these characteristics? >>> ')
        print()
        if finalAnswerIndiv.lower() == 'yes':
            classStat['str'].append(3)
            classStat['int'].append(3)
            classStat['cou'].append(5)
            classStat['loy'].append(3)
            classStat['luc'].append(3)
            classChoice.append('individual')
            print('And from there our story begins...')
            break
        else:
            print('Allow me to recount what I told you thus far...')
            print()
    else:
        print('Allow me to recount what I told you thus far...')
        print()


print()
if classChoice[0] == 'jock':
        print('A couple of weeks pass. Your free time is spent in and out of \
practice and you feel as though the entire student body worships the halls you walk down. \
Your classwork becomes a series of answers: "I forgot." "Can I turn it in later?" \
And "I\'ll have to ask Coach if he\'ll let me come late." But your grades never slip. \
Practice is Hell, games mean the world, and scholarships are on the line —— your teachers \
understand that.')
        print()
        print('Out of all of the other jocks, there are two you connect well enough with to \
actually call friends: Brent, a catcher for the baseball team, and Douglas, a second-string \
linebacker. Brent is deceptively intelligent, but would never quite show it and Douglas \
is rather quiet. The both of them seem strangely different from the others, but love \
the sports they play. Type "continue" >>> ')
        while True:
            jockContinue = input()
            if jockContinue.lower() == 'continue':
                break
            else:
                print('Type "continue" to further the story. >>> ')

if classChoice[0] == 'nerd':
        print('A couple of weeks pass. Your free time is spent in study hall and \
you feel as though the entire student body doesn\'t even realize you\'re alive. But the \
loneliness inherent in being studious over social only helps fuel your pursuit of good grades.')
        print()
        print('Out of all of the other nerds, there is only one who seems \
willing to accept the hand of friendship — Trevor — and, in a seeming drought of human companionship, \
you take what you can get. He\'s less like the others, less reserved, less defensive, and upon \
getting to know him, he reminds you of yourself. He certainly isn\'t the highest performing \
nerd you\'ve come to know, but he\'s easily the one that feels the most comfortable communicating \
with others. Type "continue" >>> ')
        while True:
            nerdContinue = input()
            if nerdContinue.lower() == 'continue':
                break
            else:
                print('Type "continue" to further the story. >>> ')

if classChoice[0] == 'outcast':
        print('A couple of weeks pass. Your free time is spent under the bleachers, away \
from all of the school clubs and pep rallies. You could do without all of this "school spirit," \
all of the people cheering on the privileged, pathetic sports ogres for running a ball and \
that\'s it.')
        print()
        print('The outcast life is a tough one. The people you\'d probably \
associate with are natural loners and largely unrelatable to an outsider. But you understand \
who they are, what they\'re going through to an extent that no one else really does and for that, \
if nothing else, you are at least a part of the subset you sought out to join. Type "continue" >>> ')
        while True:
            outcastContinue = input()
            if outcastContinue.lower() == 'continue':
                break
            else:
                print('Type "continue" to further the story. >>> ')

if classChoice[0] == 'individual':
        print('A couple of weeks pass. Your free time is spent doing as you please. You study, \
you slack off — you\'re young, you have your life ahead of you and you enjoy life the way you see fit. \
None of the core groups claim you as "one of their own," but you manage to make friends with people from \
different backgrounds, with different interests despite it.')
        print()
        print('You make friends with a girl from the gamer group named Trish and a guy from the jocks named \
Nathan. You manage, somehow, to act as a bridge between them and create a friendship where one wasn\'t, and \
perhaps, never would have been before. Type "continue" >>> ')
        while True:
            indvContinue = input()
            if indvContinue.lower() == 'continue':
                break
            else:
                print('Type "continue" to further the story. >>> ')

print()
print('One day, you\'re walking out to your car after school and you realize you forgot a book in your locker \
that you desperately need to study with for a test coming up tomorrow. You walk back inside to largely empty hallways. \
Students have gone home or are mingling out front and the teachers are in meetings or head-down into their gradebooks \
so that they can wrap it up and go home themselves. You stand at your locker, pull the book out you need, and as you \
go to close it, you see something out of the corner of your eye.')
print()
print('Claudia, a girl you\'ve had a couple of classes with, runs past you down the hallway. You hear her sniffling \
and see her wiping her face — it looks like she\'s been crying. You look back to where she came from and there\'s \
a teacher in the doorway to his classroom, watching her as she rushes down the hall. It\'s Mr. Blackwell, a sophomore \
mathematics instructor, which is weird, considering you and Claudia are seniors. He looks mad. He grabs the door, \
but before he closes it, notices you looking toward him. He scowls, shuts the door, a little harder than \
normal and then the hall is silent again. Type "continue" >>> ')
while True:
    goOn = input()
    if goOn.lower() == 'continue':
        break
    else:
        print('Type "continue" to further the story. >>> ')

print()
print('You close your locker and begin back down the hall. Claudia steps out of the bathroom doorway \
and bumps into you. You drop your book and both reach down to grab it. She looks at you, says "Sorry," \
to which you respond: ')
print()
print('(a): It\'s okay. I should have looked where I was going.')
print('(b): You should really watch where you\'re going next time.')
print('(c): (You shrug your shoulders, grab the book, turn around and leave.)')
print('>>> ')
while True:
    choiceOne = input()
    if choiceOne.lower() == 'a':
        diaChoices.append('a')
        print('She smiles a soft, almost sad smile and says, "I really should get going. Sorry again." \
She walks back down the hallway and out the front door. You walk after her, you want to ask her about \
what happened, but when you exit the building, she\'s gone. You head to your car, crank it up, and \
go home.')
        break
    elif choiceOne.lower() == 'b':
        diaChoices.append('b')
        print('She apologizes again. Her eyes glisten as she pushes past you, down the hallway and \
out the front door. It WAS her fault, after all. I get it, she\'s upset, but she needs to watch \
where she\'s going. You put the book into your bag, walk out the door, down to your car and leave.')
        break
    elif choiceOne.lower() == 'c':
        diaChoices.append('c')
        print('You proceed out the front door, down the steps and across the parking lot, and out \
toward your car. You aren\'t sure what she thought about your sudden departure, but...oh well, I guess.')
        break
    else:
        print('Please choose letter "a", "b", or "c". >>> ')

print()
print('Type "continue" >>> ')
while True:
    goOn = input()
    if goOn.lower() == 'continue':
        break
    else:
        print('Type "continue" to further the story. >>> ')

print()
print('The next day, you get to school early. It\'s hot, you ate something before bed you shouldn\'t \
have —— you don\'t know for sure, but for whatever reason, you couldn\'t sleep.')
print()
if classChoice[0] == 'jock':
    print('You can\'t, for whatever reason, seem to get Claudia off of your mind. She\'s never seemed \
like the type to cry and, while you\'ve never known her very well, you can\'t help but to feel like \
you should look into what happened. You open the front door, only to be greeted by Brent, standing \
there, surrounded by a couple of girls. You catch his eye, he waves, and approaches. He asks if you heard \
that Patrica was having a party this weekend and oh yeah! He forgot. Coach needs to see you in his office. \
Brent walks away, but you remember that earlier in the week you promised to meet with a group from your \
class about a project. This morning was the only time that worked and the project is due tomorrow. You: ')
    print()
    print('(a): Hurry down to the coach\'s office. Your group has three others, they\'ll manage without you.')
    print('(b): Head to the library. Coach teaches Government Econ., you\'ll see him then – I\'m sure he\'ll understand.')
    print('(c): Blow them both off. Claudia usually hangs out in the courtyard before your first period English class and \
maybe you can talk to her there.')
    print('>>> ')
    while True:
        choiceTwo = input()
        if choiceTwo.lower() == 'a':
            diaChoices.append('a')
            print('Coach\'s office is down the junior hallway. You hoist your bookbag higher up on your shoulder and \
saunter down toward it. A year\'s difference in high school means the WORLD and the juniors are so much smaller. It\'s \
always worth the opportunity to show off a little and show them who\'s taller.')
            print()
            print('You knock and walk into Coach\'s office, who holds up a finger while he talks on the phone. He\'s \
rounder than he probably should be, older looking than he probably is, but he\'s led a couple of the school teams \
to championships so you\'d never think less of him for it. Before you sit down, he holds out a sheet of paper \
for you to take. It\'s the grade for the makeup test you took when you were sick the other day. You look down, you \
made a C-, he gives you a thumbs up, and shoos you out —— you barely had the time to take your bag off of your shoulder \
before you haul back up upon it.')
            print()
            print('Maybe you should have met with your group. Maybe you should have spoken to Claudia. You think \
for a second how much you hate how easily you drop things for Coach, but the project will be fine, hopefully, and \
you\'ll have the chance later to figure out more about what was going on with Claudia. Maybe. Type "continue" >>> ')
            while True:
                goOn = input()
                if goOn.lower() == 'continue':
                    break
                else:
                    print('Type "continue" to further the story. >>> ')
                    
        elif choiceTwo.lower() == 'b':
            diaChoices.append('b')
            print('You hurry down to the library. Your group is working at one of the long tables, well, one of \
your group members anyway. Bernice is sitting there alone, frantically typing away something on her phone.')
            print()
            print('You lean over, say, "Hey," and she jumps, but smiles when she looks up to see it was you. She tells you \
that the other two members couldn\'t make it. Jon was "sick" while Heather said the volleyball coach needed to see her and \
she wouldn\'t be able to make it. Ha-ha. You sit down and hack away at what is left to get done. You don\'t feel like you \
contribute much, but Bernice assures you that without your help, the project wouldn\'t have gotten done.')
            print()
            print('You leave the library and feel almost proud that you came here first. Bernice is nice, but kind of a \
pushover and would have easily taken the blame if this work hadn\'t have gotten done. You feel good that she didn\'t have \
to do that and HOPEFULLY, you\'ll manage to get a good grade. Type "continue" >>> ')
            while True:
                goOn = input()
                if goOn.lower() == 'continue':
                    break
                else:
                    print('Type "continue" to further the story. >>> ')
                    
        elif choiceTwo.lower() == 'c':
            diaChoices.append('c')
            print('The courtyard is empty, save for Claudia on a bench, silently scrolling through her phone. You walk up to her, \
she looks up at you and you say sorry for what happened yesterday. She just stares at you, eyes locked on yours, but \
in a way, almost, as if she isn\'t looking at you — but through you, thinking, not even paying attention to the fact that you are \
even here. You: ')

            print()
            print('(a): Wave your hand a few inches from her face.')
            print('(b): Snap your fingers.')
            print('(c): Lean down in her ear and shout, "HEY!!" literally as loud as you can.')
            print('>>> ')

            while True:
                choiceTwoAlt = input()
                if choiceTwoAlt.lower() == 'a' or choiceTwoAlt.lower() == 'b' or choiceTwoAlt.lower() == 'c':
                    break
                else:
                    print('Please choose letter "a", "b", or "c". >>> ')

            print()
            print('She jumps. Her eyes focus back in on yours and she says, "Sorry. What did you say? I think \
I zoned out there for a minute." You say sorry again, "that...well" — you stumble over your words. She looks down \
and before you have the chance to say anything else she says, "It\'s fine." You want to ask her more about what \
happened, about Mr. Blackwell and what he did to make her cry, but before you\'re able to do so, the bell rings. \
Claudia stands up, smiles softly and brushes past you inside and onto her first class.')
            print()
            print('On your way to class, you worry that you maybe shouldn\'t have talked to her yet, that it may \
have been better if you\'d been more prepared. But oh well — what\'s done is done; hopefully there\'s another \
chance later on. Type "continue" >>>')
            while True:
                goOn = input()
                if goOn.lower() == 'continue':
                    break
                else:
                    print('Type "continue" to further the story. >>> ')

        else:
            print('Please choose letter "a", "b", or "c". >>> ')

if classChoice[0] == 'nerd':
    print('You can\'t, for whatever reason, seem to get Claudia off of your mind. She\'s never seemed \
like the type to cry and, while you\'ve never known her very well, you can\'t help but to feel like \
you should look into what happened. You open the front door and walk over to your usual spot by the \
window. You open your bag, take out a book, and start reading when Grace, a girl in your third \
period mathematics class walks up to you. She\'s cute, blonde, with a small gap inbetween her two front \
teeth. You kind of cringe when she smiles, but it\'s a girl and you\'re you —— beggars can\'t be \
choosers. If she were actually into you that is...')
    print()
    print('She hands you a note and walks away. Your heart skips a beat —— then you notice the brutish \
script scrawled across the front of the folded piece of paper: "From Trevor"')
    print()
    print('—_—\'')
    print()
    print('You open the note: "Mr. Greenbee wants to see us at lunch for a robotics meeting. "Bee" there." For \
the love of God, why can\'t he just send a text like a normal person? But you remember —— Thomas, a \
friend, more or less, promised to return your copy of "Ninja Fight 2: The Fightening" at lunch \
before he went on vacation. You can\'t remember exactly, but you\'re pretty sure he\'s planning on leaving \
directly after lunch and you won\'t see him before then. This weekend was meant for ninja fighting, but that \
won\'t happen if you don\'t meet up with Thomas. You:')
    print()
    print('(a): Go to Mr. Greenbee\'s during lunch. Ninjas can wait, Mr. Greenbee can\'t. He\'s kind of a hardass.')
    print('(b): Blow off robotics. You\'ve been done with yours for weeks and you want nothing less than the inevitable boredom of no ninjas.')
    print('(c): Do neither. You and Claudia have the same lunch and maybe you can talk to her there.')
    print('>>> ')
    while True:
        choiceTwo = input()
        if choiceTwo.lower() == 'a':
            diaChoices.append('a')
            print(''
