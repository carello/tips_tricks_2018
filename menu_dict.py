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
    print("--- Enter a selection number ---")
    for i, e in enumerate(menu_items):
        for k, v in e.items():
            print('[{}] {}'.format(i + 1, k))

    choice = input("Enter number from menu >>: ").strip()
    if choice.isalnum():
        if choice <= str(len(menu_items)):
            for k, v, in menu_items[int(choice) - 1].items():
                print(v())
    else:
        print("Please make a selection from the menu")


    # Alt method, same outcome
    #result = menu_items[int(choice)]
    #v = result.values()
    #for i in v:
    #    print(i())