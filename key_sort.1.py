import operator

stud = [('chet', 'B', 24), ('ray', 'C', 122), ('connie', 'A', 15)]
dudes = [('dave', 20), ('susie', 24), ('john', 28)]

val_dict = dict(dave=300, susie=200, john=100)


def test(car):
    age_value = car[1]
    new_age = age_value + val_dict[car[0]]
    print(car, new_age)

    return new_age

print("this")
print(sorted(stud, key=operator.itemgetter(2))[1])

print('that')
for c in sorted(dudes, key=test):
    print()
    print(c)

