"""
Dictionaries are a convenient way to store data for later retrieval by name (key).
Keys must be unique, immutable objects, and are typically strings. The values in a
dictionary can be anything. For many applications the values are simple types such as integers and strings.

It gets more interesting when the values in a dictionary are collections (lists, dicts, etc.)
In this case, the value (an empty list or dict) must be initialized the first time a given key is used.
While this is relatively easy to do manually, the defaultdict type automates and simplifies these kinds
of operations.

A defaultdict works exactly like a normal dict, but it is initialized with a function (“default factory”)
that takes no arguments and provides the default value for a nonexistent key.

A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the
default factory.
"""

from collections import defaultdict
from collections import Counter


print("\nExample 1...\n")
ice_cream = defaultdict(lambda: 'Vanilla')
ice_cream['chet'] = 'chunky monkey'
print(ice_cream['joe'])
print(ice_cream)

print("\n\nExample 2...\n")
food_list = 'spam spam spam spam eggs spam'.split()
print(type(food_list))
food_count = defaultdict(int)  # default value of int it is 0
for food in food_list:
    food_count[food] += 1  # increment elements' value by 1

print(food_list)
print(food_count)


print("\n\nExample 3...\n")
city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'),
             ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'),
             ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'),
             ('GA', 'Atlanta')]

cities_by_state = defaultdict(list)
for state, city in city_list:
    cities_by_state[state].append(city)
for state, cities in cities_by_state.items():
    print(state, ', '.join(cities))


print("\n\nExample 4...\n")
city_list2 = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'),
             ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'),
             ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'),
             ('GA', 'Atlanta'), ('TX', 'Austin'), ('IL', 'Chicago')]

cities_by_state2 = defaultdict(Counter)

for s, c in city_list2:
    cities_by_state2[s.strip()][c.strip()] += 1

for state, city in sorted(cities_by_state2.items()):
    print(state)
    for one_city, total in sorted(city.items()):
        if total == 1:
            print(f'\t{one_city}')
        else:
            print(f'\t{one_city} ({total})')




