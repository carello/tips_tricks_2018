#!/user/bin/env python3

"""
Example on using a dictionary to create a menu. The dictionary
values are calls to functions
"""


def foo():
    return "This is foo"


def bar():
    return "This is bar"


menu_items = [
    {"View foo": foo},
    {"View bar": bar},
    {"Exit": exit},
]

while True:

    for i, e in enumerate(menu_items):
        for k, v in e.items():
            print(i, k)

    print()
    choice = input(">>: ")
    for k, v, in menu_items[int(choice)].items():
        print('--> ', v())

    # Alt method, same outcome
    result = menu_items[int(choice)]
    v = result.values()
    for i in v:
        print(i())
