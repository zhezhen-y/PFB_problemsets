#!/usr/bin/env python3
#Modifiy the script in the previous problem to write the contents to a new file called "Python_06_uc.txt"

fo = open('Python_06.txt', 'r')
fw = open('Python_06_uc.txt', 'w')
for line in fo:
  line_upper = line.upper()
  fw.write(line_upper)

fo.close()
fw.close()
print("Wrote to file 'Python_06_uc.txt'")
