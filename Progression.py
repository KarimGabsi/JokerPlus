import time
import pickle

class Progression(object):
    def __init__(self, cpu, n):
        self.cpu = cpu
        self.current = 0
        self.total = n
        self.finished = False
        self.elapsed = 0
        self.started = 0
        self.state = "DEFAULT"

    def Update(self, n):
        self.current += n
        self.elapsed = int(time.time() - self.started)
        if self.current == self.total:
            self.finished = True

    def IsFinished(self):
        return self.finished

    def to_pickle(self):
        return pickle.dumps(self, 0).decode()

    def from_pickle(data):
        return pickle.loads(data.encode())

    def __str__(self):
        elapsed_str = '{:02d}:{:02d}:{:02d}'.format(self.elapsed  // 3600, (self.elapsed  % 3600 // 60), self.elapsed  % 60)
        return "CPU: {0:02d} \t STATE: {1} \t {2} | {3} \t Elapsed Time: {4}".format(self.cpu, self.state, self.current, self.total, elapsed_str)