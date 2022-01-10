import random


def game(you, comp):
    if you == comp:
        # return None
        print("Game tie")
    elif comp == 'p':
        if you == 's':
            # return True
            print("You win")
        elif you == 'r':
            # return False
            print("comp won")
    elif comp == 'r':
        if you == 's':
            # return False
            print("com won")
        elif you == 'p':
            # return True
            print("yo won")
    elif comp == 's':
        if you == 'p':
            # return False
            print("comp won ")
        elif you == 'r':
            # return True
            print("you won ")


randnum = random.randint(1, 3)

if randnum == 1:
    comp = "r"
elif randnum == 2:
    comp = 'p'
elif randnum == 3:
    comp = 's'

# print(randnum,comp)
print('comp choose Rock(r) , Paper(p), sizer(s)')
you = input('you choose Rock(r) , Paper(p), sizer(s)??').upper().lower()

print(you)
print(f"Comp choose {comp} {randnum}")
a = game(you, comp)

# if a==True:
#     print('you win')
# elif a==None:
#     print('game tie ')
# elif a==False:
#     ('you lose comp win ')
