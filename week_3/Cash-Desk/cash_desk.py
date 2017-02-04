class Bill:
    def __init__(self, amount):
        self.amount = amount
        type_chek = type(self.amount)

        if type_chek != int:
            raise TypeError('Wrong type entered!!!-{}'.format(type_chek))

        if self.amount < 0:
            raise ValueError('You have no money: {}'.format(self.amount))

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return int(self.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.__str__())

    def __gt__(self, other):
        return self.amount > other.amount

    def __le__(self, other):
        return self.amount < other.amount


class BatchBill:

    def __init__(self, values):
        self.values = values

    def __len__(self):
        return len(self.values)

    def total(self):
        return sum(bills=[Bill(value) for value in values])

    def __getitem__(self, index):
        return self.values[index]

    def total(self):
        return sum([int(value) for value in self.values])

class CashDesk:
    def __init__(self):
        self.money= {}

    def count_bills(self, Bill):
        if Bill.__int__() in self.money.keys():
            self.money[Bill.__int__()] += 1
        else:
            self.money[Bill.__int__()] = 1

    def take_money(self, money):
        if isinstance(money, Bill):
            if money not in self.money.keys():
                self.money[money] = 0
            self.money[money] += 1
        elif isinstance(money, BatchBill):
            for index in money:
                if index not in self.money.keys():
                    self.money[index] = 0
                self.money[index] +=1

    def total(self):
        return sum([int(value) * self.money[value] for value in self.money.keys()])

    def inspect(self):
        print_info = []
        print_info.append('We have a total of {}$ in the desk'
                          .format(self.total()))
        print_info.append('We have the following count of bills, sorted in ascending order:')

        # for bill, count in sorted(self.money.items(), key=operator.itemgetter(0)):
        #     print_info.append("{}$ bills - {}".format(bill.value, count))
        for key, value in sorted(self.money.items()):
            print_info.append("{0}$ bills - {1}".format(key.amount, value))


        return "\n".join(print_info)
