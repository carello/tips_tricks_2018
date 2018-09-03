

class Books(object):
    def __init__(self, *books):
        self._books = books


    def __iter__(self):
        return iter(self._books)

    def __str__(self):
        return "My Books: {}".format(self._books)


bks1 = Books(['red', 'blue', 'green', ])
bks2 = Books(['yellow', 'thin', 'boring', ])

for b in bks1:
    print(b)

print(bks2)
