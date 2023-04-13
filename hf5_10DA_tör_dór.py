t = list(map(lambda x: list(map(int, x.split("-"))),open("input.txt").read().split("\n")))

l = list(filter( lambda x: x<9, t[0]))

print("2. feladat")
print(f'Az 1. sorban szereplő 9-nél kisebb számok maximuma: {max(l)}')

q = list(sorted(t[1]))[:15]
s = 1
for i in q:
    s *= i

print("3. feladat")
print(f' A  2. sorban szereplő 15 legkisebb szám szorzatának nagyságrendje: {len(str(s))}')