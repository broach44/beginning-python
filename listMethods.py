# numbers = [5, 2, 1, 7, 5, 4]
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers)
# print(numbers2)

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)


print(uniques)