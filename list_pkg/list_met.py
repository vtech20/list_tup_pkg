import logging

class list_class:
    def __init__(self, lst):
        self.lst = lst
        try:
            if type(self.lst) != list:
                raise ValueError("Input is not a list")
        except Exception as e:
            print(e)

    def list_reverse(self):
        try:
            self.lst = self.lst[::-1]
        except Exception as e:
            logging.exception(e)
        return self.lst

    def list_clear(self):
        try:
            del self.lst[:]
        except Exception as e:
            logging.exception(e)
        return self.lst

    def list_count(self, elem):
        try:
            j = 0
            lst1 = [j + 1 for i in self.lst if i == elem]
        except Exception as e:
            logging.exception(e)
        return sum(lst1)

    def list_remove(self, elem):
        try:
            lst1 = [i for i in self.lst if i != elem]
            self.lst = lst1
        except Exception as e:
            logging.exception(e)
        return self.lst

    def list_pop(self, elem_idx):
        try:
            lst2 = [i for idx, i in enumerate(self.lst) if idx != elem_idx]
            self.lst = lst2
        except Exception as e:
            logging.exception(e)
        return self.lst

    def list_extend(self, new):
        try:
            size = len(self.lst)
            self.lst[size:] = new
        except Exception as e:
            logging.exception(e)
        return self.lst

    def list_append(self, new):
        try:
            size = len(self.lst)
            n1 = [new]
            self.lst = self.lst + n1
        except Exception as e:
            logging.exception(e)
        return self.lst

    def list_sort(self):
        try:
            for i in range(len(self.lst)):
                for j in range(len(self.lst)):
                    if (self.lst[i] < self.lst[j]):
                        self.lst[j], self.lst[i] = self.lst[i], self.lst[j]
        except Exception as e:
            logging.exception(e)
        return self.lst

    def list_insert(self, index, new_val):
        try:
            if index == 0:
                l1 = [new_val] + self.lst
                self.lst = l1
            elif index != 0:
                l1 = self.lst[0:index] + [new_val] + self.lst[index:]
                self.lst = l1
        except Exception as e:
            logging.exception(e)
        return self.lst