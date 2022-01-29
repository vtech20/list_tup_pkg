import logging

class tuple_class:

    def __init__(self, tup):
        self.tup = tup
        try:
            if type(self.tup) != tuple:
                raise ValueError("Input is not a Tuple")
        except Exception as e:
            print(e)

    def tuple_index(self, elem):
        try:
            j = 0
            for i in self.tup:
                if i != elem:
                    j = j + 1
                else:
                    break
        except Exception as e:
            logging.exception(e)

        return j

    def tuple_count(self, elem):
        try:
            j = 0
            for i in self.tup:
                if i == elem:
                    j = j + 1
        except Exception as e:
            logging.exception(e)

        return j
