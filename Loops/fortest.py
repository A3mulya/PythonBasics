for letter in 'Python':
   print ('Current Letter :', letter)

proj = ['Scope', 'RBS',  'Discover']
for proj1 in proj:
   print( 'Current proj :', proj1)

   #----------------By Index
print("Index approach------------")
for index in range(len(proj)):
       print('Current fruit :', proj[index])

#-------------------Inner
print('Lasttttttttttttttttttttttttttttttt')
for num in range(10,20):
   for i in range(2,num):
      if num%i == 0:
         j=num/i
         print ('%d equals %d * %d' % (num,i,j))
         break
   else:
      print( num, 'is a prime number')