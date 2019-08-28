
class player:
    def __init__(self,id):
        self.__id=id
        self.__ammount=1000
        self.__position=0
        self.__hotelid=[]

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id=id
    @property
    def position(self):
        return self.__position

    @property
    def ammount(self):
        return self.__ammount

    @ammount.setter
    def ammount(self, ammount):
        self.__ammount = ammount

    @position.setter
    def position(self,pos):
        self.__position=pos

    def chances(self):
        self._chances +=1

    @property
    def hotelid(self):
        return self.__hotelid


    @hotelid.setter
    def hotelid(self,id):
        self.__hotelid.append(id)

    def calammount(self):
        for i in self.__hotelid:
            self.__ammount+=200
        return self.__ammount





