# e = "Live from New York, it's Saturday Night"
# x = e.split(' ')
# for e in x:
#     print(e[0].upper())


def acronym(someString):
    for i in someString.split():
        val = i[0].upper()
        print(val)
        
print(acronym("Live from New York, it's Saturday Night"))
# print(acronym("Here we go again"))
