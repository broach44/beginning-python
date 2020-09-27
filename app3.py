# from ecommerce import shipping
import random
#
# shipping.calc_shipping()
#
# for i in range(3):
#     print(random.randint(10, 20))
#
# members = ['John', 'Mary', 'Bob', 'Mosh']
# leader = random.choice(members)
# print(leader)


class Dice:
    def roll(self):
        first_roll = random.randint(1, 6)
        second_roll = random.randint(1, 6)
        return first_roll, second_roll


dice1 = Dice()

print(dice1.roll())
