from module import *

a:float = float(input('kérem a téglalap "a" oldalának hosszát: '))
b:float = float(input('kérem a téglalap "b" oldalának hosszát: '))

kerulet = teglalap_kerulete(a, b)
terulet = teglalap_terulete(a, b)

print(f'a téglalap kerülete: {kerulet}')
print(f'a téglalap területe: {terulet}')

n:str = input('hogy hívnak? ')
d:str = input('milyen napszak van? ')

koszon(n, d)

valasz = input(f'hogy vagy ma {d}, {n}?')
