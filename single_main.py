#from Randomizer import *
#from Player import *
#import time
#import os

#myRandom = Randomizer()

#def cls():
#    os.system('cls' if os.name=='nt' else 'clear')

#def Make_Sequential_Draw():
#    draw = Draw()
#    draw.n_1 = myRandom.Get_10()
#    draw.n_2 = myRandom.Get_10()
#    draw.n_3 = myRandom.Get_10()
#    draw.n_4 = myRandom.Get_10()
#    draw.n_5 = myRandom.Get_10()
#    draw.n_6 = myRandom.Get_10()
#    draw.symbol = myRandom.Get_12()
#    return draw

#def Make_Simultanious_Draw():
#    return myRandom.Get_SIM_Draw()

##Sequential Random Player
#def Make_Random_Player_Sequential():
#    draws =[]
#    for x in range(0, 12):
#        draws.append(Make_Sequential_Draw())
#    return draws

##Alle cijfers voor eerste 10 + 2 duplicaten
#def Make_FirstNumber_Player_Sequential():
#    draws =[]
#    for x in range(0, 10):
#        d = Make_Sequential_Draw()
#        d.n_1 = x
#        draws.append(d)

#    for x in range(0, 2):
#        draws.append(Make_Sequential_Draw())

#    return draws

##Sequential Symbol Player
#def Make_Symbol_Player_Sequential():
#    draws =[]
#    for x in range(0, 12):
#        d = Make_Sequential_Draw()
#        d.symbol = x
#        draws.append(d)

#    return draws

##Same number all symbol player
#def Make_SameNumber_Symbol_Player_Sequential():
#    draws = Make_Symbol_Player_Sequential()
#    for x in draws:
#        x.n_1 = 1
#        x.n_2 = 1
#        x.n_3 = 1
#        x.n_4 = 1
#        x.n_5 = 1
#        x.n_6 = 1

#    return draws

##Lonely Gambling Soldier....
#def Make_OneDraw_Player_Sequential():
#    draws = []
#    draws.append(Make_Sequential_Draw())
#    return draws


#def Simulate(n, players, display=False):

#    all_status=""
#    start_time = time.time()
#    progress_time = start_time
#    for x in range(0, n):

#        Draw_SEQ = Make_Sequential_Draw()
#        Draw_SIM = Make_Simultanious_Draw()

#        all_status = ""
#        for p in players:
#            p.Analyze(seq_draw = Draw_SEQ, sim_draw=Draw_SIM)
#            all_status += p.get_status()

#        elapsed_time = time.time() - progress_time
#        if elapsed_time >= 15 or x == 0:
#            if display:
#                cls()
#                print(all_status)
#                total_elapsed = int(time.time() - start_time)
#                total_elapsed_str = '{:02d}:{:02d}:{:02d}'.format(total_elapsed // 3600, (total_elapsed % 3600 // 60), total_elapsed % 60)
#                print("PROGRESS: {0} / {1}".format(x+1, n))
#                print("Time Elapsed: {0} (refresh every 15 seconds)".format(total_elapsed_str))

#            progress_time = time.time()
            
#    cls()
#    print("FINAL RESULT") 
#    print(all_status)
#    total_elapsed = int(time.time() - start_time)
#    total_elapsed_str = '{:02d}:{:02d}:{:02d}'.format(total_elapsed // 3600, (total_elapsed % 3600 // 60), total_elapsed % 60)
#    print("PROGRESS: {0} / {1}".format(x+1, n))
#    print("Time Elapsed: {0} (refresh every 15 seconds)".format(total_elapsed_str))

#if __name__ == "__main__":

#    players = []

#    players.append(Player(name="Random Player", draws=Make_Random_Player_Sequential()))
#    players.append(Player(name="First Number Player", draws=Make_FirstNumber_Player_Sequential()))
#    players.append(Player(name="Symbol Player", draws=Make_Symbol_Player_Sequential()))
#    players.append(Player(name="SNAS Player", draws=Make_SameNumber_Symbol_Player_Sequential()))
#    players.append(Player(name="One Draw Player", draws=Make_OneDraw_Player_Sequential()))

#    for p in players:
#        print(p)

#    print("n° of players: ", len(players))

#    while True:
#        n = None
#        try:
#            n = int(input("How many simulations? (press 0 to exit) \n --> "))
#            if n <= 0:
#                break               
#        except:
#            print("Use integers if you don't mind ( >0 )")

#        Simulate(n, players, True) #Turn True for continious display
