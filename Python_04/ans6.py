#!/usr/bin/env python3
list = [101,2,15,22,95,33,2,27,72,15,52]
#print even values in the list
for l in list:
  if l % 2 == 0:
    print (l)
print("done")
#sort and print each element
list2 = sorted(list)
for l in list2:
  print(l)
print("done")

#take the even number and sum
even = [ l for l in list if l%2 == 0]

sum = 0
for e in even:
  sum = sum + e
print('sum of even numbers:', sum)

#take the odd number and sum
odd = [ l for l in list if l%2 != 0] 

sum2 = 0
for o in odd:
  sum2 = sum2 + o
print('sum of odd numbers:', sum2)
