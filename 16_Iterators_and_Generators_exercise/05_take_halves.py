def solution():
    def integers():
        value = 1
        while True:
            yield value
            value += 1

    def halves():
        for i in integers():
            yield i/2

    def take(n, seq):
        result=[]
        for num in seq:
            if len(result)==n:
                return result
            result.append(num)


    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
