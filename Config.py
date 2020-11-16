from Randomizer import Randomizer
from Draw import *

class Config(object):
    def __init__(self, display=False):
        self.random = Randomizer(display)

    def Make_Sequential_Draw(self):
        draw = Draw()
        draw.n_1 = self.random.Get_10()
        draw.n_2 = self.random.Get_10()
        draw.n_3 = self.random.Get_10()
        draw.n_4 = self.random.Get_10()
        draw.n_5 = self.random.Get_10()
        draw.n_6 = self.random.Get_10()
        draw.symbol = self.random.Get_12()
        return draw
    
    def Make_Simultanious_Draw(self):
        return self.random.Get_SIM_Draw()

    #Sequential Random Player
    def Make_Random_Player_Sequential(self):
        draws =[]
        for x in range(0, 12):
            draws.append(self.Make_Sequential_Draw())
        return draws

    #Alle cijfers voor eerste 10 + 2 duplicaten
    def Make_FirstNumber_Player_Sequential(self):
        draws =[]
        for x in range(0, 10):
            d = self.Make_Sequential_Draw()
            d.n_1 = x
            draws.append(d)

        for x in range(0, 2):
            draws.append(self.Make_Sequential_Draw())

        return draws

    #Sequential Symbol Player
    def Make_Symbol_Player_Sequential(self):
        draws =[]
        for x in range(0, 12):
            d = self.Make_Sequential_Draw()
            d.symbol = x
            draws.append(d)

        return draws

    #Same number all symbol player
    def Make_SameNumber_Symbol_Player_Sequential(self):
        draws = self.Make_Symbol_Player_Sequential()
        for x in draws:
            x.n_1 = 1
            x.n_2 = 1
            x.n_3 = 1
            x.n_4 = 1
            x.n_5 = 1
            x.n_6 = 1

        return draws

    #Lonely Gambling Soldier....
    def Make_OneDraw_Player_Sequential(self):
        draws = []
        draws.append(self.Make_Sequential_Draw())
        return draws