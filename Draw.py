class Draw(object):
    def __init__(self, number=None, symbol=None):
        if number == None and symbol == None:
            self.n_1 = None
            self.n_2 = None
            self.n_3 = None
            self.n_4 = None
            self.n_5 = None
            self.n_6 = None
            self.symbol = None
        else:
            if number < 0 or number > 999999:
                raise 'Invalid Number Boi'

            if symbol < 0 or symbol > 11:
                raise 'Invalid Symbol Boi'

            str_number = "{:06d}".format(number)
            self.n_1 = int(str_number[0])
            self.n_2 = int(str_number[1])
            self.n_3 = int(str_number[2])
            self.n_4 = int(str_number[3])
            self.n_5 = int(str_number[4])
            self.n_6 = int(str_number[5])
            self.symbol = symbol

    def __eq__(self, other, *attributes):
        if not isinstance(other, type(self)):
            return NotImplemented

        if attributes:
            d = float('NaN')  # default that won't compare equal, even with itself
            return all(self.__dict__.get(a, d) == other.__dict__.get(a, d) for a in attributes)

        return self.__dict__ == other.__dict__

    def __str__(self):
        return "{0}-{1}-{2}-{3}-{4}-{5} Sym:{6}".format(self.n_1,
                                                      self.n_2,
                                                      self.n_3,
                                                      self.n_4,
                                                      self.n_5,
                                                      self.n_6,
                                                      self.symbol)