import multiprocessing as mp
from multiprocessing.managers import SyncManager, NamespaceProxy
import signal
import time
import psutil
from Config import Config
from Progression import Progression
import os
from Player import Player


class MyManager(SyncManager): pass

class ConfigProxy(NamespaceProxy):
    # We need to expose the same __dunder__ methods as NamespaceProxy,
    # in addition to the b method.
    _exposed_ = ('__getattribute__', 
                 '__setattr__', 
                 '__delattr__', 
                 'Make_Sequential_Draw',
                 'Make_Simultanious_Draw',
                 'Make_Random_Player_Sequential',
                 'Make_FirstNumber_Player_Sequential',
                 'Make_Symbol_Player_Sequential',
                 'Make_SameNumber_Symbol_Player_Sequential',
                 'Make_OneDraw_Player_Sequential')

    def Make_Sequential_Draw(self):
        callmethod = object.__getattribute__(self, '_callmethod')
        return callmethod('Make_Sequential_Draw')
    def Make_Simultanious_Draw(self):
        callmethod = object.__getattribute__(self, '_callmethod')
        return callmethod('Make_Simultanious_Draw')
    def Make_Random_Player_Sequential(self):
        callmethod = object.__getattribute__(self, '_callmethod')
        return callmethod('Make_Random_Player_Sequential')
    def Make_FirstNumber_Player_Sequential(self):
        callmethod = object.__getattribute__(self, '_callmethod')
        return callmethod('Make_FirstNumber_Player_Sequential')
    def Make_Symbol_Player_Sequential(self):
        callmethod = object.__getattribute__(self, '_callmethod')
        return callmethod('Make_Symbol_Player_Sequential')
    def Make_SameNumber_Symbol_Player_Sequential(self):
        callmethod = object.__getattribute__(self, '_callmethod')
        return callmethod('Make_SameNumber_Symbol_Player_Sequential')
    def Make_OneDraw_Player_Sequential(self):
        callmethod = object.__getattribute__(self, '_callmethod')
        return callmethod('Make_OneDraw_Player_Sequential')

#handle SIGINT from SyncManager object
def mgr_sig_handler(signal, frame):
    print("not closing the mgr")

#initilizer for SyncManager
def mgr_init():
    signal.signal(signal.SIGINT, mgr_sig_handler)
    #signal.signal(signal.SIGINT, signal.SIG_IGN) # <- OR do this to just ignore the signal
    print("initialized mananger")

MyManager.register('Config', Config, ConfigProxy)

class Simulation(object):
    def __init__(self, n):
        self.n = n
        self.players = []
        self.cpus = mp.cpu_count()

        self.operations = divmod(n, self.cpus) # Equal operations per thread/cpu
        self.sims = [self.operations[0]] * self.cpus # x simulations per thread
        self.sims[-1] += self.operations[1] # if there is a remainder of operations, add it to the last
        
        self.PROGRESS = []
        for x in range(0, len(self.sims)):
            self.PROGRESS.append(Progression(x, self.sims[x]))

    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def Simulate(self, progress, players, shared_obj, config):
        p = psutil.Process()
        p.cpu_affinity([progress.cpu])
        progress.started = time.time()

        progress.state = "INITIALZING"
        shared_obj["CPU_{0}_PROGRESS".format(progress.cpu)] = progress.to_pickle()

        progress.state = "WORKING"
        for i in range(0, progress.total):
            Draw_SEQ = config.Make_Sequential_Draw()
            Draw_SIM = config.Make_Simultanious_Draw()

            for p in players:
                p.Analyze(seq_draw = Draw_SEQ, sim_draw=Draw_SIM)

            progress.Update(1)
            shared_obj["CPU_{0}_PROGRESS".format(progress.cpu)] = progress.to_pickle()
            for j in range(0, len(players)):
                shared_obj["CPU_{0}_PLAYERS_{1}".format(progress.cpu, j)] = players[j].to_pickle()

        progress.state = "FINISHED"
        shared_obj["CPU_{0}_PROGRESS".format(progress.cpu)] = progress.to_pickle()

    
    def Run(self):

        c_manager = MyManager()
        c_manager.start(mgr_init)

        print("making config manager")
        shared_config = c_manager.Config(display=True)

        print("Making Players")
        self.players.append(Player(name="Random Player", draws=shared_config.Make_Random_Player_Sequential()))
        self.players.append(Player(name="First Number Player", draws=shared_config.Make_FirstNumber_Player_Sequential()))
        self.players.append(Player(name="Symbol Player", draws=shared_config.Make_Symbol_Player_Sequential()))
        self.players.append(Player(name="SNAS Player", draws=shared_config.Make_SameNumber_Symbol_Player_Sequential()))
        self.players.append(Player(name="One Draw Player", draws=shared_config.Make_OneDraw_Player_Sequential()))

        manager = mp.Manager()
        shared_obj = manager.dict()

        for i in range(0, len(self.PROGRESS)):
            shared_obj["CPU_{0}_PROGRESS".format(self.PROGRESS[i].cpu)] = None
            for j in range(0, len(self.players)):
                shared_obj["CPU_{0}_PLAYERS_{1}".format(self.PROGRESS[i].cpu, j)] = None


        print("Preparing Multi-CPU Jobs")
        for i in range(0, len(self.PROGRESS)):
            p = mp.Process(target=self.Simulate, args=(self.PROGRESS[i], self.players, shared_obj, shared_config,))
            p.daemon = True
            p.start()

        print("ALL CPU Jobs ready to go!")
        total_started = time.time()
        while True:
            updated_players = self.players.copy()

            for i in range(0, len(self.PROGRESS)):
                recv_progress = shared_obj["CPU_{0}_PROGRESS".format(self.PROGRESS[i].cpu)]
                if recv_progress != None:
                    self.PROGRESS[i] = Progression.from_pickle(recv_progress)

                recv_players = []
                for j in range(0, len(updated_players)):
                    received = shared_obj["CPU_{0}_PLAYERS_{1}".format(self.PROGRESS[i].cpu, j)]
                    if received != None:
                        nplayer = Player.from_pickle(received)
                        recv_players.append(nplayer)
                
                if len(recv_players) == len(updated_players):
                    for x in range(0, len(updated_players)):
                        updated_players[x] = updated_players[x] + recv_players[x]

            stop = True
            display = ""
            for progress in self.PROGRESS:
                if progress.IsFinished() == False:
                    stop = False
                display += progress.__str__() + "\n"

            total_elapsed = int(time.time() - total_started)
            total_elapsed_str = 'Total Elapsed: {:02d}:{:02d}:{:02d}'.format(total_elapsed  // 3600, (total_elapsed  % 3600 // 60), total_elapsed  % 60)


            p_results = ""
            for player in updated_players:
                p_results += player.get_status()

            display += p_results
            display += total_elapsed_str


            self.cls()
            print(display)

            if stop:
                with open("RESULTS.txt", "w") as file:
                    text = ""
                    for player in updated_players:
                        text += player.__str__()
                    text += display
                    file.writelines(text)
                break
            else:
                time.sleep(10) #sleep 10 seconds (adjustable, even 1 don't matter, its just for screen)