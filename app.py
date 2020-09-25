# course = 'Python for Beginners'
#
# print(course.replace('beginners', 'Absolute Beginners'))
# print('python' in course)

# is_hot = True
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day!")
# print("Enjoy your day")


homePrice = 1000000
buyer_credit_statusIsGood = True

if buyer_credit_statusIsGood:
    print("Buyer needs to make a down payment of 10%")
    buyer_downPayment = homePrice * .1
else:
    print("Buyer needs to make a down payment of 20%")
    buyer_downPayment = homePrice * .2

print(f"Buyer's down payment: ${buyer_downPayment}");


