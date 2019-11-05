import hotel as H
import tkinter as tk
class board:
    def __init__(self,playerList):
        self.__playerList=playerList
        self.__hotel=[2,9,19,32]
        self.__treasure=[33,22,12,3]
        self.__jail=[35,26,17,6]
        self.hotl=[]
        for i in self.__hotel:
            self.hotl.append(H.hotel(i))



    def play(self,player,pos):
        for i in self.hotl:
            if i.hotelid == pos:
                if i.ownerid == 0:
                    player.hotelid = pos
                    curammount=player.ammount
                    curammount=curammount-200
                    player.ammount=curammount
                    i.ownerid=player.id
                    print("owns hotel ",pos," now ,amount remaining is:",curammount)

                else:
                    for j in self.__playerList:
                        if i.ownerid==j.id and j.id != player.id:
                            curammount=j.ammount
                            curammount=curammount+50
                            j.ammount=curammount
                            curammount2=player.ammount
                            curammount2=curammount2-50
                            player.ammount=curammount2
                            print("has landed in a hotel owned by player ", j.id,",amount 50 has been deducted, amount remaining is:",curammount2)
            else:
                pass

        if pos in self.__treasure:
            curammount = player.ammount
            curammount =curammount+ 200
            player.ammount = curammount
            print("has found treasure, amount remaining is:",curammount)
        if pos in self.__jail:
            curammount = player.ammount
            curammount =curammount- 150
            player.ammount = curammount
            print("landed in jail, amount remaining is:",curammount)
        else:
            pass








