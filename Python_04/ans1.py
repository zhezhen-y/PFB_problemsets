#!/usr/bin/env python3
fav = ['a','b','c','d','e']
print(fav)
print(fav[2])
fav[2] = 'bird'
print(fav)
fav.append('new')
print(fav)
fav.insert(0,'i')
print(fav)
fav.insert(3,'i')
print(fav)
fav.pop()
print(fav)
fav.pop(0)
print(fav)
fav.pop(2)
print(fav)
fav_j = ",".join(fav)
print(fav_j)
