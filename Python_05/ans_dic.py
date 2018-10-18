#!/usr/bin/env python3
fav_dic = { 'color': 'blue' ,'animal': 'cat', 'subject': 'biology'}
print(fav_dic['color'])
fav_thing = 'color'
print(fav_dic[fav_thing])
print(fav_dic['animal'])
fav_thing = 'animal'
print(fav_dic[fav_thing])
fav_dic['organism'] = 'mitochondria'
fav_thing = 'organism'
print(fav_dic[fav_thing])
print(fav_dic.keys())
fav_dic['organism'] = 'not sure'

#Take a value from the command line for fav_thing and print the value of that item from the dictionary. Maybe you want to print out all the keys to the user so that they know what to pick from.
input_key = input('pick a value from color, animal, subject and organism:')
print('my favorite',input_key,'is:',fav_dic[input_key])

#Get the fav_thing from the command line and a new value for that key. Change the value with the user inputted value.
add_key = input('give a type of thing:')
add_value = input('what is your favorite?')
fav_dic[add_key] = add_value
print('your favorite',add_key,'is added to the dictionary')
print(fav_dic)

#Use a for loop to print out each key and value of the dictionary.
for f in fav_dic:
  print( f, fav_dic[f])
