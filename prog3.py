s = input('Введите	строку:	')
s1 = ''
for	c in	s:				#перебирает	все	символы	в	строке	s
 if c == 'а':	#если	значение	переменной	совпадает	с	«а»
    c = 'б' #то	заменяем	ее	на	букву	«б»
 s1 = s1 + c
print (s1)