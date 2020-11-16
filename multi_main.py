from Player import Player
import time
import os

from Simulation import Simulation
import multiprocessing as mp

from Config import Config

if __name__ == "__main__":

    mp.freeze_support()
    #myConfig = Config(display=True)

    #players = []

    #players.append(Player(name="Random Player", draws=myConfig.Make_Random_Player_Sequential()))
    #players.append(Player(name="First Number Player", draws=myConfig.Make_FirstNumber_Player_Sequential()))
    #players.append(Player(name="Symbol Player", draws=myConfig.Make_Symbol_Player_Sequential()))
    #players.append(Player(name="SNAS Player", draws=myConfig.Make_SameNumber_Symbol_Player_Sequential()))
    #players.append(Player(name="One Draw Player", draws=myConfig.Make_OneDraw_Player_Sequential()))

    #for p in players:   
    #    print(p)

    #print("n° of players: ", len(players))

    while True:
        n = None
        try:
            n = int(input("How many simulations? (press 0 to exit) \n --> "))
            if n <= 0:
                break
            else:
                print("Starting Simulations -> ", n)
                mySims = Simulation(n=n)
                mySims.Run()              
        except Exception as err:
            exception_type = type(err).__name__
            print(exception_type)
            print(err)

    print("Finished")

