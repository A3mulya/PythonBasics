count = 9
while (count >=0):
   print('The count is:', count)
   count = count- 1

   #Inner While test

i = 2
while (i < 100):
   j = 2
   while (j <= (i / j)):
         if not (i % j): break
         j = j + 1
if (j > i / j):
   print(i, " is prime")
   i = i + 1