class hotel:
    def __init__(self,id):
        self.__id=id
        self.__ownerid=0

    @property
    def hotelid(self):
        return self.__id

    @property
    def ownerid(self):
        return self.__ownerid

    @ownerid.setter
    def ownerid(self,id):
        self.__ownerid=id