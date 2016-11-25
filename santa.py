import random

nimed = ['Tiina', 'Marko', 'Margusja', 'Kristina', 'Kirsi', 'Toomas', 'Anti', 'Kertu', 'Kristel']
ei_tohi = [
    ['Marko', 'Tiina'],
    ['Margusja', 'Kristina'],
    ['Kirsi', 'Toomas'],
    ['Anti', 'Kertu'],
    ['Kristel', 'Kristina']
]

def valid(a, b):
    for x in range(len(a)):
        if a[x] == b[x]:
            return False

        paar = [a[x], b[x]]
        if paar in ei_tohi or paar.reverse() in ei_tohi:
            print(paar, 'on keelatud')
            return False

    return True

kellelt = list(nimed)
kellele = list(nimed)

while not valid(kellelt, kellele):
    random.shuffle(kellelt)
    random.shuffle(kellele)

print('----')
for x in range(len(kellelt)):
    print(kellelt[x], '->', kellele[x])

