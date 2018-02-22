stud = [('dave', 'B', 24), ('jane', 'C', 12), ('john', 'A', 15)]
dudes = [('dave', 20), ('susie', 24), ('john', 28)]

val_dict = dict(dave=300, susie=200, john=100)


def test(card):
    age_value = card[1]
    new_age = age_value + val_dict[card[0]]
    print(card, new_age)

    return new_age

#print(sorted(stud, key=itemgetter(2))[0])


for c in sorted(dudes, key=test):
    print()
    print(c)

