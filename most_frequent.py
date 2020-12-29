import operator

if __name__ == '__main__':

    str = 'mississippi'

    most_frequent = dict()
    for letter in str:
        if letter not in most_frequent:
            most_frequent[letter] = str.count(letter)

    order = sorted(most_frequent.items(), key=operator.itemgetter(1), reverse=True)
    print(order)
