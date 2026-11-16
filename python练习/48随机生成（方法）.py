import random

# randint(a, b)：随机生成一个整数，范围是 a 到 b，两端都包含。
# 这里是 1 到 100，包含 1 和 100。
print(random.randint(1, 100))

# randrange(start, stop, step)：按步长从范围内取一个整数。
# 包含 start，不包含 stop。不写 step 时步长默认为 1。
# 这里是 1、2、3 … 99，不包含 100。若要步长为 2，应写成 randrange(1, 100, 2)。
print(random.randrange(1, 100,2))

# choice(序列)：从列表、元组或字符串里随机选出 1 个元素并返回。
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# shuffle(列表)：把列表里的元素原地打乱，直接修改原列表。
# 它没有返回值，返回的是 None，所以 print 会输出 None。
#元组  字符串不能打更改
print(random.shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
