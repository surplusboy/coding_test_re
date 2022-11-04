def my_answer():
    n = 1260
    coin = [500, 100, 50, 10]
    coin_count = list()

    for i in coin:
        count = n // i
        coin_count.append(count)
        n -= i * count

    return sum(coin_count)


def model_answer():
    n = 1260
    count = 0
    coin = [500, 100, 50, 10]

    for i in coin:
        count += n // i
        n %= i

    return count

print(my_answer())
print(model_answer())