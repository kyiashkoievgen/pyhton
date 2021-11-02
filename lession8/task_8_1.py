class Data:

    def __init__(self, dat):
        self.dat = dat

    @classmethod
    def first_method(cls, d):
        cls.number = list(map(int, d.split("-")))
        Data.valid(cls.number)

    @staticmethod
    def valid(num):
        if num[0] > 30 or num[0] < 1 or num[1] > 12 or num[1] <1 or num[2] < 1:
            raise ValueError("дата не правельная")


data = Data("10-10-2021")
data.first_method("10-10-2021")
print(data.number)
