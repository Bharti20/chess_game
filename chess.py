class spot:
    def __init__(self,hight,width):
        self.hight_of_spot = hight
        self.width_of_spot = width
    def spotHight(self):
        return self.hight_of_spot
    
    def spotWidth(self):
        return self.hight_of_spot


class piece:
    def __init__(self, Pawn, King,Queen,Rook,Knight,Bishop):
        