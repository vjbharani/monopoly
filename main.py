import player as p
import board
import random
plr=[]
pos=[]

try:
    a= int(input("\nenter number of players"))
    for i in range(1,a+1):
        plr.append(p.player(i))
        plr[i-1].position=0
except:
    print("enter valid input")

b=board.board(plr)

for i in range(1,11):
    for j in plr:
        print("\nplayer",j.id,"press enter to roll dice")
        input()
        r = random.randrange(2, 12)
        pos=j.position
        pos+=r
        if pos >=38:
            pos -= 38
        j.position=pos
        print("dice move:", r, " player", j.id, "position:", pos)
        b.play(j, pos)

winner=plr[0]
for i in range(0,a):
    print("player:",plr[i].id,"ammount is:",plr[i].calammount())
    if i>0:
        if plr[i].ammount >winner.ammount:
            winner=plr[i]
print("winner is:player",winner.id)





