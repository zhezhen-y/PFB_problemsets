#!/usr/bin/env python3
v = "sapiens, erectus, neanderthalensis"
print(v)
v2 = v.split(',')
print(v2)
v3 = v2.copy()
print(sorted(v3))
print(sorted(v3, key=len))
