import requests
import json
import random

from Draw import *
import tqdm
import time
        
API_KEY = 'e3ea18b1-7960-4ad3-9ee9-fe64ed88f732'

class Randomizer(object):
    def __init__(self, display):
        self.display = display
        self.n_10_list = []
        self.n_12_list = []
        self.possibilities = []

        if self.__load():
            if self.display:
                print("Using local random value files.")
        else:
            if self.display:
                print("No local values found, getting online values")
            self.__gen_10_list()
            self.__gen_12_list()

        if self.display:
            print("Generating possibility list")

        self.__gen_possibilities()     

        if self.display:
            print("------------------------------------------------------------")
            print("RANDOMIZER INITIALIAZED")
            print("Total possibilities: ", len(self.possibilities))
            print("n_10 list count:" , len(self.n_10_list))
            print("n_12 list count:" , len(self.n_12_list))
            print("------------------------------------------------------------")
            print("")

    def __gen_10_list(self):

        url = 'https://api.random.org/json-rpc/1/invoke'
        data = {'jsonrpc':'2.0','method':'generateIntegers','params': {'apiKey': API_KEY,'n':10000,'min':0,'max':9,'replacement':'true','base':10},'id':666}
        params = json.dumps(data)
        response = requests.post(url,params)

        if (response.status_code == 200):
            json_data = json.loads(response.text)
            #print(json_data)
            self.n_10_list = json_data['result']['random']['data']

            #save new list to file
            with open("n_10.txt", "w") as file:
                json.dump(self.n_10_list, file)
        else:
            print(response.text)
            raise 'Getting them randomz failed (10) :/ (check api key?)'

    def __gen_12_list(self):

        url = 'https://api.random.org/json-rpc/1/invoke'
        data = {'jsonrpc':'2.0','method':'generateIntegers','params': {'apiKey': API_KEY,'n':10000,'min':0,'max':11,'replacement':'true','base':10},'id':777}
        params = json.dumps(data)
        response = requests.post(url,params)

        if (response.status_code == 200):
            json_data = json.loads(response.text)
            #print(json_data)
            self.n_12_list = json_data['result']['random']['data']

            #save new list to file
            with open("n_12.txt", "w") as file:
                json.dump(self.n_12_list, file)
        else:
            print(response.text)
            raise 'Getting them randomz (12) failed :/ (check api key?)'

    def __gen_possibilities(self):

        if self.display:
            pbar = tqdm.tqdm(total=12000000)
            for x in range(0, 1000000):
                for y in range(0, 12):
                    self.possibilities.append(Draw(x, y))
                pbar.update(12)
            pbar.close()
        else:
            for x in range(0, 1000000):
                for y in range(0, 12):
                    self.possibilities.append(Draw(x, y))

    def __load(self):
        try:
            with open("n_10.txt", "r") as file:
                self.n_10_list = json.load(file)
            with open("n_12.txt", "r") as file:
                self.n_12_list = json.load(file)

            if len(self.n_10_list) != 0 and len(self.n_12_list) != 0:
                return True
            else:
                return False
        except:
            print("Problem reading files...")
            return False


    #Returns a single random decimal number between 0-9 [Sequential Transition]
    def Get_10(self):
        time.sleep(0.0000001) #Sleep 0.001 seconds (to adjust the seed)
        random.seed(time.time()) #Get a new seed => seed is the variable that defines the internal list of "RANDOMS"
        obj_i = random.randint(0, len(self.n_10_list)-1) #Get a random number out of our own list based upon a local random number.
        return self.n_10_list[obj_i]

    #Returns a single random decimal number between 0-11 [Sequential Transition]
    def Get_12(self):
        time.sleep(0.0000001)
        random.seed(time.time())
        obj_i = random.randint(0, len(self.n_12_list)-1)
        return self.n_12_list[obj_i]

    #Returns a random draw out of all the possibilities [Simultanious Transition]
    def Get_SIM_Draw(self):
        time.sleep(0.0000001)
        random.seed(time.time())
        obj_i = random.randint(0, len(self.possibilities)-1)
        return self.possibilities[obj_i]