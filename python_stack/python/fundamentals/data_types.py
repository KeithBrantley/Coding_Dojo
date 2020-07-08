# # # is_hungry = True
# # # has_freckles = False

# # # age = 39
# # # weight = 170.60

# # # name = "Joe Blue"

# # # dog = ("Bruce", "cocker spaniel", 19, False)
# # # print(dog[0])
# # # dog[1] = "daschund"

# # empty_list = []
# # ninjas = ["Rozen", "KB", "Quiver"]
# # print(ninjas[2])
# # ninjas[0] = "Francis"
# # print(ninjas)
# # ninjas.append("Michael")
# # print(ninjas)
# # ninjas.pop()
# # print(ninjas)
# # ninjas.pop(1)
# # print(ninjas)

empty_dict = {}
new_person = {"name": "John", "age": 38, "weight": 160.2, "has_glasses": False}
new_person["name"] = "Jack"
new_person["hobbies"] = ["climbing", "coding"]
print(new_person)

w = new_person.pop("weight")
print(w)
print(new_person)

print(type(2.63))
print(type((new_person)))

print(len(new_person))
print(len("Coding Dojo"))