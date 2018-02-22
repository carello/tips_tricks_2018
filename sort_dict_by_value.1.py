import operator
# Sorting a dictionary by value

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

print(sorted(xs.items(), key=lambda x: x[1]))

# Alternate method by operator

print(sorted(xs.items(), key=operator.itemgetter(1)))

