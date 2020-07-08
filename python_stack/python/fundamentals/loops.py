# for x in range(0, 10, 1):
#     print(x)
# for x in range(0, 10):
#     print(x)
# for x in range(10):
#     print(x)

# for x in range(0, 20, 2):
#     print(x)
# for x in range(20, 10, -5):
#     print(x)

# my_list = ("abc", 123, "xyz")
# for i in range(0, len(my_list)):
#     print(i, my_list[i])

# for v in my_list:
#     print(v)

# my_dict = { "name": "Noelle", "language": "Python" }
# for k in my_dict:
#     print(k)

# my_dict = {"name": "Noelle", "language": "Python" }
# for k in my_dict:
#     print(my_dict[k])

capitals = {"Washington": "Olympia", "California": "Sacremento", "Idaho": "Boise", "Illinois": "Springfield", "Texas": "Austin", "Oklahoma": "Oklahoma City", "Virginia": "Richmond"}

for key in capitals.keys():
    print(key)

for val in capitals.values():
    print(val)

for key, val in capitals.items():
    print(key, " = ", val)