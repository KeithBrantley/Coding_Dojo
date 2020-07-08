# Basics
for i in range(150 + 1):
    print(i)

# Multiples of five
for i in range(5, 1000+1, 5):
    print(i)

# Counting the Dojo Way
for i in range(1, 100+1):
    if i % 5 == 0:
        print('Dojo')
    if i % 10 == 0:
        print('Coding Dojo')
    else:
        print(i)

# Whoa. That Suckers Huge
for i in range(500000):
    sum = 0
    if i % 2 != 0:
        sum += i
print(sum)

# Countdown by fours
for i in range(2018, 0, -4):
    if i % 2 == 0:
        print(i)

# Flexible counter
low_num = 2
high_num = 9
mult = 3
for i in range(low_num, high_num+1):
    if i % mult == 0:
        print(i)