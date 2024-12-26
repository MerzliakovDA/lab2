import	random
number	=	random.randint(1,	25)
choices	=	0
while	choices	<	5:
    print('Угадай	число	между	1	and	25:')
    guess = input()
    guess = int(guess)
    choices	=	choices	+	1
    if	guess	<	number:	#если	число	пользователя	меньше	загаданного
        print ('Мое	число	больше	твоего')
    if	guess	>	number:	#если	число	пользователя	больше	загаданного
        print ('Мое	число	меньше	твоего')
    if	guess	==	number:	#если	число	пользователя	равно	загаданному 
       break
if	guess	==	number:
 print('Молодец!	Ты	угадал	число	с'	+	str(choices)	+	'попытки!')
else:
 print('К	сожалению,	ты	не	угадал	число.	Я	загадал'	+	str(number))
