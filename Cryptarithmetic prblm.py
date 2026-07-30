from itertools import permutations

letters = "SENDMORY"

for p in permutations("0123456789", len(letters)):
    d = dict(zip(letters, p))

    if d['S'] == '0' or d['M'] == '0':
        continue

    SEND = int(d['S'] + d['E'] + d['N'] + d['D'])
    MORE = int(d['M'] + d['O'] + d['R'] + d['E'])
    MONEY = int(d['M'] + d['O'] + d['N'] + d['E'] + d['Y'])

    if SEND + MORE == MONEY:
        print("SEND =", SEND)
        print("MORE =", MORE)
        print("MONEY =", MONEY)
        break