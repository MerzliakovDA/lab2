def sum(n):	
    sum = 0
    while	n>0:	
        sum += n % 10
        n = n // 10
    return sum	
#основная	программа	
k = int(input('Введите	число:	'))
while	k	>	9:		#пока	сумма	цифр	не	будет	одной	цифрой
    k = sum(k) #вызываем	функцию
if	k%3==0:
   print ('Число	делится	на	3')
else:
   print ('Число	не	делится	на	3')