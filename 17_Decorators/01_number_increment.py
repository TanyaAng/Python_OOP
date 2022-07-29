def number_increment(numbers):
    def increase():
        return [x + 1 for x in numbers]

    return increase()


# without **closure**
# def number_increment(numbers):
#     def increase(numbers):
#         return [x + 1 for x in numbers]
#
#     return increase(numbers)


print(number_increment([1, 2, 3]))
