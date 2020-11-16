import pickle

class Player(object):
    def __init__(self, name, draws,
                 plays = 0, drawscount = 0,
                 seq1 = 0, seq2 = 0, seq3 = 0, seq4 = 0, seq5 = 0, seq6 = 0,
                 seqwinnumbers = 0, seqwinsymbol = 0, seqwinjackpot = 0,
                 sim1 = 0, sim2 = 0, sim3 = 0, sim4 = 0, sim5 = 0, sim6 = 0,
                 simwinnumbers = 0, simwinsymbol = 0, simwinjackpot = 0):

        self.name = name
        self.draws = draws

        self.plays = plays
        self.drawscount = drawscount
        
        self.seq_1 = seq1
        self.seq_2 = seq2
        self.seq_3 = seq3
        self.seq_4 = seq4
        self.seq_5 = seq5
        self.seq_6 = seq6

        self.seq_win_numbers = seqwinnumbers
        self.seq_win_symbol = seqwinsymbol
        self.seq_win_jackpot = seqwinjackpot

        self.sim_1 = sim1
        self.sim_2 = sim2
        self.sim_3 = sim3
        self.sim_4 = sim4
        self.sim_5 = sim5
        self.sim_6 = sim6

        self.sim_win_numbers = simwinnumbers
        self.sim_win_symbol = simwinsymbol
        self.sim_win_jackpot = simwinjackpot

    def __add__(self, new):
        if self.name == new.name:
            total_plays = self.plays + new.plays
            total_drawcount = self.drawscount + new.drawscount
        
            total_seq1 = self.seq_1 + new.seq_1
            total_seq2 = self.seq_2 + new.seq_2
            total_seq3 = self.seq_3 + new.seq_3
            total_seq4 = self.seq_4 + new.seq_4
            total_seq5 = self.seq_5 + new.seq_5
            total_seq6 = self.seq_6 + new.seq_6

            total_seq_win_numbers = self.seq_win_numbers + new.seq_win_numbers
            total_seq_win_symbol = self.seq_win_symbol + new.seq_win_symbol
            total_seq_win_jackpot = self.seq_win_jackpot + new.seq_win_jackpot

            total_sim_1 = self.sim_1 + new.sim_1
            total_sim_2 = self.sim_2 + new.sim_2
            total_sim_3 = self.sim_3 + new.sim_3
            total_sim_4 = self.sim_4 + new.sim_4
            total_sim_5 = self.sim_5 + new.sim_5
            total_sim_6 = self.sim_6 + new.sim_6

            total_sim_win_numbers = self.sim_win_numbers + new.sim_win_numbers
            total_sim_win_symbol = self.sim_win_symbol + new.sim_win_symbol
            total_sim_win_jackpot = self.sim_win_jackpot + new.sim_win_jackpot

            return Player(self.name, self.draws,
                          total_plays, total_drawcount,
                          total_seq1, total_seq2, total_seq3, total_seq4, total_seq5, total_seq6,
                          total_seq_win_numbers, total_seq_win_symbol, total_seq_win_jackpot,
                          total_sim_1, total_sim_2, total_sim_3, total_sim_4, total_sim_5, total_sim_6,
                          total_sim_win_numbers, total_sim_win_symbol, total_sim_win_jackpot)
        else:
            raise "TRYING TO ADD WRONG NAME PLAYERS"

    def Analyze(self, seq_draw, sim_draw):
        #We analyze each time there is a draw
        self.plays += 1
        
        #How many draws does the player use (during the course of the whole simulations)?
        self.drawscount += len(self.draws)

        #COMPARISON (SEQUENTIAL)
        for x in self.draws:
            #Jackpot?
            if x == seq_draw:
                self.seq_win_jackpot += 1
                continue

            got_Symbol = x.__eq__(seq_draw, 'symbol')
            got_1 = x.__eq__(seq_draw, 'n_1')
            got_2 = x.__eq__(seq_draw, 'n_2')
            got_3 = x.__eq__(seq_draw, 'n_3')
            got_4 = x.__eq__(seq_draw, 'n_4')
            got_5 = x.__eq__(seq_draw, 'n_5')
            got_6 = x.__eq__(seq_draw, 'n_6')

            got_all = False
            if got_1 and got_2 and got_3 and got_4 and got_5 and got_6: #We got all 6 numbers?
                self.seq_win_numbers +=1
                got_all = True

            if got_all == False and got_Symbol == True: #We dont have 6 numbers, but we have symbol
                self.seq_win_symbol += 1

            # We got all numbers so we stop.
            if got_all:
                continue

            if got_1:
                self.seq_1 += 1
            if got_2:
                self.seq_2 += 1
            if got_3:
                self.seq_3 += 1
            if got_4:
                self.seq_4 += 1
            if got_5:
                self.seq_5 += 1
            if got_6:
                self.seq_6 += 1

                
        #COMPARISON (SIMULTANIOUS)
        for x in self.draws:
            #Jackpot?
            if x == sim_draw:
                self.sim_win_jackpot += 1
                continue

            got_Symbol = x.__eq__(sim_draw, 'symbol')
            got_1 = x.__eq__(sim_draw, 'n_1')
            got_2 = x.__eq__(sim_draw, 'n_2')
            got_3 = x.__eq__(sim_draw, 'n_3')
            got_4 = x.__eq__(sim_draw, 'n_4')
            got_5 = x.__eq__(sim_draw, 'n_5')
            got_6 = x.__eq__(sim_draw, 'n_6')

            got_all = False
            if got_1 and got_2 and got_3 and got_4 and got_5 and got_6: #We got all 6 numbers?
                self.sim_win_numbers +=1
                got_all = True

            if got_all == False and got_Symbol == True: #We dont have 6 numbers, but we have symbol
                self.sim_win_symbol += 1

            # We got all numbers so we stop.
            if got_all:
                continue

            if got_1:
                self.sim_1 += 1
            if got_2:
                self.sim_2 += 1
            if got_3:
                self.sim_3 += 1
            if got_4:
                self.sim_4 += 1
            if got_5:
                self.sim_5 += 1
            if got_6:
                self.sim_6 += 1

    def get_status(self):
        status = "----------------------------------------------------------------------------------------------------------------------------------\n"
        status += "Player: {0} \t Plays: {1} \t  DrawCount: {2} \t  DrawHand: {3}\n\n".format(self.name, self.plays, self.drawscount, len(self.draws))

        status += "Sequential -> \t\t n1: {0} \t n2: {1} \t n3: {2} \n \t\t\t n4: {3} \t n5: {4} \t n6: {5} \n" .format(self.seq_1, self.seq_2, self.seq_3, self.seq_4, self.seq_5, self.seq_6)
        status += "Sequential WINS -> \t All Numbers: {0} \t Symbol: {1} \t  Jackpot: {2} \n\n" .format(self.seq_win_numbers, self.seq_win_symbol, self.seq_win_jackpot)

        status += "Simultanious -> \t n1: {0} \t n2: {1} \t n3: {2} \n \t\t\t n4: {3} \t n5: {4} \t n6: {5} \n" .format(self.sim_1, self.sim_2, self.sim_3, self.sim_4, self.sim_5, self.sim_6)
        status += "Simultanious WINS -> \t All Numbers: {0} \t Symbol: {1} \t Jackpot: {2} \n" .format(self.sim_win_numbers, self.sim_win_symbol, self.sim_win_jackpot)
        status += "----------------------------------------------------------------------------------------------------------------------------------\n"

        return status

    def to_pickle(self):
        return pickle.dumps(self, 0).decode()

    def from_pickle(data):
        return pickle.loads(data.encode())

    def __str__(self):
        txt = "--------------------------\n"
        txt += "{0}\n".format(self.name)
        for x in self.draws:
            txt += "{0}\n".format(x)
        txt += "--------------------------\n"
        return txt