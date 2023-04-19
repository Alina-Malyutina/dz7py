text = input('Enter text: ').lower().split()
func = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя')
fir = func(text[0])
if all([func(i) == fir for i in text]):
    print('Парам пам-пам')
else:
    print('Пам парам')

