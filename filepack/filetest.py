fo = open("D:\\a.out", "r")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
for line in fo:
 print(line)
fo.close()